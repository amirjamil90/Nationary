import json
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import time
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment
from openpyxl.styles.borders import Border, Side
import http.client, urllib.request, urllib.parse, urllib.error, base64

wb=Workbook()
dest_filename = 'final_book.xlsx'
ws2 = wb.create_sheet(title="scancode")
df = pd.read_excel('nation.xlsx', sheet_name='Sheet1',sep='\s*,\s*')
latitudes=df['LATITUDE'].tolist()
longitudes=df['LONGITUDE'].tolist()
building_id=df['BUILDING'].tolist()
print(building_id)
for i in range(0,len(latitudes)):
    headers = {
    # Request headers
    'api_key': '4d3592db5746421bbceec98aa299b82f',
    }

    params = urllib.parse.urlencode({
    # Request parameters
    'lat': latitudes[i],
    'long': longitudes[i],
    'language': 'A',
    'format': 'json',
    'encode': 'utf8',
    })
    
    try:
        conn = http.client.HTTPSConnection('apina.address.gov.sa')
        conn.request("GET", "/NationalAddress/v3.1/Address/address-geocode?%s" % params, "{body}", headers)
        response = conn.getresponse()
        print(response)
        data = response.read()
        json_data=json.loads(data)
        new_national_address= json_data['Addresses'][0]['PKAddressID']    #TO GET THE NATIONAL ADDRESS COMPLETE CODE WHICH INCLUDES POSTAL CODE, BULDING CODE AND ADDITIONAL CODE. 
        print(new_national_address)
        #cellname_text='B'+str(i+1)
        #building_id_cell='A'+str(i+1)
        #ws2[cellname_text]=new_national_address
        print("hii")
        #ws2[building_id_cell]=building_id[i]
        conn.close()  
        time.sleep(6)              #CLOSE THE CONNECTION. WE NEED TO CLOSE THE CONNECTION EVERYTIME. SO FOR MULTIPLE REQUEST MULTIPLE CONNECTIONS NEEDED AS THREAD. 
    except Exception as e:
        print("Not Applicable")
        time.sleep(6)
	   
wb.save(filename = dest_filename)





