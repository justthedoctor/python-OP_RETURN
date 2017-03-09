import sys, string
from OP_RETURN import *


if len(sys.argv)<2:
	sys.exit(
'''Usage:
python store-OP_RETURN.py <data> <testnet (optional)>'''
	)
	
data=sys.argv[1]

if len(sys.argv)>2:
	testnet=bool(sys.argv[2])
else:
	testnet=False

data_from_hex=OP_RETURN_hex_to_bin(data)
if data_from_hex is not None:
	data=data_from_hex

result=OP_RETURN_store(data, testnet)

if 'error' in result:
	print('Error: '+result['error'])
else:
	print("TxIDs:\n"+"\n".join(result['txids'])+"\n\nRef: "+result['ref']+"\n\nWait a few seconds then check on: http://"+
		('testnet.' if testnet else '')+'coinsecrets.org/')
