import sys, string
from OP_RETURN import *


if len(sys.argv)<4:
	sys.exit(
'''Usage:
python send-OP_RETURN.py <send-address> <send-amount> <metadata> <testnet (optional)>

Examples:
python send-OP_RETURN.py 149wHUMa41Xm2jnZtqgRx94uGbZD9kPXnS 0.001 'Hello, blockchain!'
python send-OP_RETURN.py 149wHUMa41Xm2jnZtqgRx94uGbZD9kPXnS 0.001 48656c6c6f2c20626c6f636b636861696e21
python send-OP_RETURN.py mzEJxCrdva57shpv62udriBBgMECmaPce4 0.001 'Hello, testnet blockchain!' 1'''
	)

dummy, send_address, send_amount, metadata = sys.argv[0:4]
if len(sys.argv)>4:
	testnet=bool(sys.argv[4])
else:
	testnet=False

metadata_from_hex=OP_RETURN_hex_to_bin(metadata)
if metadata_from_hex is not None:
	metadata=metadata_from_hex

result=OP_RETURN_send(send_address, float(send_amount), metadata, testnet)

if 'error' in result:
	print('Error: '+result['error'])
else:
	print('TxID: '+result['txid']+'\nWait a few seconds then check on: http://'+
		('testnet.' if testnet else '')+'coinsecrets.org/')
