# from email.errors import NonPrintableDefect
from ast import arg
from glob import glob
from pickle import NONE
import shutil
import tempfile
from os import listdir, path
# from xdrlib import ConversionError
from zipfile import ZipFile
import random
from traceback import format_exc
import codecs
from bs4 import BeautifulSoup
from sys import platform
import base64,requests,json
from urllib import parse
import adjust_new
import os,gzip
# import appsflyernew

global attribution
attribution = []
global session
session = []
global event
event = []
global sdk_click_data
sdk_click_data = []
global sdk_info
sdk_info = []
global adjust_data
adjust_data = {}
global firebase_data
firebase_data = {}

input_path = "logs"

file_name = listdir(input_path)[0]

input_file = input_path+"/"+file_name

# package_name = str(input("Please Enter Package Name"))

def main():
	# uncommnert below 5 lines
	temp_dir = tempfile.mkdtemp(prefix="C:/httplogs_",suffix="_"+str(random.randint(1000,9999)))
	print(temp_dir)
	zf = ZipFile(input_file,'r')
	zf.extractall(temp_dir)
	zf.close()
	# temp_dir = "E:/httplogs_0lyxxta9_5166"
	# print(listdir(temp_dir))

	try:
		dir_list = listdir(temp_dir)
		for x in dir_list:
			if x.endswith(".htm"):
				file_link = path.join(temp_dir,x)
				# print(file_link)
				log_list_html = BeautifulSoup(codecs.open(file_link,'r'),features="html.parser")
				tc1 = 0
				column_numbers = {"#":-1,"Result":-1,"Protocol":-1,"Host":-1,"URL":-1,"Body":-1}
				for row in log_list_html('tr'):
					if len(row('td')) == 0 and len(row('th')) > 0:
						i=0
						for i in range(len(row('th'))):
							column_number_key = row('th')[i].text
							if column_number_key in column_numbers:
								column_numbers[column_number_key]=i
						for column_number_key in column_numbers:
							if column_numbers.get(column_number_key) == -1:
								del column_numbers[column_number_key]
					elif len(row('td')) > 0 and len(row('th')) == 0:
						log_host = row('td')[column_numbers.get('Host')].text
						log_no = row('td')[column_numbers.get('#')].text
						url_path = row('td')[column_numbers.get('URL')].text
						links_html = row('td')[0]
						links = {"C":None,"S":None,"M":None}
						for link in row('td')[0]('a',href=True):
							if "linux" in platform:
								links[link.text] = link['href'].replace('\\','/')
							else:
								links[link.text] = link['href']
						request_file = None
						response_file = None
						if links.get('C'):
							request_file = path.join(temp_dir,links.get('C'))
						if links.get('S'):
							response_file = path.join(temp_dir,links.get('S'))

						# print(log_host)
						# exit()
						# parse_gcd_log(log_host, log_no, links, request_file, response_file,url_path)
						# print("Calling ___GCD")
							# print("# "+str(log_no)+", "+log_contentType,)
					else:
						print(row)
						print("*"*100)
					# print("~"*50)
					tc1 += 1
					# if tc1 == 100:
					# 	break
				# print(log_list_html.read())
				print(column_numbers)
		for x in dir_list:
			if x.endswith(".htm"):
				file_link = path.join(temp_dir,x)
				# print(file_link)
				log_list_html = BeautifulSoup(codecs.open(file_link,'r'),features="html.parser")
				tc1 = 0
				column_numbers = {"#":-1,"Result":-1,"Protocol":-1,"Host":-1,"URL":-1,"Body":-1}
				for row in log_list_html('tr'):
					if len(row('td')) == 0 and len(row('th')) > 0:
						i=0
						for i in range(len(row('th'))):
							column_number_key = row('th')[i].text
							if column_number_key in column_numbers:
								column_numbers[column_number_key]=i
						for column_number_key in column_numbers:
							if column_numbers.get(column_number_key) == -1:
								del column_numbers[column_number_key]
					elif len(row('td')) > 0 and len(row('th')) == 0:
						log_host = row('td')[column_numbers.get('Host')].text
						log_no = row('td')[column_numbers.get('#')].text
						url_path = row('td')[column_numbers.get('URL')].text
						links_html = row('td')[0]
						links = {"C":None,"S":None,"M":None}
						for link in row('td')[0]('a',href=True):
							if "linux" in platform:
								links[link.text] = link['href'].replace('\\','/')
							else:
								links[link.text] = link['href']
						request_file = None
						response_file = None
						if links.get('C'):
							request_file = path.join(temp_dir,links.get('C'))
						if links.get('S'):
							response_file = path.join(temp_dir,links.get('S'))

						# print(log_host)
						# exit()
						parse_single_log(log_host, log_no, links, request_file, response_file,url_path)
							# print("# "+str(log_no)+", "+log_contentType,)
					else:
						print(row)
						print("*"*100)
					# print("~"*50)
					tc1 += 1
					# if tc1 == 100:
					# 	break
				# print(log_list_html.read())
				print(column_numbers)

	except:
		error_out = format_exc()
		print(error_out)


	# uncomment below 3 line
	print("#"*50+"\nPress Enter to exit ...\n"+"#"*50)
	input("")
	os.remove(input_file)
	shutil.rmtree(temp_dir)




	# a = tempfile.shopeerandom1

# log = []
def parse_single_log(log_host, log_no, links, request_file, response_file,url_path):
	# print(log_host)
	# log.append(log_host)
	# exit()
	if "adjust" in log_host:
		# pass
		print("S"*100)
		print(links)
		print("**"*100)
		print((log_host, log_no, links, request_file, response_file,url_path))
		parse_adjust_request(filepath=request_file,log_host = log_host,url_path=url_path)
	elif "firebaseinstallations.googleapis.com" in log_host:
		print("F"*100)
		print(url_path)
		parse_firebase_request(filepath=request_file,log_host = log_host,url_path=url_path)






def parse_firebase_request(filepath=None,log_host= None,url_path=None):
	print(filepath)
	# print("hjgahgh"*100)
	print(log_host)
	firebase_data['url'] = url_path
	if filepath == None:
		print("Request parse appsflyer request function without passing request file path")
		return True
	if path.isfile(filepath):
		no = 0
		with open(filepath,'rb') as infile:
			# print("z"*100)
			# print(infile.read())
			# print("z"*100)
			for line in infile:
				# print(line)
				no += 1
				try:
					line1 = line.decode('utf-8').replace("\n","").replace("\r","")
					if "x-firebase-client" in line1:
						print("A"*100)
						print("*"*60+"x-firebase-client"+"*"*60)
						print(line1)
						b =  parse.urlparse(line1)
						print(b)
						b1 = b.path	
						print(b1)
						firebase_data['x-firebase-client'] = b1.strip()
					if "X-Android-Cert" in line1:
						print("A"*100)
						print("*"*60+"X-Android-Cert"+"*"*60)
						print(line1)
						b =  parse.urlparse(line1)
						print(b)
						b1 = b.path	
						print(b1)
						firebase_data['X-Android-Cert'] = b1.strip()
						# print("="*200)
					if "x-goog-api-key" in line1:
						print("A"*100)
						print("*"*60+"x-goog-api-key"+"*"*60)
						print(line1)
						b =  parse.urlparse(line1)
						print(b)
						b1 = b.path	
						print(b1)
						firebase_data['x-goog-api-key'] = b1.strip()
						print("="*200)
					# print(line1)
					# print(8)
					if line1 == "":
						print("~"*60+str(no))
						break

				except:
					pass
			# infile.seek(no-1)
			file_data = b""
			for line in infile:
				# print(line)
				file_data += line
			# print(file_data)
				
			print("#"*50)
			print("Final="*100)
			try:
				print(file_data)
				firebase_data['data'] = json.loads(file_data.decode())
			except:
				final_data = gzip.decompress(file_data)
				print(final_data)
				firebase_data['data'] = json.loads(final_data.decode())
				# print(file_data)
				# print(len(file_data))
		# print(codecs.open(filepath,'r').read())
	else:
		print("requested path is not a file")
		return True



def parse_adjust_request(filepath=None,log_host= None,url_path=None):
	print(filepath)
	# print("hjgahgh"*100)
	print(log_host)
	adjust_data['url'] = log_host
	if filepath == None:
		print("Request parse appsflyer request function without passing request file path")
		return True
	if path.isfile(filepath):
		no = 0
		with open(filepath,'rb') as infile:
			# print("z"*100)
			# print(infile.read())
			# print("z"*100)
			for line in infile:
				# print(line)
				no += 1
				try:
					line1 = line.decode('utf-8').replace("\n","").replace("\r","")
					if "Authorization" in line1:
						print("A"*100)
						print("*"*60+"Authorization"+"*"*60)
						print(line1)
						b =  parse.urlparse(line1)
						print(b)
						b1 = b.path
						b2 = b1.find('algorithm')
						# print(b2)
						adjust_data['auth_algo'] = b1[b2+11:].split('"')[0]
						print(b1[b2+11:].split('"')[0])
					if "Client-SDK" in line1:
						print("A"*100)
						print("*"*60+"Client"+"*"*60)
						print(line1)
						b =  parse.urlparse(line1)
						print(b)
						b1 = b.path	
						print(b1)
						adjust_data['sdkclient'] = b1.strip()
						print("="*200)
					if "Content-Type" in line1:
						print("A"*100)
						print("*"*60+"Content"+"*"*60)
						print(line1)
						b =  parse.urlparse(line1)
						print(b)
						b1 = b.path	
						print(b1)
						adjust_data['Content'] = b1.strip()
						print("="*200)
					print(line1)
					# print(8)
					if line1 == "":
						print("~"*60+str(no))
						break

				except:
					pass
			# infile.seek(no-1)
			file_data = b""
			for line in infile:
				# print(line)
				file_data += line
			# print(file_data)

			if url_path == '/session':
				da =file_data
				session.append(da)
				print(len(file_data))
				print("E"*100)
			elif url_path == '/event':
				# print("session"*100)
				da =file_data
				event.append(da)
				print(len(file_data))
			elif url_path.split('?')[0] == '/attribution':
				# print("session"*100)
				# da = file_data
				attribution.append(url_path.split('?')[1])
				# print("session"*100)
				# attribution = log_host.split('?')[1]
				print(len(file_data))
			elif url_path == '/sdk_click':
				da =file_data
				# event.append(da)
				sdk_click_data.append(da)
				print(len(file_data))
			elif url_path == '/sdk_info':
				da =file_data
				# event.append(da)
				sdk_info.append(da)
				print(len(file_data))
				# adjust_data['sdk_info'] = True
			# elif log_host == 'register':
			# 	Appsflyer_data['register'] =True
			else:
				
				print("#"*50)
				print(file_data)
				print(len(file_data))
		# print(codecs.open(filepath,'r').read())
	else:
		print("requested path is not a file")
		return True







def parse_query(t):
	import codecs  
	# byteData =t[0]
	try:
		q = codecs.decode(t, 'UTF-8') 
	except:
		q = t
	t2 = []
	q = q.strip()
	if q == "":
		return {}
	if q.startswith("?"):
		q = q[1:]
	arr = [pair.split("=") for pair in q.split("&")]
	args = {}
	for k, v in arr:
		args[k] = v

	return args




def event_parse(li):
	l2 = []
	event_list = []
	event_data = []
	patner_param = []
	for i in li:
		res = parse_query(i)
		l2.append(res)
	# print(l2)
	for i in l2:
		event_list.append(i.get('event_token'))

		if i.get('callback_params'):
			tempcall = parse.unquote(i.get('callback_params'))
		else:
			tempcall = {}
		if i.get('partner_params'):
			temppatner = parse.unquote(i.get('partner_params'))
		else:
			temppatner = {}
		tmp = {"event":i.get('event_token'),"callback":tempcall,"patner":temppatner}
		event_data.append(tmp)

	return event_data
	# return patner_param,call_back,l2[0],event_list
if __name__ == "__main__":
	main()
	# print(firebase_data)
	# exit()
	print("*"*50+"attribution"+"*"*50)
	if len(attribution) > 0:
		Atribution_data = parse_query(attribution[0])
		print(Atribution_data)

	print("*"*50+"session"+"*"*50)
	if len(session) > 0:
		Session_data = parse_query(session[0])
		print(Session_data)
	# # print()
	print("*"*50+"event"+"*"*50)
	if len(event) > 0:
		print(len(event))
		eventData = parse_query(event[0])
		eventlist = event_parse(event)
		# print(patner)
		# print(callback)
		# print(eve1)
		print(eventlist)
	else:
		# patner =[]
		# callback =[]  
		# eve1 = {}
		eventData  = []
		eventlist = []
	print("*"*50+"sdk_click_data"+"*"*50)
	if len(sdk_click_data) > 0:
		SdkClick_data = parse_query(sdk_click_data[0])
		print(SdkClick_data)
		# print(type(SdkClick_data))
	# exit()
	# print(sdk_click_data)
	print("*"*50+"sdk_info"+"*"*50)
	if len(sdk_info) > 0:
		Sdk_info_data = parse_query(sdk_info[0])
		print(Sdk_info_data)
	else:
		Sdk_info_data = {}
	# print(sdk_info)
	print(adjust_data)
	# print(log)
	adjust_new.file_creation(Session_data,adjust_data,Atribution_data,Sdk_info_data,SdkClick_data,eventlist,eventData,firebase_data)