import urllib.request, urllib.parse, urllib.error
import json
import ssl

#address = 'Belorussian State University'

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    parms['key'] = 42
    #if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
    #exit()
            #print(data)
            continue

#print(json.dumps(js, indent=4))

    placeid = js['results'][0]['place_id']

    print('Place id ', placeid)
