#-*- coding: utf-8 -*-
# created by him@nshu
import sys
if int(sys.version_info.major) == 2:
    py_version = 2
else:
    py_version = 3
    import urllib.parse as urlparse
from datetime import datetime,timedelta
from sdk import installtimenew, util
from hashlib import sha1
import time, random, json, string, urllib, uuid, hashlib
false = False
true = True
null = None


campaign_data = {
   'package_name' : 'com.footlocker.mena',
   'app_name' : 'footlocker',
   'app_version_name' : '1.22.56',
   'app_version_code' : '8000270',
   'supported_os' : '7',
   'supported_countries' : 'WW',
   'link' : '',
   'tracker' : ['adjust'],
   'app_size' : 22,
   'adjust' : {'sdk': 'react-native4.33.0@android4.33.2', 'app_token': 'pwj5et4km77k', 'app_secret': '181920364235870017351318908670710663'},
   'country' : [('USA', 50), ('India', 3), ('Malaysia', 4), ('Indonesia', 1), ('Thailand', 2), ('Egypt', 1), ('Russia', 6), ('USA', 10), ('SaudiArabia', 1), ('SouthAfrica', 1), ('Israel', 2), ('Kenya', 1), ('Nigeria', 1), ('Pakistan', 2), ('Qatar', 1), ('Brazil', 3), ('Mexico', 4), ('Canada', 5), ('UK', 30), ('HongKong', 5), ('Spain', 4), ('France', 4), ('Australia', 5)],
   'retention' : {1: 85, 2: 82, 3: 78, 4: 75, 5: 70, 6: 66, 7: 62, 8: 58, 9: 55, 10: 50, 11: 48, 12: 45, 13: 40, 14: 39, 15: 38, 16: 37, 17: 35, 18: 35, 19: 34, 20: 33, 21: 32, 22: 31, 23: 30, 24: 29, 25: 29, 26: 28, 27: 27, 28: 26, 29: 25, 30: 25, 31: 24, 32: 23, 33: 23, 34: 22, 35: 22, 36: 21, 37: 20, 38: 19, 39: 19, 40: 18, 41: 16, 42: 16, 43: 16, 44: 15, 45: 15, 46: 14, 47: 13, 48: 13, 49: 12, 50: 11, 51: 11, 52: 10, 53: 9, 54: 9, 55: 8, 56: 7, 57: 6, 58: 5, 59: 4, 60: 3},
	}
firebase_data = {"url": "/v1/projects/fl-store-ad11e/installations", "x-firebase-client": "3", "X-Android-Cert": "0A2CFED36EFCFE046499AB5EF4501B4C984A73DB", "x-goog-api-key": "AIzaSyCyS9Funm6MGke3h1kUtUvtKkmNdjJEcJU", "data": {"fid": "ebhZD-5QQsu7j85jrogHV0", "appId": "1:162437311554:android:2dd04f9efc6a5e2a3891db", "authVersion": "FIS_v2", "sdkVersion": "a:17.0.0"}}

adjust_data = {"url": "s2s.adjust.com", "sdkclient": "react-native4.33.0@android4.33.2", "auth_algo": "adj3", "Content": "application/x-www-form-urlencoded", "initiated_by": "backend"}

session_data = {"updated_at": "2023-04-17T06%3A55%3A58.634Z-0500", "device_type": "tablet", "device_manufacturer": "OnePlus", "gps_adid": "8e73a294-c140-429b-b271-681ec5545083", "environment": "production", "session_count": "1", "android_uuid": "630ac3da-ea16-470f-92e1-09ccb4aaf2d3", "attribution_deeplink": "1", "connectivity_type": "1", "os_build": "N2G48H", "api_level": "25", "needs_response_details": "1", "push_token": "ebhZD-5QQsu7j85jrogHV0%3AAPA91bEBeOBszb0T2MRtdXd93JcAwirUVDqH05t2j8hUMOoFhDnq0tFFg_8GaMtCXDtfTDwGCEyTQB7d9DZDBP0irVeCXN0BcUh_nVic16CQj-d2rgJvwj-M6yQXK5ynCbpdFdxFHlyL", "event_buffering_enabled": "0", "mcc": "404", "app_secret": "181920364235870017351318908670710663", "os_name": "android", "display_width": "720", "screen_format": "long", "screen_density": "high", "hardware_name": "OnePlus-user+7.1.2+20171130.276299+release-keys", "tracking_enabled": "1", "gps_adid_src": "service", "package_name": "com.footlocker.mena", "mnc": "34", "installed_at": "2023-04-17T06%3A55%3A58.634Z-0500", "app_version": "1.22.56", "country": "US", "gps_adid_attempt": "1", "screen_size": "large", "app_token": "pwj5et4km77k", "ui_mode": "1", "device_name": "A5010", "display_height": "1280", "created_at": "2023-04-17T06%3A56%3A58.681Z-0500", "language": "en", "os_version": "7.1.2", "cpu_type": "x86_64", "sent_at": "2023-04-17T06%3A56%3A58.769Z-0500"}

sdk_click_data = {"google_play_instant": "0", "device_type": "tablet", "source": "install_referrer", "referrer": "adjust_reftag%3DcK3l0bNN1iBOG%26utm_source%3DAffiliate%2BNetworks%26utm_campaign%3Dplatformance%26utm_content%3D23%26utm_term%3D19_4_%257Bsource%257D", "click_time": "2023-04-17T06%3A55%3A12.000Z-0500", "device_manufacturer": "OnePlus", "gps_adid": "8e73a294-c140-429b-b271-681ec5545083", "environment": "production", "time_spent": "0", "android_uuid": "630ac3da-ea16-470f-92e1-09ccb4aaf2d3", "connectivity_type": "1", "os_build": "N2G48H", "needs_response_details": "1", "mcc": "404", "event_buffering_enabled": "0", "click_time_server": "2023-04-17T06%3A55%3A12.000Z-0500", "app_secret": "181920364235870017351318908670710663", "install_begin_time": "2023-04-17T06%3A55%3A18.000Z-0500", "os_name": "android", "display_width": "720", "gps_adid_src": "service", "tracking_enabled": "1", "mnc": "34", "installed_at": "2023-04-17T06%3A55%3A58.634Z-0500", "gps_adid_attempt": "1", "screen_size": "large", "language": "en", "install_version": "1.22.56", "cpu_type": "x86_64", "updated_at": "2023-04-17T06%3A55%3A58.634Z-0500", "install_begin_time_server": "2023-04-17T06%3A55%3A18.000Z-0500", "session_count": "1", "referrer_api": "google", "attribution_deeplink": "1", "api_level": "25", "push_token": "ebhZD-5QQsu7j85jrogHV0%3AAPA91bEBeOBszb0T2MRtdXd93JcAwirUVDqH05t2j8hUMOoFhDnq0tFFg_8GaMtCXDtfTDwGCEyTQB7d9DZDBP0irVeCXN0BcUh_nVic16CQj-d2rgJvwj-M6yQXK5ynCbpdFdxFHlyL", "screen_format": "long", "subsession_count": "1", "screen_density": "high", "hardware_name": "OnePlus-user+7.1.2+20171130.276299+release-keys", "session_length": "0", "package_name": "com.footlocker.mena", "app_version": "1.22.56", "country": "US", "app_token": "pwj5et4km77k", "device_name": "A5010", "ui_mode": "1", "created_at": "2023-04-17T06%3A56%3A58.889Z-0500", "display_height": "1280", "os_version": "7.1.2", "sent_at": "2023-04-17T06%3A56%3A58.924Z-0500"}

atribution_data = {"device_type": "tablet", "gps_adid": "8e73a294-c140-429b-b271-681ec5545083", "environment": "production", "android_uuid": "630ac3da-ea16-470f-92e1-09ccb4aaf2d3", "attribution_deeplink": "1", "needs_response_details": "1", "api_level": "25", "push_token": "ebhZD-5QQsu7j85jrogHV0%3AAPA91bEBeOBszb0T2MRtdXd93JcAwirUVDqH05t2j8hUMOoFhDnq0tFFg_8GaMtCXDtfTDwGCEyTQB7d9DZDBP0irVeCXN0BcUh_nVic16CQj-d2rgJvwj-M6yQXK5ynCbpdFdxFHlyL", "event_buffering_enabled": "0", "app_secret": "181920364235870017351318908670710663", "os_name": "android", "tracking_enabled": "1", "gps_adid_src": "service", "package_name": "com.footlocker.mena", "initiated_by": "backend", "app_version": "1.22.56", "gps_adid_attempt": "1", "app_token": "pwj5et4km77k", "ui_mode": "1", "device_name": "A5010", "created_at": "2023-04-17T06%3A57%3A02.607Z-0500", "os_version": "7.1.2", "sent_at": "2023-04-17T06%3A57%3A02.658Z-0500"}

event_data = []

events_details = []




def install(app_data, device_data):
	# print "Please wait installing..."
	installtimenew.main(app_data,device_data,app_size=campaign_data.get('app_size'),os='android')

	if not app_data.get('sec'):
		timez=device_data.get('timezone')    
		sec = (abs(int(timez))/100)*3600+(abs(int(timez))%100)*60
		if int(timez) < 0:
			sec = (-1) * sec
		app_data['sec'] = sec
	# user = util.register_user(country=device_data.get('locale').get('country'))
	# req = locationData.getLocation(device_data.get('locale').get('country'))

	if session_data.get('push_token'):
		pushtoken_session(app_data)


	if not app_data.get('android_uuid'):
		app_data['android_uuid']=str(uuid.uuid4())
	app_data['fid']=random.choice(['c','d','e','f'])+''.join(random.choice(string.digits + string.ascii_letters + '-_') for _ in range(21))
	num = 5
	while(num >0):
		req = firebase_installations(app_data,device_data)
		res= util.execute_request(**req)
		try:
			tmp = json.loads(res.get('data'))
			app_data['fid2'] = tmp.get('fid')
			break
		except:
			pass
		num -= 1
	if not app_data.get('fid2'):
		raise Exception ("Erorr in Firebase call  for country"+device_data.get('locale').get('country'))
		return {'status':False}


	# print 'Session'
	req = adjust_session(app_data, device_data)
	util.execute_request(**req)


	# print 'Sdk_click'
	req = adjust_sdk_click( app_data, device_data)
	util.execute_request(**req)
	time.sleep(random.randint(1,5))



	if adjust_data.get('sdk_info'):
		req = adjust_sdk_info(app_data,device_data)
		util.execute_request(**req)



	# print 'Attribution'
	req = adjust_attribution(app_data, device_data)
	util.execute_request(**req)



# ==========================================================================
#  for manually  update comment whole for loop
# ===========================================================================
	for i in events_details:
		event_token = i.get('event')
		callback = i.get('callback')
		if callback:
			callback1 = json.loads(callback)
		else:
			callback1 = {}
		patner = i.get('patner')
		if patner:
			patner1 = json.loads(patner)
		else:
			patner1 = {}
		req = adjust_events(app_data,device_data,event_token=event_token,callback=callback1,patner=patner1)
		util.execute_request(**req)
		time.sleep(random.randint(1,5))



# ===========================================================================================
# ===========================================================================================

#  For update in events pls write from her....................................................

	# req = adjust_events(app_data,device_data,event_token='',)
	# util.execute_request(**req)
	# time.sleep(random.randint(1,5))




	return {'status':True}
#============================================================================================================================
def open(app_data, device_data, day =1):
	

	if app_data.get('times'):
		# print 'Session'
		req = adjust_session(app_data, device_data)
		util.execute_request(**req)


	return {'status':True}

#==================================================================================================================================================================================





def firebase_installations( app_data, device_data ):
	method = "post"
	url = 'https://firebaseinstallations.googleapis.com'+firebase_data.get('url')

	headers = {
		'Content-Type':"application/json",
		'Accept':"application/json",
		'Cache-Control':"no-cache",
		'X-Android-Package':campaign_data.get('package_name'),
		'x-firebase-client':firebase_data.get('x-firebase-client'),
		'X-Android-Cert':firebase_data.get('X-Android-Cert'),
		'x-goog-api-key':firebase_data.get('x-goog-api-key'),
		'User-Agent':get_ua(device_data),
		'Connection':"Keep-Alive",
		'Accept-Encoding':"gzip"
	}

	data ={
		"fid": app_data.get('fid'),
		"appId":firebase_data.get('data').get('appId') ,
		"authVersion": firebase_data.get('data').get('authVersion'),
		"sdkVersion": firebase_data.get('data').get('sdkVersion')
	}
	
	return {'url': url, 'httpmethod': method, 'headers': headers, 'params': None, 'data': json.dumps(data)}





def adjust_session( app_data, device_data):

	url='https://'+adjust_data.get('url')+'/session'
	
	httpmethod='post'

	app_data['session_started']=int(time.time())

	if not app_data.get('session_count'):
		app_data['session_count'] = 1
	else:
		app_data['session_count'] +=1
	
	headers={
			'Client-SDK':campaign_data.get('adjust').get('sdk'),
			'Content-Type':'application/x-www-form-urlencoded',
			'User-Agent': get_ua(device_data),
			'Accept-Encoding':'gzip'
	}

	params={}

	data={
		'android_uuid':app_data.get('android_uuid'),
		'api_level':device_data.get('sdk'),
		'app_token':campaign_data.get('adjust').get('app_token'),
		'app_version':campaign_data.get('app_version_name'),
		'attribution_deeplink':1,
		'connectivity_type':1,
		'country':device_data.get('locale').get('country'),
		'cpu_type':device_data.get('cpu'),
		'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
		'device_manufacturer':device_data.get('manufacturer'),
		'device_name':device_data.get('model'),
		'device_type':device_data.get('device_type'),
		'display_height':device_data.get('resolution').split('x')[-2],
		'display_width':device_data.get('resolution').split('x')[-1],
		'environment':'production',
		'event_buffering_enabled':0,
		# 'fb_id':app_data.get('fb_id'),
		'gps_adid':device_data.get('adid'),
		'gps_adid_src':'service',
		"gps_adid_attempt": 1,
		'hardware_name':device_data.get('hardware'),
		'installed_at':datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
		'language':device_data.get('locale').get('language'),
		'needs_response_details':1,
		'network_type':0,
		'os_build':device_data.get('build'),
		'os_name':'android',
		'os_version':device_data.get('os_version'),
		'package_name':campaign_data.get('package_name'),
		'screen_density':get_screen_density(device_data),
		'screen_format':get_screen_format(device_data),
		'screen_size':'normal',
		'sent_at':(datetime.utcfromtimestamp(time.time() +random.randint(15,25)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
		'session_count':app_data.get('session_count'),
		'tracking_enabled':1,
		'updated_at':datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
		# "vm_isa":device_data.get('cpu')[:-4]
	}

	if session_data.get('vm_isa'):
		data['vm_isa'] = device_data.get('cpu')[:-4]
	if session_data.get('app_secret'):
		data['app_secret'] = session_data.get('app_secret')
	
	if session_data.get('ui_mode'):
		data['ui_mode'] = 1
	if session_data.get('fb_id'):
		data['fb_id'] = app_data.get('fb_id')



	if app_data.get('pushtoken'):
		data['push_token'] = app_data.get('pushtoken')
	app_data['subsession']=1
	if campaign_data.get('adjust').get('app_secret'):
		headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'session')

	return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}

#====================================================================================

def adjust_sdk_click(app_data,device_data):

	url='https://'+adjust_data.get('url')+'/sdk_click'
	httpmethod='post'
	app_data['session_started']=int(time.time())
	headers={
			'Client-SDK': campaign_data.get('adjust').get('sdk'),
			'Content-Type':'application/x-www-form-urlencoded',
			'User-Agent': get_ua(device_data),
		'Accept-Encoding':'gzip',

	}

	params={}

	
	data={
			'android_uuid':app_data.get('android_uuid'),
			'api_level':device_data.get('sdk'),
			'app_token':campaign_data.get('adjust').get('app_token'),
			'app_version':campaign_data.get('app_version_name'),
			'attribution_deeplink':1,
			'connectivity_type':1,
			# 'click_time':        datetime.utcfromtimestamp(app_data.get('times').get('click_time')+app_data.get('sec')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone'),
			# "click_time_server": datetime.utcfromtimestamp(app_data.get('times').get('click_time')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone'),
			'country':device_data.get('locale').get('country'),
			'cpu_type':device_data.get('cpu'),
			'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
			'device_manufacturer':device_data.get('manufacturer'),
			'device_name':device_data.get('model'),
			'device_type':device_data.get('device_type'),
			'display_height':device_data.get('resolution').split('x')[-2],
			'display_width':device_data.get('resolution').split('x')[-1],
			'environment':'production',
			'event_buffering_enabled':0,
			'google_play_instant':0,
			'gps_adid_attempt':1,
			# 'fb_id':app_data.get('fb_id'),
			'gps_adid':device_data.get('adid'),
			'gps_adid_src':'service',
			'hardware_name':device_data.get('hardware'),
			'installed_at':datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone'),
			# "install_begin_time":datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),
			# "install_begin_time_server":	datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),
			# 'install_version':campaign_data.get('app_version_name'),
			'language':device_data.get('locale').get('language'),
			'needs_response_details':1,
			'network_type':0,
			'os_build':device_data.get('build'),
			'os_name':'android',
			'os_version':device_data.get('os_version'),
			'package_name':campaign_data.get('package_name'),
			'referrer':app_data.get('referrer') or 'utm_source=(not%20set)&utm_medium=(not%20set)',
			# 'referrer_api':'google',
			'screen_density':get_screen_density(device_data),
			'screen_format':get_screen_format(device_data),
			'screen_size':'normal',
			'sent_at':(datetime.utcfromtimestamp(time.time() +random.randint(15,25)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
			'session_count':app_data.get('session_count'),
			'session_length':int(time.time())- app_data.get('session_started'),
			'source':'install_referrer',
			'subsession_count':subsession(app_data),
			'time_spent':time_spent(app_data),
			'tracking_enabled':1,
			'updated_at': datetime.utcfromtimestamp(app_data.get('times').get('install_complete_time')+app_data.get('sec')).isoformat()[:-3]+'Z'+device_data.get('timezone') or None,
			# "vm_isa":device_data.get('cpu')[:-4]
	}

	if sdk_click_data.get('vm_isa'):
		data['vm_isa'] = device_data.get('cpu')[:-4]
	if sdk_click_data.get('app_secret'):
		data['app_secret'] = sdk_click_data.get('app_secret')
	
	if sdk_click_data.get('ui_mode'):
		data['ui_mode'] = 1
	if sdk_click_data.get('install_version'):
		data['install_version'] = sdk_click_data.get('install_version')



	if sdk_click_data.get('click_time'):
		data['click_time'] = datetime.utcfromtimestamp(app_data.get('times').get('click_time')+app_data.get('sec')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone')

	if sdk_click_data.get('click_time_server'):
		data['click_time_server'] = datetime.utcfromtimestamp(app_data.get('times').get('click_time')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+'Z'+device_data.get('timezone')

	if sdk_click_data.get('install_begin_time'):
		data['install_begin_time'] = datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone')
	if sdk_click_data.get('install_begin_time_server'):
		data['install_begin_time_server'] =datetime.utcfromtimestamp(app_data.get('times').get('download_begin_time')+app_data.get('sec')+app_data.get('sec')).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'+device_data.get('timezone'),

			
	if sdk_click_data.get('fb_id'):
		data['fb_id'] = app_data.get('fb_id')

	if sdk_click_data.get('install_version'):
		data['install_version'] = sdk_click_data.get('install_version')

	if sdk_click_data.get('install_version'):
		data['install_version'] = sdk_click_data.get('install_version')

	if sdk_click_data.get('referrer_api'):
		data['referrer_api'] = sdk_click_data.get('referrer_api')

	if app_data.get('pushtoken'):
		data['push_token'] = app_data.get('pushtoken')
	if campaign_data.get('adjust').get('app_secret'):
		headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),data.get('source'),campaign_data.get('adjust').get('app_secret'), 'click')

	# data['click_time_server'] = datetime.utcfromtimestamp(int(app_data.get('times').get('click_time')) +  timedelta(seconds= random.randint(1,6))).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'+device_data.get('timezone')
	# data['install_begin_time_server'] = datetime.utcfromtimestamp((app_data.get('times').get('download_begin_time')+app_data.get('sec')) + timedelta(seconds= random.randint(1,6))).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'+device_data.get('timezone')
	return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}

#==================================================================================

def adjust_attribution(app_data,device_data,initiated_by=None):

	url='https://'+adjust_data.get('url')+'/attribution'

	httpmethod='get'

	headers={
		'Client-SDK':campaign_data.get('adjust').get('sdk'),
		'User-Agent':get_ua(device_data),
		'Accept-Encoding':'gzip',
	}

	params={
			'android_uuid':app_data.get('android_uuid'),
			'api_level':device_data.get('sdk'),
			'app_token':campaign_data.get('adjust').get('app_token'),
			'app_version':campaign_data.get('app_version_name'),
			# 'app_secret':campaign_data.get('adjust').get('app_secret'),
			'attribution_deeplink':1,
			'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
			'device_name':device_data.get('model'),
			'device_type':device_data.get('device_type'),
			'environment':'production',
			'event_buffering_enabled':0,
			'gps_adid':device_data.get('adid'),
			'gps_adid_src':'service',     
			'gps_adid_attempt':1,
			# 'fb_id':app_data.get('fb_id'),
			'initiated_by':initiated_by,
			'needs_response_details':1,
			'os_name':'android',
			'os_version':device_data.get('os_version'),
			'package_name':campaign_data.get('package_name'),
			'tracking_enabled':1,
			# 'secret_id':'2',
			'sent_at':(datetime.utcfromtimestamp(time.time() +random.randint(15,25)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
			# 'session_count':app_data.get('session_count'),
	}

	if atribution_data.get('app_secret'):
		params['app_secret'] = atribution_data.get('app_secret')
	if atribution_data.get('secret_id'):
		params['secret_id'] = atribution_data.get('secret_id')
	if atribution_data.get('initiated_by'):
		params['initiated_by'] = atribution_data.get('initiated_by')
	if atribution_data.get('ui_mode'):
		params['ui_mode'] = 1
	if app_data.get('pushtoken'):
		params['push_token'] = app_data.get('pushtoken')



	data=None
	if campaign_data.get('adjust').get('app_secret'):
		headers['Authorization'] = get_auth(params.get('created_at'),params.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'attribution')
	return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}


#====================================================================================
def adjust_sdk_info(app_data,device_data):

	url='https://'+adjust_data.get('url')+'/sdk_info'

	httpmethod='post'
	pushtoken(app_data)
	headers={
		'Client-SDK':campaign_data.get('adjust').get('sdk'),
		'User-Agent':get_ua(device_data),
		'Accept-Encoding':'gzip',
	}

	data={
			# 'android_uuid':app_data.get('android_uuid'),
			'app_token':campaign_data.get('adjust').get('app_token'),
			'attribution_deeplink':1,
			'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
			'environment':'production',
			'event_buffering_enabled':0,
			'gps_adid':device_data.get('adid'),
			# 'gps_adid_src':'service',  
			# 'gps_xadid_attempt':1,
			'needs_response_details':1,
			"push_token":app_data.get('pushtoken'),
			"source":"push",
			'tracking_enabled':1,
			'sent_at':(datetime.utcfromtimestamp(time.time() +app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
	}
	if adjust_data.get('sdk_info'):
		if sdk_info_data.get('android_uuid'):
			data['android_uuid'] = app_data.get('android_uuid')
		if sdk_info_data.get('gps_adid_attempt'):
			data['gps_adid_attempt'] = sdk_info_data.get('gps_adid_attempt')
		if sdk_info_data.get('gps_xadid_attempt'):
			data['gps_xadid_attempt'] = sdk_info_data.get('gps_xadid_attempt')





	params=None
	if campaign_data.get('adjust').get('app_secret'):
		headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'info')
	
	return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}





#========================================================================================================================================================================


def adjust_events(app_data,device_data,event_token=None,callback = None,patner= None):

	url='https://'+adjust_data.get('url')+'/event'

	httpmethod='post'

	headers={
			'Client-SDK':campaign_data.get('adjust').get('sdk'),
			'User-Agent':get_ua(device_data),
			'Content-Type': 'application/x-www-form-urlencoded',
			'Accept-Encoding':'gzip',    
	}

	params=None

	
	if not app_data.get('event_count'):
		app_data['event_count']=1
	else:
		app_data['event_count']=app_data['event_count']+1

	# print(app_data)

	data={
		'android_uuid':app_data.get('android_uuid'),
		'api_level':device_data.get('sdk'),
		'app_token':campaign_data.get('adjust').get('app_token'),
		'app_version':campaign_data.get('app_version_name'),
		'attribution_deeplink':1,
		'connectivity_type':1,
		'country':device_data.get('locale').get('country'),
		'cpu_type':device_data.get('cpu'),
		# 'callback_params':json.dumps(callback),
		'created_at':(datetime.utcfromtimestamp(time.time()+random.randint(4,10)+app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
		'device_manufacturer':device_data.get('manufacturer'),
		'device_name':device_data.get('model'),
		'device_type':device_data.get('device_type'),
		'display_height':device_data.get('resolution').split('x')[-2],
		'display_width':device_data.get('resolution').split('x')[-1],
		'environment':'production',
		'event_buffering_enabled':0,
		'event_count':app_data.get('event_count'),
		'event_token':event_token,
		'gps_adid':device_data.get('adid'),
		'gps_adid_attempt':'1',
		'gps_adid_src':'service',
		# 'fb_id':app_data.get('fb_id'),
		'hardware_name':device_data.get('hardware'),
		'language':device_data.get('locale').get('language'),
		'needs_response_details':1,
		'network_type':0,
		'os_build':device_data.get('build'),
		'os_name':'android',
		'os_version':device_data.get('os_version'),
		'package_name':campaign_data.get('package_name'),
		'partner_params' : patner,
		# 'push_token' : push_token,
		# "partner_params":partner_params,
		'screen_density':get_screen_density(device_data),
		'screen_format':get_screen_format(device_data),
		'session_count':app_data.get('session_count'),
		'session_length':int(time.time())-app_data.get('session_started'),
		'screen_size':'normal',
		'subsession_count':subsession(app_data),
		'sent_at':(datetime.utcfromtimestamp(time.time() +app_data.get('sec'))).isoformat()[:-3]+'Z'+device_data.get('timezone'),
		'time_spent':time_spent(app_data),
		'tracking_enabled':1,
		#  "vm_isa":device_data.get('cpu')[:-4]

	}


	if event_data.get('vm_isa'):
		data['vm_isa'] = device_data.get('cpu')[:-4]
	if event_data.get('app_secret'):
		data['app_secret'] = event_data.get('app_secret')
	
	if event_data.get('ui_mode'):
		data['ui_mode'] = 1
	if event_data.get('fb_id'):
		data['fb_id'] = app_data.get('fb_id')


	if app_data.get('pushtoken'):
		data['push_token'] = app_data.get('pushtoken')

	if callback:
		data['callback_params'] = json.dumps(callback)
	if patner:
		data['partner_params'] = json.dumps(patner)

	if campaign_data.get('adjust').get('app_secret'):
		headers['Authorization'] = get_auth(data.get('created_at'),data.get('gps_adid'),campaign_data.get('adjust').get('app_secret'), 'event')
	return {'url':url, 'httpmethod':httpmethod, 'headers':headers, 'params':params, 'data':data}


#============================================================================================

def get_auth(created_at,activity_kind, app_secret,gps_adid , source =''):
	string = created_at+activity_kind+source+app_secret+gps_adid
	sign = hashlib.sha256(string).hexdigest()
	if source:
		return 'Signature secret_id="{0}",signature="{1}",algorithm="sha256",headers="created_at gps_adid source app_secret activity_kind"'.format(campaign_data.get('adjust').get('secret_id'),sign)
	return 'Signature secret_id="{0}",signature="{1}",algorithm="sha256",headers="created_at gps_adid app_secret activity_kind"'.format(campaign_data.get('adjust').get('secret_id'),sign)



def time_spent(app_data):
	if not app_data.get('time_spent'):
		app_data['time_spent'] = str(0)
	else:
		app_data['time_spent'] = int(app_data.get('time_spent')) + (int(time.time()) - app_data.get('session_started'))

	return app_data.get('time_spent')

def subsession(app_data):
	possibility = [True]*30+[False]*70
	random.shuffle(possibility)
	if random.choice(possibility):
		if not app_data.get('subsession'):
			app_data['subsession']=1
		else:
			app_data['subsession']+=1
	return app_data.get('subsession')

def get_screen_density(device_data):
	dpi = int(device_data.get('dpi'))
	if dpi >= 320:
		return 'high'
	elif dpi >= 180:
		return 'medium'
	else:
		return 'low'
		
def get_screen_format(device_data):
	resolution = device_data.get('resolution')
	b = resolution.split('x')
	c = float(b[1])/float(b[0])
	if c >= 1.77:
		return 'long'
	else:
		return 'normal'

def pushtoken(app_data):
	if not app_data.get('pushtoken'):
		if sdk_info_data.get('push_token'):
			initial = sdk_info_data.get('push_token')
			if "APA91b" in initial:
				length = len(initial.split('APA91b')[1])
				if app_data.get('fid2'):
					app_data['pushtoken'] = app_data.get('fid2')+ ':APA91b' + ''.join(random.choice(string.digits + string.ascii_letters + '-_') for _ in range(length))
				else:
					app_data['pushtoken'] = app_data.get('fid')+ ':APA91b' + ''.join(random.choice(string.digits + string.ascii_letters + '-_') for _ in range(length))
			else:
				length = len(initial)
				app_data['pushtoken'] = ''.join(random.choice(string.digits + string.ascii_letters + '-_') for _ in range(length))
		else:
			pass
def pushtoken_session(app_data):
	if not app_data.get('pushtoken'):
		if session_data.get('push_token'):
			initial = session_data.get('push_token')
			if "APA91b" in initial:
				length = len(initial.split('APA91b')[1])
				if app_data.get('fid2'):
					app_data['pushtoken'] = app_data.get('fid2')+ ':APA91b' + ''.join(random.choice(string.digits + string.ascii_letters + '-_') for _ in range(length))
				else:
					app_data['pushtoken'] = app_data.get('fid')+ ':APA91b' + ''.join(random.choice(string.digits + string.ascii_letters + '-_') for _ in range(length))
			else:
				length = len(initial)
				app_data['pushtoken'] = ''.join(random.choice(string.digits + string.ascii_letters + '-_') for _ in range(length))
		else:
			pass


def get_country():
	weighted_choices = campaign_data['country'] if campaign_data.get('country') else ('USA', 4)
	country_list = [val for val, cnt in weighted_choices for i in range(cnt)]
	return random.choice(country_list)

def get_retention(day):
	return campaign_data['retention'][day] if campaign_data['retention'].get(day) else 0


def get_ua(device_data):
    if int(device_data.get("sdk")) >=19:
        return 'Dalvik/2.1.0 (Linux; U; Android '+device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+device_data.get('build')+')'
    else:
        return 'Dalvik/1.6.0 (Linux; U; Android '+device_data.get('os_version')+'; '+device_data.get('model')+' Build/'+device_data.get('build')+')'






#######################################################################################



	