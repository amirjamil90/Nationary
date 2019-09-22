import httplib, urllib, base64
import json

headers = {
    # Request headers
    'api_key': 'PRIMARY API KEY',
}

params = urllib.urlencode({
    # Request parameters
    'lat': 'LATITUDE',
    'long': 'LONGITUDE',
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
    conn.close().    #CLOSE THE CONNECTION. WE NEED TO CLOSE THE CONNECTION EVERYTIME. SO FOR MULTIPLE REQUEST MULTIPLE CONNECTIONS NEEDED AS THREAD. 
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))



