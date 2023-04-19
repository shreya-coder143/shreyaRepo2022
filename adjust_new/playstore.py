from google_play_scraper import app
import json
# import adjust_new
# import new

# # p = new.package
# print ("hello")
# print(p)

# with open('playstore_support/pac.txt','r') as  file:
#     p = file.read()
#     # print(p)



result = app(
    "com.shopee.ph"

    # lang='en', # defaults to 'en'
    # country=da.get(i), # defaults to 'us'
)

print(result.get('title'))
exit()
n = 'true'
m = 'false'
o = 'null'
with open('help.py','w') as file:
    file.write(n+" = True\n")
    file.write(m+" = False\n")
    file.write(o+" = None\n")
    file.write("data = { ")
    file.write("'"+p+"':")
    file.write(json.dumps(result))
    file.write("}")
# print (result)