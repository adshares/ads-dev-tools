#!/usr/bin/env python
import getpass
import os
import subprocess

# config variables
secret_path = 'secret/ads'
node_number = 16

if __name__ == '__main__':

    # Login to vault
    token = getpass.getpass("Input Vault token (it will be hidden): ")
    subprocess.call(['vault', 'login', token])

    # Write nodes
    for nid in xrange(node_number):

        # Create the individual secret path, with node number in hex format
        node_secret_path = '{0}/node{1:04x}'.format(secret_path, nid + 1)

        # Grab private key from command line
        priv_key = getpass.getpass("Private key for node {0} (it will be hidden): ".format(node_secret_path))

        # Save to vault
        subprocess.call(['vault', 'write', node_secret_path, 'value={0}'.format(priv_key)])

    # Remove saved login token
    os.remove(os.path.expanduser('~/.vault_tokens'))
