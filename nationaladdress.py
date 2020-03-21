import httplib, urllib, base64
import json
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import time
df = pd.read_excel('nation.xlsx', sheet_name='Sheet1',sep='\s*,\s*')
latitudes=df['LATITUDE'].tolist()
longitudes=df['LONGITUDE'].tolist()
for i in range(0,len(latitudes)):

    headers = {
        # Request headers
        'api_key': 'primary key',
    }

    params = urllib.urlencode({
        # Request parameters
        'lat': latitudes[i],
        'long': longitudes[i],
        'language': 'A',
        'format': 'json',
        'encode': 'utf8',   #THIS IS VERY IMPORTANT BECAUSE SOME SYMBOLOGY NOT DEFINED IN LANGAUGE SET. 
    })

    try:
        conn = httplib.HTTPSConnection('apina.address.gov.sa')
        #REQUEST PARAMETERS
        conn.request("GET", "/NationalAddress/v3.1/Address/address-geocode?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        json_data=json.loads(data)
        print(json_data['Addresses'][0]['PKAddressID'])     #TO GET THE NATIONAL ADDRESS COMPLETE CODE WHICH INCLUDES POSTAL CODE, BULDING CODE AND ADDITIONAL CODE. 
        conn.close()  
        time.sleep(6)              #CLOSE THE CONNECTION. WE NEED TO CLOSE THE CONNECTION EVERYTIME. SO FOR MULTIPLE REQUEST MULTIPLE CONNECTIONS NEEDED AS THREAD. 
    except Exception as e:
        print("Not Applicable")
	time.sleep(6)




