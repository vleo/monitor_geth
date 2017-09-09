# monitor_geth

Simple python script to show Ethereum (ETH) geth process blockchain synchronization state:

```
$ ./monitor_geth.py -h
usage: monitor_geth.py [-h] [-v]

Show Etherum blockchain sync process state

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  verbosity: -v enable info, -vv enable debug
```
It is assumed, that another geth process is running, using 'attach' geth command to get info.
It is also assumed, that geth executable is in the current directory (./geth) when this script is run.
In other words, put this script to 
>/home/user/.config/Ethereum Wallet/binaries/Geth/unpacked
