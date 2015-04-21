import os
import socket
from swiftclient import client
usr = 'ywnag121'
key = ''		#change it to [passwordhere] before puting the code on github.
authurl = 'http://140.247.152.207:35357/v2.0'
ten = 'EC500-openstack-passthru'


def connect_swift():			###for createing connection to the account and getting an object to work on swift.
	con = client.Connection(authurl=authurl,user=usr, key=key,auth_version='2',tenant_name=ten, retries=5,)
	return con

from swiftclient import ClientException

def create_container(con, container):	###for creating a container from the connection object.
	try:
		con.put_container(container)
	except ClientException as e:
                return e.msg, e.http_status
	else:
		return "", 204
def delete_container(con, container):	### for deleting a container from the connection object.
	try:
		con.delete_container(container)
	except ClientException as e:
		return e.msg, e.http_status
	else:
                return "", 204


from flask import Flask, request
app = Flask(__name__)

@app.route("/<container>", methods=['PUT', 'DELETE', 'GET', 'POST', 'HEAD'])
def hello(container):
        if request.method == 'PUT':
                con = connect_swift()
                return create_container(con, container)
        elif request.method == 'DELETE':
                con = connect_swift()
                return delete_container(con, container)
        else:
                return "Not yet implemented", 501


@app.route("/<container>/<obj>", methods=['PUT', 'DELETE', 'GET', 'POST', 'HEAD'])
def func2(container, obj):
        return "Not Yet Implemented", 501

@app.route("/", methods=['GET'])
def bluh():
        return "", 204

if __name__ == "__main__":
        app.run()