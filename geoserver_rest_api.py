import requests

# create data store
for x in range(80):
    url = 'http://localhost:8080/geoserver/rest/workspaces/tasmania/coveragestores'
    xml_file_path = 'pyramid1.xml'
    xml_data = '<coverageStore><workspace>tasmania</workspace><name>pyramid' + str(x) + '</name><type>ImagePyramid</type><enabled>true</enabled><url>file:data/tasmania/dir' + str(x) + '</url></coverageStore>'
    username = 'admin'
    password = 'geoserver'

    headers = {'Content-type': 'text/xml'}
    data = open(xml_file_path, 'rb').read()

    response = requests.post(url, auth=(username, password), headers=headers, data=xml_data)
    print(response.text)

# create layer
for x in range(80):
    url = 'http://localhost:8080/geoserver/rest/workspaces/tasmania/coveragestores/pyramid' + str(x) + '/coverages'
    xml_data = '<coverage><nativeName>pyramid' + str(x) + '</nativeName><title>pyramid' + str(x) + '</title><name>pyramid' + str(x) + '</name><srs>EPSG:404000</srs></coverage>'
    username = 'admin'
    password = 'geoserver'

    headers = {'Content-type': 'text/xml'}
    response = requests.post(url, auth=(username, password), headers=headers, data=xml_data)
    print(response.text)

# create layer group
url = 'http://localhost:8080/geoserver/rest/layergroups'
xml_data = '<layerGroup><name>pyramidGroup</name><title>pyramidGroup</title><workspace><name>tasmania</name></workspace><layers>'
for x in range(77):
    xml_data = xml_data + '<layer>pyramid' + str(x) + '</layer>'
xml_data = xml_data + '</layers></layerGroup>'

headers = {'Content-type': 'text/xml'}
username = 'admin'
password = 'geoserver'

response = requests.post(url, auth=(username, password), headers=headers, data=xml_data)
print(response.text)