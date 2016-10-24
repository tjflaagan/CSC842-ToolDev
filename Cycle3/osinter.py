#!/usr/bin/python3

import ipaddress
import collections
import argparse
import configparser
import censys
from censys import *


def scopeBuilder(args):
	with open(args.file) as f:
		data = f.readlines()

	seen = set()
	networks = []
	ll = []
	err = []
	
	for x in data:
		if x not in seen:
			networks.append(x)
			seen.add(x)
	
	for x in networks:
		for y in networks:
			x1 = ipaddress.IPv4Network(x.split('\n')[0], strict=False)
			y1 = ipaddress.IPv4Network(y.split('\n')[0], strict=False)
			if x1.overlaps(y1) and x != y:
				if x1.num_addresses >= y1.num_addresses:
					networks.remove(y)
				print(x, ' overlaps ', y)
	
	if args.iplist:
		for x in networks:
			try:
				for addr in ipaddress.IPv4Network(x, strict=False):
					ll.append(addr)
			except:
				err.append(x)
	else:
		for i in networks:
			ll.append(i)
	
	with open(args.output, 'w') as f:
		for i in ll:
			f.write(str(i) + '\n')

def censysFunc(config, args):
	
	uid = config['Censys']['uid']
	secret = config['Censys']['secret']
	
	api = censys.ipv4.CensysIPv4(api_id=uid, api_secret=secret)
	
	ll = []
	with open('subnetList.txt') as f:
		data = f.readlines()
	
	for ip in data:
		try:
			result = api.search(ip.split('\n')[0])
			# This is the time that I had to use to make sure I didn't hit the limit. Your rate may be different.
			time.sleep(2.6)
			print(list(result))
			ll.append(result)
		except:
			print('Error')
	
	with open('testout.txt', 'w') as f:
		for i in ll:
			f.write(str(list(i)))



def main():
	parser = argparse.ArgumentParser(prog="OSINTr", description='OSINTr')
	parser.add_argument('--file', '-f', type=str, help='Input list of subnets', required=False)
	parser.add_argument('--config', '-c', type=str, help='Config file', required=False)
	parser.add_argument('--output', '-o', type=str, help='Subnet output file', required=False, default='subnetList.txt')
	parser.add_argument('--buildScope', '-b', help='Build / Fix scope', required=False, default=False, action='store_true')
	parser.add_argument('--censys', help='Use censys', required=False, default=False, action='store_true')
	parser.add_argument('--iplist', '-i', help='Build entire IP list', required=False, default=False, action='store_true')

	args = parser.parse_args()
	censysCheck = args.censys
	buildScope = args.buildScope

	
	config = configparser.ConfigParser()
	config.sections()
	config.read('config.ini')

	if buildScope:
		scopeBuilder(args)

	if censysCheck:
		censysFunc(config, args)


if __name__ == '__main__':
    main()
