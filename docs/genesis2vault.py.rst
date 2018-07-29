Vault tool #2
=============
usage: genesis2vault.py [-h] [-g GENESIS] [-t TOKEN] secret_path

Copy private keys from a genesis file to Vault.

positional arguments:
  secret_path           Path to secrets

optional arguments:
  -h, --help            show this help message and exit
  -g GENESIS, --genesis GENESIS
                        Genesis URI (url or filepath)
  -t TOKEN, --token TOKEN
                        Vault write token

Notes
-----

This tool copies private keys from a genesis file into Vault.

Each private key is individually written to Vault.

If `--token` is not provided, user will be asked to provide one from command line. All user input is hidden on the command line.
