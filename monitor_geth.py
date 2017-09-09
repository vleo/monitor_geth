#!/usr/bin/python3

# Copyright Vassili Leonov (c) 2017 under GNU GPL v3.0 or later

import argparse
import logging
import subprocess
import re

parser = argparse.ArgumentParser(
    description='Show Etherum blockchain sync process state'
)

parser.add_argument("-v", "--verbose", help="verbosity: -v enable info, -vv enable debug",
                    action="count")

verbosity = parser.parse_args().verbose
if verbosity is not None:
  if verbosity > 1:
    logging.basicConfig(level=logging.DEBUG,format='%(levelname)s:%(message)s')
  elif verbosity == 1:
    logging.basicConfig(level=logging.INFO,format='%(levelname)s:%(message)s')

def getV(l,vn,vv0):
  m = re.match(' *'+vn+': *(?P<vv>\d+)',l)
  if m:
    vv = int(m.group('vv'))
    logging.debug("{:s}={:d}".format(vn,vv))
    return vv
  else:
    return vv0


try:
  result = subprocess.run(['./geth', '--exec','eth.syncing','attach'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except Exception as e:
  print(type(e),e)
  exit()


logging.info(result)

if result.returncode ==1:
  print("Can't attach to another geth process; exiting")
  exit()


output = result.stdout.decode('utf-8').split('\n')

highestBlock=None
currentBlock=None
knownStates=None
pulledStates=None
startingBlock=None


for l in output:
  logging.info(">>{}<<".format(l))
  if l == "false":
    print("geth process is not syncing (just started or already synced)")
    exit()
  highestBlock=getV(l,'highestBlock',highestBlock)
  currentBlock=getV(l,'currentBlock',currentBlock)
  knownStates=getV(l,'knownStates',knownStates)
  pulledStates=getV(l,'pulledStates',pulledStates)
  startingBlock=getV(l,'startingBlock',startingBlock)


print('blocks done = {:d}'.format(currentBlock-startingBlock))
print('blocks left = {:d}'.format(highestBlock-currentBlock))
print('states left = {:d}'.format(knownStates-pulledStates))
