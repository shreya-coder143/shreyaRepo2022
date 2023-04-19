#-*- coding: utf-8 -*-


from subprocess import call,check_output
import subprocess
from os import listdir , rename
# from playstore_support import help
import ast
import json,sys,traceback
import requests
from bs4 import BeautifulSoup
import re as ser
import random,os
import google_play_scraper 

# import playstore
regex = '^[A-Za-z][A-Za-z0-9_]*'


def check(string,name12):

	if ser.search(regex, string) :
		name12['name'] = string
		print("Vlaid")
	else:
		print("Invalid Name Enter Valid Name")


def file_creation(Session_data,adjust_data,Atribution_data,Sdk_info_data,SdkClick_data,eventlist,eventData,firebase_data):

	name12 = {} 

	# global  package_name
	package_name =  Session_data.get('package_name')
	with open('playstore_support/pac.txt','w') as  file:
		file.write(package_name)




	print("============================== please wait finding App information from Playstore==============================")
	try:

		result =google_play_scraper.app(package_name)
		app_name = result.get('title')
		# print(app_name)
		os_ver = str(random.randint(6,9))
		app_size = random.randint(10,50)
		# print type(exit_code)
		# print len(exit_code)
	except:
		traceback.print_exc(file=sys.stdout)
		print("sorry app detail Not availbale on play store\n")
		# app_size = input("Enter app_size...............\n")
		app_name = str(input("Enter App Name...............\n"))
		os_ver = str(random.randint(6,9))
		app_size = random.randint(10,50)




	app = app_name
	print(app_name)
	inpu = 'temp.txt'
	try:
		with open(inpu,'w') as t :
			t.write(app)
	except:
		app_name = input("Enter app Name")
	print(app_name)
	os.remove(inpu)


	while(not name12.get('name')):
		name = str(input("Enter File name of app name only string...............\n"))

		check(name,name12)


	filename =  name12.get('name').replace(' ','')
	# print app.lower()




	# ==============================write intial import 

	txtfile = 'myfile/'+filename+'.py'

	l = [
    "import sys",
    "if int(sys.version_info.major) == 2:",
    "    py_version = 2",
    "else:",
    "    py_version = 3",
    "    import urllib.parse as urlparse",
	"from datetime import datetime,timedelta",
	"from sdk import installtimenew, util",
	"from hashlib import sha1",
	"import time, random, json, string, urllib, uuid, hashlib",
	"false = False",
	"true = True",
	"null = None"]

	f  = open(txtfile,'a')
	f.write("#-*- coding: utf-8 -*-")
	f.write('\n')
	f.write('# created by him@nshu')
	f.write('\n')
	for x in l:
		f.write(x)
		f.write('\n')

	f.write('\n')
	f.write('\n')

	f.close()






	if Atribution_data.get('app_secret'):
		app_secret =Atribution_data.get('app_secret')
	if Atribution_data.get('secret_id'):
		secret_id =Atribution_data.get('secret_id')
	package_name = Session_data.get('package_name')
	app_version_name =Session_data.get('app_version')
	app_token =Session_data.get('app_token')
	Client_SDK =adjust_data.get('sdkclient')
	eve  = []
	call_back = {}
	partner = {}





	# reading the data from the file
	with open('support_file/text.txt') as f:
		data = f.read()
	
	# print("Data type before reconstruction : ", type(data))
		
	# reconstructing the data as a dictionary
	d = ast.literal_eval(data)
	
	# print("Data type after reconstruction : ", type(d))
	d['adjust']['sdk'] = Client_SDK
	d['package_name'] = package_name
	d['app_version_name'] = app_version_name
	d['app_name'] =app_name
	d['link'] = ""
	try:
		d['app_size'] =int(app_size)
	except:
		d['app_size'] =random.randint(20,100)

	d['supported_os'] = os_ver
	d['adjust']['app_token'] = app_token
	if Atribution_data.get('app_secret'):
		d['adjust']['app_secret'] = app_secret
	if Atribution_data.get('secret_id'):
		d['adjust']['secret_id'] = secret_id




	# d2 = {}
	if Sdk_info_data:
		adjust_data['sdk_info'] = True
	adjust_data['initiated_by'] =Atribution_data.get('initiated_by')
	# d2['event_data'] =eve_list

	# d2['url'] =adjust_data.get('url')




	error = ["app_size","retention","country","adjust","tracker"]
	b = "campaign_data = "
	session = "session_data = "
	sdk_cilvk = "sdk_click_data = "
	sdk_info = "sdk_info_data = "
	atribution = "atribution_data = "
	even = "event_data = "
	details = "events_details = "
	adjust = 'adjust_data = '
	firebase = "firebase_data = "
	with open(txtfile, 'a',encoding="utf-8") as convert_file:
		convert_file.write(b)
		convert_file.write("{")
		convert_file.write("\n")

		li = d.items()
		for st in li:
			if st[0] in error:
				pass
			else:
				t = "   "+"'"+st[0]+"' : '"+st[1]+"',"

				convert_file.write(t)
				convert_file.write("\n")

		for key, value in d.items(): 
			if key in error:
				convert_file.write("   '%s' : %s,\n" % (key, value))

	
		convert_file.write("	}")
		convert_file.write("\n")


		convert_file.write(firebase)
		convert_file.write(json.dumps(firebase_data))
		convert_file.write("\n")
		convert_file.write("\n") 


	
		convert_file.write(adjust)
		convert_file.write(json.dumps(adjust_data))
		convert_file.write("\n")
		convert_file.write("\n") 
		


		convert_file.write(session)
		convert_file.write(json.dumps(Session_data))
		convert_file.write("\n")
		convert_file.write("\n") 
		

		convert_file.write(sdk_cilvk)
		# print(SdkClick_data)
		# print(type(SdkClick_data))
		try:
			convert_file.write(json.dumps(SdkClick_data.decode()))
			convert_file.write("\n")
			convert_file.write("\n")
		except:
			convert_file.write(json.dumps(SdkClick_data))
			convert_file.write("\n")
			convert_file.write("\n")

		if Sdk_info_data:
			convert_file.write(sdk_info)
			convert_file.write(json.dumps(Sdk_info_data))
			convert_file.write("\n")
			convert_file.write("\n")

		convert_file.write(atribution)
		convert_file.write(json.dumps(Atribution_data))
		convert_file.write("\n")
		convert_file.write("\n")

		convert_file.write(even)
		convert_file.write(json.dumps(eventData))
		convert_file.write("\n")
		convert_file.write("\n")

		convert_file.write(details)
		convert_file.write(json.dumps(eventlist))
		convert_file.write("\n")
		convert_file.write("\n")


	with open("support_file/t.txt") as f:
		with open(txtfile, "a") as f1:
			for line in f:
				f1.write(line)



	print("File Created")

