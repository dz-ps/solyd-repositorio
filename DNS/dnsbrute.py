import sys

import dns.resolver

resolver = dns.resolver.Resolver()

print("DNS Brute by ZumakD")

try:
	target = sys.argv[1]
	wordlist = sys.argv[2]
except:
	print("Usage: python3 dnsbrute.py domain wordlist.txt or /usr/share/wordlists/dirb/common.txt")
	sys.exit()

try:
	with open(wordlist, "r") as arq:
		subdomains = arq.read().splitlines()
except:
	print("Wordlist not found")
	sys.exit()
	

for subdomain in subdomains:
	try:
		sub_target = "{}.{}".format(subdomain, target)
		results = resolver.resolve(sub_target, "A")
		for result in results:
			print("{} -> {}".format(sub_target, result))
	except:
	    	print("Could not find any subdomains")
