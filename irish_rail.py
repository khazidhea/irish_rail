from flask import Flask
from flask import render_template
from flask import send_file
import urllib
import xmltodict
import json

app = Flask(__name__)

@app.route('/static/<filename>')
def serve_static(filename):
	return send_file('static/' + filename)

@app.route('/<station_code>')
def station(station_code):
	xmlurl = 'http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML?StationCode=' + station_code
	xml = urllib.urlopen(xmlurl)
	station = xmltodict.parse(xml)
	result = {'error':0}
	try:
		result['station_info'] = station['ArrayOfObjStationData']['objStationData']
	except KeyError:
		result['error'] ='Could not retrive station info for ' + station_code
	return json.dumps(result)

@app.route('/')
def index():
	xmlurl = 'http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML'
	xml = urllib.urlopen(xmlurl)
	stations = json.dumps(xmltodict.parse(xml)['ArrayOfObjStation']['objStation'])
	return render_template('irish_rail.html', stations=stations)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')