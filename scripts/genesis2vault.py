#!/usr/bin/env python
from __future__ import print_function
import argparse
import getpass
import json
import os
import re
import subprocess

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen


class GenesisFile(object):
    """
    Genesis file object, with helper functions.
    """
    def __init__(self, genesis_file):
        """
        Read the file in.

        :param genesis_file: Genesis filepath or URL
        """

        if genesis_file.startswith('http'):
            genesis_response = urlopen(genesis_file)
            self.genesis = json.loads(genesis_response.read())
        else:
            with open(genesis_file, 'r') as f:
                self.genesis = json.load(f)

        self._genesis_dict()

    def _genesis_dict(self):
        self.nodes = {}
        for index, node in enumerate(self.genesis['nodes']):

            node_ident = self.node_identifier_from_accounts(node)
            if not node_ident:
                node_ident = '{0:04x}'.format(index)

            self.nodes[node_ident] = node

    def node_count(self):
        """
        Get number of nodes in genesis file

        :return: Number of nodes
        """
        return len(self.nodes)

    def node_data(self, node_number):
        """
        Get keys and signatures associated with this node.

        :param node_number: Node index number.
        :return: Tuple of private key, public key and signature.
        """
        node_config = self.nodes[node_number]
        return node_config['_secret'], node_config['public_key'], node_config['_sign']

    def node_identifier_from_accounts(self, node):
        """
        Get node identifiers from the first account identifier associated with this node.

        :return: List of identifiers.
        """
        for account in node['accounts']:
            addr = account["_address"]
            if re.search('-0{8}-', addr):
                return addr[:4]

    def node_identifier_from_public_key(self, pub_key):
        for node_id in self.nodes.keys():
            if self.nodes[node_id]['public_key'] == pub_key:
                return node_id

    def save(self, filepath):
        with open(filepath, 'w') as f:
            json.dump(self.genesis, f)


def get_keys_from_genesis(genesis):

    genesis_data = GenesisFile(genesis)
    keys = [(nid, genesis_data.nodes[nid]['_secret']) for nid in sorted(genesis_data.nodes.keys())]
    return keys


def write(keys, token, secret):

    subprocess.call(['vault', 'login', token])
    for nid, priv_key in keys:
        subprocess.call(['vault', 'write', '{0}/node{1}'.format(secret, nid), 'value={0}'.format(priv_key)])

    os.remove(os.path.expanduser('~/.vault-token'))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Copy private keys from a genesis file to Vault.')
    parser.add_argument('secret_path', help="Path to secrets")
    parser.add_argument('-g', '--genesis', help='Genesis URI (url or filepath)')

    args = parser.parse_args()

    keys = get_keys_from_genesis(args.genesis)
    token = getpass.getpass("Input Vault token (it will be hidden): ")

    write(keys, token, args.secret_path)
