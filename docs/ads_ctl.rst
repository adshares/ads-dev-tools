ADS daemon control tool
=======================
usage: ads_ctl [-h] [-i] [--data-dir DATA_DIR] [-w] [-d]
               {start,stop,clean,nodes,network,wait}

Start ADS nodes.

positional arguments:
  {start,stop,clean,nodes,network,wait}

optional arguments:
  -h, --help            show this help message and exit
  -i, --init            Initialize the first network node.
  --data-dir DATA_DIR   Writeable working directory.
  -w, --wait            Wait and make sure the daemon is working.
  -d, --debug           Enable debug mode

Notes
-----

ads_ctl modifies the genesis start time, so that it's in the future. It's the same for all nodes.

Debug option is used when calculating the new genesis time. Debug makes the new time a multiplicaiton of 32 seconds, instead of 512 seconds.

`--init` needs to be run only for one node in the network.

`nodes` and `network` return information about the state of the network. `nodes` checks the genesis of all nodes, while `network` queries live nodes for basic information.

`clean` removes all information from node configuration and all live files

`stop` asks the nodes to close politely using SIGTERM, then assassinates them using SIGKILL.
