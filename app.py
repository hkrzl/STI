#!flask/bin/python

from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
from flask import make_response

import requests, json

auth = HTTPBasicAuth()
app = Flask(__name__)

@auth.get_password
def get_password(username):
	if username == 'admin':
	   return 'admin'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error':'Unauthorized access'}), 401)

@app.route('/rackhd/login', methods=['POST'])
@auth.login_required
def rackhd_login():
	if not request.json or not 'username' in request.json:
		abort(400)

	user =  request.json['username']
	pw = request.json['password']
	
	url = "https://localhost:8443/login"
	payload = '{"username" : "' + user + '", "password" : "' + pw +'"}'
	
	headers= {
		"Content-Type": "application/json"
	}

	r = requests.post(url, headers=headers, data=payload, verify=False)
	return r.text

	#IPMIPOLLERS

@app.route('/rackhd/ipmipollers/read', methods=['GET'])
@auth.login_required
def read_ipmipollers():
        url = "https://localhost:8443/api/current/pollers"

        token = "JWT " + request.headers.get('token')

        headers = {
                "Content-Type": "application/json",
                "Authorization": token
        }

        r = requests.get(url, headers=headers, verify=False)
        return r.text

@app.route('/rackhd/ipmipollers/create', methods=['POST'])
@auth.login_required
def create_ipmipollers():
        url = "https://localhost:8443/api/current/pollers"

        token = "JWT " + request.headers.get('token')

        headers = {
                "Content-Type": "application/json",
                "Authorization": token
        }

        type = request.json['type']
	node = request.json['node']
	command = request.json['command']

	payload = '{"type":"' + type + '", "pollInterval":10000, "node":"' + node + '", "config": {"command":"' + command + '"}}'

        r = requests.post(url, headers=headers, data=payload, verify=False)
        return r.text

@app.route('/rackhd/ipmipollers/update', methods=['PATCH'])
@auth.login_required
def update_ipmipollers():
        
	base_url = "https://localhost:8443/api/current/pollers"

        pollerId = request.json['pollerId']

        url = base_url + "/" + pollerId

        token = "JWT " + request.headers.get('token')

        headers = {
                "Content-Type": "application/json",
                "Authorization": token
        }

        field = request.json['field']
        data = request.json['data']

	payload = '{"%s":"%s"}' % (field,data)

	r = requests.patch(url, headers=headers, data=payload, verify=False)

        return r.text

@app.route('/rackhd/ipmipollers/delete', methods=['DELETE'])
@auth.login_required
def delete_ipmipollers():

        base_url = "https://localhost:8443/api/current/pollers"

	pid = request.json['pid']

        url = base_url + "/" + pid

        token = "JWT " + request.headers.get('token')

        headers = {
                "Content-Type":"application/json",
                "Authorization": token
        }

        r = requests.delete(url, headers=headers, verify=False)
	return r.text


#IBMS

@app.route('/rackhd/ibms/create', methods=['PUT'])
@auth.login_required
def create_ibms():
	url = "https://localhost:8443/api/current/ibms"

	token = "JWT " + request.headers.get('Token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	nodeId = request.json['nodeId']
	service = request.json['service']
	community = request.json['community']
	host = request.json['host']

	payload = '{"nodeId": "' + nodeId + '", "service":"' + service + '", "config":{"community":"' + community + '", "host":"' + host + '"}}'

	response = requests.put(url, headers=headers, data=payload, verify=False)

	return response.text

@app.route('/rackhd/ibms/read', methods=['GET'])
@auth.login_required
def read_ibms():
	url = "https://localhost:8443/api/current/ibms"

	token = "JWT " + request.headers.get('Token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	response = requests.get(url, headers=headers, verify=False)

	return response.text

@app.route('/rackhd/ibms/update', methods=['PATCH'])
@auth.login_required
def update_ibms():
	base_url = "https://localhost:8443/api/current/ibms"

	id = request.json['id']

	url = base_url + "/" + id

	token = "JWT " + request.headers.get('Token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	service = request.json['service']
	community = request.json['community']
	host = request.json['host']

	payload = '{"service":"' + service + '", "config":{"community":"' + community + '", "host":"' + host + '"}}'

	response = requests.patch(url, headers=headers, data=payload, verify=False)

	return response.text

@app.route('/rackhd/ibms/delete', methods=['DELETE'])
@auth.login_required
def delete_ibms():
	base_url = "https://localhost:8443/api/current/ibms"

	id = request.json['id']

	url = base_url + "/" + id

	token = "JWT " + request.headers.get('token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": token
	}

	response = requests.delete(url, headers=headers, verify=False)

	return response.text


if __name__ == '__main__':
	app.run(debug=True)
