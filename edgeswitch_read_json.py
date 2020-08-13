#!/usr/bin/env python3
# Usage ./edgeswitch_read_json.py SFPINDEX SEARCHDATA

import json
import sys


HOSTNAME_FILE = sys.argv[3]
HOSTNAME_FILE = HOSTNAME_FILE.replace(".","_")

with open('/tmp/edgeswitch_'+HOSTNAME_FILE+'_data.json', 'r') as json_file:
    dados = json.load(json_file)

item = sys.argv[1]
sfp_data = sys.argv[2]

# Define a function to search the item
def search_json (name):
 for keyval in dados:
  if name == keyval['SFP_INDEX']:
   return keyval[sfp_data]

# Check the return value and print message
if (search_json(item) != None):
  print(search_json(item))
else:
  print("0")
