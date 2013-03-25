import urllib
import xmltodict
import json

xmlurl = 'http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML'
xml = urllib.urlopen(xmlurl)
stations = xmltodict.parse(xml)['ArrayOfObjStation']['objStation']