Vault tool #1
=============

When launched, the tool will ask the user for Vault token:
    `"Input Vault token (it will be hidden): "`

This token needs to be able to write the secrets for `secret_path` (default 'secret/ads').

The token will be used to login to Vault. User will then have the opportunity to provide private keys:
    `"Private key for node secret/ads/node0001 (it will be hidden): "`

Each private key is immediately written to Vault.

Notes
-----

All user input is hidden on the command line.

The default settings are:

::

    secret_path = 'secret/ads'  # Internal vault path for secrets.
    node_number = 16  # Number of nodes we want to provide keys for.

Default settings can be edited directly in the script.
