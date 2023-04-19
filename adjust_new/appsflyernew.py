# from wsgiref.validate import InputWrapper
# import appsflyer 
# from subprocess import call,check_output
import ast
import json
import requests
from bs4 import BeautifulSoup
import re as ser
import random
import traceback
import sys
import google_play_scraper 
regex = '^[A-Za-z][A-Za-z0-9_]*'


name12 = {} 

def check(string,name12):

     # pass the regular expression
     # and the string in search() method
    if ser.search(regex, string) :
        name12['name'] = string
        print("Vlaid")
    else:
        print("Invalid Name Enter Valid Name")

   # Enter the string


def file_creation(conversion_data,launchs_data,inapp_data,event_name,event_value,appsflyer_data,Apps_key):
    package_name =  appsflyer_data.get('id')
    
    


    # package_name =  appsflyer_data.get('id')
    # with open('playstore_support/pac.txt','w') as  file:
    #     file.write(package_name)



    print("============================== please wait finding App information from Playstore==============================")
    try:

        result =google_play_scraper.app(package_name)
        app_name = result.get('title')
        print(app_name)
        os_ver = str(random.randint(6,9))
        app_size = random.randint(10,50)
        # print type(exit_code)
        # print len(exit_code)
    except:
        traceback.print_exc(file=sys.stdout)
        print("sorry app detail Not availbale on play store\n")
        # app_size = input("Enter app_size...............\n")
        app_name = str(input("Enter App Name...............\n"))
        # os_ver = str(input("Enter Os version...............\n"))








    # app = app_name.replace(' ','')
    app = app_name
    print(app_name)
    # app1 =  app_name.replace('-','')
    # app1 = app.split('')[0]
    # filename = app.lower()
    # filename = "temp1"

    while(not name12.get('name')):
        name = str(input("Enter File name of app name only string...............\n"))

        check(name,name12)


    filename =  name12.get('name').replace(' ','')
    # print app.lower()




    # ==============================write intial import 

    txtfile = 'myfile/'+filename+'.py'

    l = ["import sys",
    "reload(sys)",
    "sys.setdefaultencoding('utf-8')",
    "from datetime import datetime",
    "from sdk import installtimenew, util, NameLists",
    "import clicker, Config",
    "from sdk import NameLists",
    "import time, random, json, string, urllib, uuid, hashlib",
    "from spicipher import af_cipher",
    "import sys ",
    "from collections import OrderedDict",
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





    # if atribution_data.get('app_secret'):
    #     app_secret = atribution_data.get('app_secret')
    # if atribution_data.get('secret_id'):
    #     secret_id = atribution_data.get('secret_id')
    package_name =  appsflyer_data.get('id')
    app_version_name = conversion_data.get('app_version_name')
    app_version_code = conversion_data.get('app_version_code')
    # api_ver = conversion_data.get('referrers')[0].get('api_ver')
    sig = conversion_data.get('sig')
    # api_ver_name = conversion_data.get('referrers')[0].get('api_ver_name')
    platformextension = conversion_data.get('platformextension')
    key = conversion_data.get('appsflyerKey')
    buildnumber = appsflyer_data.get('build_number')


    eve  = []
    call_back = {}
    partner = {}



    error = ["app_size","retention","country","api_ver"]

    # reading the data from the file
    with open('support_file/appstext.txt') as f:
        data = f.read()
    
    # print("Data type before reconstruction : ", type(data))
        
    # reconstructing the data as a dictionary
    d = ast.literal_eval(data)
    
    # print("Data type after reconstruction : ", type(d))
    d['package_name'] = package_name
    d['app_version_name'] = conversion_data.get('app_version_name')
    d['app_version_code'] = conversion_data.get('app_version_code')
    d['app_name'] =app_name
    d['supported_os'] = os_ver
    d['link'] = ""
    if conversion_data.get('referrers'):
        try:
            d['api_ver'] =conversion_data.get('referrers')[0].get('api_ver')
            d['api_ver_name'] = conversion_data.get('referrers')[0].get('api_ver_name')
        except:
            pass
    # print conversion_data.get('sig')
    if conversion_data.get('sig'):
        d['sig'] = conversion_data.get('sig')
    else:
        d['sig'] = ''
        # print "he;llo"
        # print type(d.get('sig'))
    d['platformextension'] = conversion_data.get('platformextension')



    d['appsflyer']['key'] = conversion_data.get('appsflyerKey')
    d['appsflyer']['buildnumber'] = appsflyer_data.get('build_number')
    d['appsflyer']['version'] = 'v'+appsflyer_data.get('build_number')[:-2]
    d['appsflyer']['spiKey'] =  Apps_key.get('production_key')
    spykey =  Apps_key.get('dev_key')


    try:
        d['app_size'] =int(app_size)
    except:
        d['app_size'] =random.randint(20,100)





    d2 = {}


    d2['event_name'] = event_name







    b = "campaign_data = "
    conversion = "conversion_data = "
    appsflyer = "Appsflyer_data = "
    launch = "launch_data = "
    inapp = "inapp_data = "
    event_name = "Event_name = "
    event_data = "event_data = "
    with open(txtfile, 'a') as convert_file:
        convert_file.write(b)
        convert_file.write("{")
        convert_file.write("\n")
        li = d.items()
        for st in li:
            if st[0] == "appsflyer":
                # convert_file.write("\n")
                convert_file.write("    'appsflyer' : { \n")
                for k in st[1].items():
             
                    t1 = "      "+"'"+k[0]+"' : '"+k[1]+"',"

                    convert_file.write(t1)
                    convert_file.write("\n")
                    # except:
                    #     traceback.print_exc(file=sys.stdout)
                
                convert_file.write("       #'spiKey' : ")
                s = "'"+spykey+"'"
                convert_file.write(s)
                # convert_file.write("'")
                convert_file.write("\n")
                convert_file.write("    },")
                convert_file.write("\n")
            elif not st[0] in error:
                # try:
                t = "   "+"'"+st[0]+"' : '"+st[1]+"',"

                convert_file.write(t)
                convert_file.write("\n")
                # except:
                #     traceback.print_exc(file=sys.stdout)

            else:
                pass

        for key, value in d.items(): 

            if key in error:
                convert_file.write("    '%s' : %s,\n" % (key, value))

    
    
        convert_file.write("    }")
        convert_file.write("\n")

        # convert_file.write("\n")
        convert_file.write("\n")

        convert_file.write(event_name)
        convert_file.write(json.dumps(d2))
        convert_file.write("\n")
        convert_file.write("\n") 
        


        convert_file.write(conversion)
        convert_file.write(json.dumps(conversion_data))
        convert_file.write("\n")
        convert_file.write("\n") 
        

        # convert_file.write(launch)
        # convert_file.write(json.dumps(dyc_launchs_data))
        # convert_file.write("\n")
        # convert_file.write("\n")


        convert_file.write(inapp)
        convert_file.write(json.dumps(inapp_data))
        convert_file.write("\n")
        convert_file.write("\n")

        convert_file.write(event_data)
        convert_file.write(json.dumps(event_value))
        convert_file.write("\n")
        convert_file.write("\n")
        convert_file.write(appsflyer)
        convert_file.write(json.dumps(appsflyer_data))
        convert_file.write("\n")
        convert_file.write("\n")



    # s = "hello"
    # file_name = s+'.py'
    with open("support_file/apps.txt") as f:
        with open(txtfile, "a") as f1:
            for line in f:
                f1.write(line)




    # mypath1 = 'apps_logs'
    # for f in listdir(mypath1):
    #     path = f
    #     # print f

    # try:
    #     n =  path[:-8]
    #     # print path
    #     # print n
    #     # exit()
    #     # Absolute path of a file
    #     old_name = r"apps_logs\\"+n+".webtest"
    #     new_name = r"apps_logs\\"+n+".xml"


    #     # print old_name
    #     # print new_name

    #     # exit()
    #     # new_name = r"E:\demos\files\reports\new_details.txt"

    #     # Renaming the file
    #     rename(old_name, new_name)


    #     new_path = n+".xml"
    # # print new_path
    # except:
    #     new_path  = path


    # from re import S

    # s = filename
    # file_name = 'myfile/'+filename+'.py'
    # with open(txtfile) as f:
    #     with open(file_name, "w") as f1:
    #         for line in f:
    #             f1.write(line)

    print ("File Created")








