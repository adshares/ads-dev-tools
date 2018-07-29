Configuration tool
==================

usage: ads_configure [-h] [--node NODE] [--private-key PRIVATE_KEY]
                     [--genesis GENESIS] [--data-dir DATA_DIR]
                     [--interface INTERFACE] [--user-dirs] [--port PORT]
                     [--client-port CLIENT_PORT]

Configure ADS nodes.

optional arguments:
  -h, --help            show this help message and exit
  --node NODE           Node number
  --private-key PRIVATE_KEY
                        Private key for the node
  --genesis GENESIS     Genesis filepath or url
  --data-dir DATA_DIR   Writeable working directory.
  --interface INTERFACE
                        Interface this node is bound to.
  --user-dirs           Create account directories.
  --port PORT           Node port
  --client-port CLIENT_PORT
                        Node port

Notes
-----

If you provide node number argument, only one configuration will be created. If you provide private key at the same time, ads_configure will check if the key matches the node identifier and exit with a return code 1 if it doesn't.

If you provide the private key option, it will find the corresponding public key from the genesis file.

Genesis can be provided by either file path or URL. Irrespectively, a copy of it will be put int the node config directory.

Data dir is the directory which hosts all the node config directories. If --user-dir is provided, it also hosts user directories.

Account configuration directories are created only if --user-dirs is provided.
