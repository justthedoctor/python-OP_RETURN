import sys, string
from OP_RETURN import *


if len(sys.argv)<2:
	sys.exit(
'''Usage:
python retrieve-OP_RETURN.py <ref> <testnet (optional)>'''
	)

ref=sys.argv[1]

if len(sys.argv)>2:
	testnet=bool(sys.argv[2])
else:
	testnet=False

results=OP_RETURN_retrieve(ref, 1, testnet)

if 'error' in results:
	print('Error: '+results['error'])
	
elif len(results):
	for result in results:
		print("Hex: ("+str(len(result['data']))+" bytes)\n"+OP_RETURN_bin_to_hex(result['data'])+"\n")
		print("ASCII:\n"+re.sub(b'[^\x20-\x7E]', b'?', result['data']).decode('utf-8')+"\n")
		print("TxIDs: (count "+str(len(result['txids']))+")\n"+"\n".join(result['txids'])+"\n")
		print("Blocks:"+("\n"+("\n".join(map(str, result['heights'])))+"\n").replace("\n0\n", "\n[mempool]\n"))
		
		if 'ref' in result:
			print("Best ref:\n"+result['ref']+"\n")

		if 'error' in result:
			print("Error:\n"+result['error']+"\n")

else:
	print("No matching data was found")
