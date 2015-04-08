import os
import socket
from swiftclient import client
#usr = 'singh1'
#key = 'JRARJNS'
#authurl = 'http://140.247.152.207:35357/v2.0'
#ten = 'EC500-openstack-passthru'

#token1='MIITnAYJKoZIhvcNAQcCoIITjTCCE4kCAQExCTAHBgUrDgMCGjCCEfIGCSqGSIb3DQEHAaCCEeMEghHfeyJhY2Nlc3MiOiB7InRva2VuIjogeyJpc3N1ZWRfYXQiOiAiMjAxNS0wNC0wN1QyMjozNDoyMS41OTYzMTAiLCAiZXhwaXJlcyI6ICIyMDE1LTA0LTA3VDIzOjM0OjIxWiIsICJpZCI6ICJwbGFjZWhvbGRlciIsICJ0ZW5hbnQiOiB7ImRlc2NyaXB0aW9uIjogIiIsICJlbmFibGVkIjogdHJ1ZSwgImlkIjogImQ1Nzg1ZTQzOTNiYTRkYjU4NzFjMzRiNmE2YzNlZjdiIiwgIm5hbWUiOiAiRUM1MDAtb3BlbnN0YWNrLXBhc3N0aHJ1In19LCAic2VydmljZUNhdGFsb2ciOiBbeyJlbmRwb2ludHMiOiBbeyJhZG1pblVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3Ojg3NzQvdjIvZDU3ODVlNDM5M2JhNGRiNTg3MWMzNGI2YTZjM2VmN2IiLCAicmVnaW9uIjogIlJlZ2lvbk9uZSIsICJpbnRlcm5hbFVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3Ojg3NzQvdjIvZDU3ODVlNDM5M2JhNGRiNTg3MWMzNGI2YTZjM2VmN2IiLCAiaWQiOiAiNGMwZGI1ZmFlNzkxNDU4NGEwMTc4ZjY5NDE4YmQyYzYiLCAicHVibGljVVJMIjogImh0dHA6Ly8xNDAuMjQ3LjE1Mi4yMDc6ODc3NC92Mi9kNTc4NWU0MzkzYmE0ZGI1ODcxYzM0YjZhNmMzZWY3YiJ9XSwgImVuZHBvaW50c19saW5rcyI6IFtdLCAidHlwZSI6ICJjb21wdXRlIiwgIm5hbWUiOiAibm92YSJ9LCB7ImVuZHBvaW50cyI6IFt7ImFkbWluVVJMIjogImh0dHA6Ly8xMC4zMS4yNy4yMDc6OTY5Ni8iLCAicmVnaW9uIjogIlJlZ2lvbk9uZSIsICJpbnRlcm5hbFVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3Ojk2OTYvIiwgImlkIjogIjBjNDU2NTcxZDAzZjQzOWM4ZWJhY2YwOWE0OTZlM2JiIiwgInB1YmxpY1VSTCI6ICJodHRwOi8vMTQwLjI0Ny4xNTIuMjA3Ojk2OTYvIn1dLCAiZW5kcG9pbnRzX2xpbmtzIjogW10sICJ0eXBlIjogIm5ldHdvcmsiLCAibmFtZSI6ICJuZXV0cm9uIn0sIHsiZW5kcG9pbnRzIjogW3siYWRtaW5VUkwiOiAiaHR0cDovLzEwLjMxLjI3LjIwNzo4Nzc2L3YyL2Q1Nzg1ZTQzOTNiYTRkYjU4NzFjMzRiNmE2YzNlZjdiIiwgInJlZ2lvbiI6ICJSZWdpb25PbmUiLCAiaW50ZXJuYWxVUkwiOiAiaHR0cDovLzEwLjMxLjI3LjIwNzo4Nzc2L3YyL2Q1Nzg1ZTQzOTNiYTRkYjU4NzFjMzRiNmE2YzNlZjdiIiwgImlkIjogIjBjMGQyNmU1OWZiZDQ4MTVhMzAwZWM1OTI4ODBlYzcyIiwgInB1YmxpY1VSTCI6ICJodHRwOi8vMTQwLjI0Ny4xNTIuMjA3Ojg3NzYvdjIvZDU3ODVlNDM5M2JhNGRiNTg3MWMzNGI2YTZjM2VmN2IifV0sICJlbmRwb2ludHNfbGlua3MiOiBbXSwgInR5cGUiOiAidm9sdW1ldjIiLCAibmFtZSI6ICJjaW5kZXJ2MiJ9LCB7ImVuZHBvaW50cyI6IFt7ImFkbWluVVJMIjogImh0dHA6Ly8xMC4zMS4yNy4yMjMvc3dpZnQvdjEiLCAicmVnaW9uIjogIlJlZ2lvbk9uZSIsICJpbnRlcm5hbFVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjIzL3N3aWZ0L3YxIiwgImlkIjogIjNhZjM0ZGVmZjNhMjQ5MWJhZjRkZmMyNGRjYjAwMjJlIiwgInB1YmxpY1VSTCI6ICJodHRwOi8vMTQwLjI0Ny4xNTIuMjIzL3N3aWZ0L3YxIn1dLCAiZW5kcG9pbnRzX2xpbmtzIjogW10sICJ0eXBlIjogInMzIiwgIm5hbWUiOiAic3dpZnRfczMifSwgeyJlbmRwb2ludHMiOiBbeyJhZG1pblVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3OjkyOTIiLCAicmVnaW9uIjogIlJlZ2lvbk9uZSIsICJpbnRlcm5hbFVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3OjkyOTIiLCAiaWQiOiAiNTgzMDhkOGMxOGFlNGViZDgzZGJjZDE2NDE5MzVkZGIiLCAicHVibGljVVJMIjogImh0dHA6Ly8xNDAuMjQ3LjE1Mi4yMDc6OTI5MiJ9XSwgImVuZHBvaW50c19saW5rcyI6IFtdLCAidHlwZSI6ICJpbWFnZSIsICJuYW1lIjogImdsYW5jZSJ9LCB7ImVuZHBvaW50cyI6IFt7ImFkbWluVVJMIjogImh0dHA6Ly8xMC4zMS4yNy4yMDc6ODM4Ni8iLCAicmVnaW9uIjogIlJlZ2lvbk9uZSIsICJpbnRlcm5hbFVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3OjgzODYvIiwgImlkIjogIjBhMjQxZjBlMThmMDQwOWM4ODc0ZGQwNzg3OTYxZjJmIiwgInB1YmxpY1VSTCI6ICJodHRwOi8vMTQwLjI0Ny4xNTIuMjA3OjgzODYvIn1dLCAiZW5kcG9pbnRzX2xpbmtzIjogW10sICJ0eXBlIjogImRhdGFfcHJvY2Vzc2luZyIsICJuYW1lIjogInNhaGFyYSJ9LCB7ImVuZHBvaW50cyI6IFt7ImFkbWluVVJMIjogImh0dHA6Ly8xMC4zMS4yNy4yMDc6ODAwMC92MS8iLCAicmVnaW9uIjogIlJlZ2lvbk9uZSIsICJpbnRlcm5hbFVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3OjgwMDAvdjEvIiwgImlkIjogIjI3NTJjMzk1YWRmMzQ0Y2M5MGE3MGFkMzQzZDQ3MjU5IiwgInB1YmxpY1VSTCI6ICJodHRwOi8vMTQwLjI0Ny4xNTIuMjA3OjgwMDAvdjEvIn1dLCAiZW5kcG9pbnRzX2xpbmtzIjogW10sICJ0eXBlIjogImNsb3VkZm9ybWF0aW9uIiwgIm5hbWUiOiAiaGVhdC1jZm4ifSwgeyJlbmRwb2ludHMiOiBbeyJhZG1pblVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3Ojg3NzciLCAicmVnaW9uIjogIlJlZ2lvbk9uZSIsICJpbnRlcm5hbFVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3Ojg3NzciLCAiaWQiOiAiYWQ1ZmNhNzk2ZDg2NGZhZDkwNjlhZjA5MDY2YjdmM2UiLCAicHVibGljVVJMIjogImh0dHA6Ly8xNDAuMjQ3LjE1Mi4yMDc6ODc3NyJ9XSwgImVuZHBvaW50c19saW5rcyI6IFtdLCAidHlwZSI6ICJtZXRlcmluZyIsICJuYW1lIjogImNlaWxvbWV0ZXIifSwgeyJlbmRwb2ludHMiOiBbeyJhZG1pblVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3Ojg3NzYvdjEvZDU3ODVlNDM5M2JhNGRiNTg3MWMzNGI2YTZjM2VmN2IiLCAicmVnaW9uIjogIlJlZ2lvbk9uZSIsICJpbnRlcm5hbFVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3Ojg3NzYvdjEvZDU3ODVlNDM5M2JhNGRiNTg3MWMzNGI2YTZjM2VmN2IiLCAiaWQiOiAiNDk3MTI1NWFhNzMwNGNjNzgwMjJmODA0NWViNTMwMGYiLCAicHVibGljVVJMIjogImh0dHA6Ly8xNDAuMjQ3LjE1Mi4yMDc6ODc3Ni92MS9kNTc4NWU0MzkzYmE0ZGI1ODcxYzM0YjZhNmMzZWY3YiJ9XSwgImVuZHBvaW50c19saW5rcyI6IFtdLCAidHlwZSI6ICJ2b2x1bWUiLCAibmFtZSI6ICJjaW5kZXIifSwgeyJlbmRwb2ludHMiOiBbeyJhZG1pblVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3Ojg3NzMvc2VydmljZXMvQWRtaW4iLCAicmVnaW9uIjogIlJlZ2lvbk9uZSIsICJpbnRlcm5hbFVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3Ojg3NzMvc2VydmljZXMvQ2xvdWQiLCAiaWQiOiAiOTQ5M2U1NmI4NmEwNDhhMTg5M2MwMjhiYjU2ZDEyMDEiLCAicHVibGljVVJMIjogImh0dHA6Ly8xNDAuMjQ3LjE1Mi4yMDc6ODc3My9zZXJ2aWNlcy9DbG91ZCJ9XSwgImVuZHBvaW50c19saW5rcyI6IFtdLCAidHlwZSI6ICJlYzIiLCAibmFtZSI6ICJub3ZhX2VjMiJ9LCB7ImVuZHBvaW50cyI6IFt7ImFkbWluVVJMIjogImh0dHA6Ly8xMC4zMS4yNy4yMDc6ODAwNC92MS9kNTc4NWU0MzkzYmE0ZGI1ODcxYzM0YjZhNmMzZWY3YiIsICJyZWdpb24iOiAiUmVnaW9uT25lIiwgImludGVybmFsVVJMIjogImh0dHA6Ly8xMC4zMS4yNy4yMDc6ODAwNC92MS9kNTc4NWU0MzkzYmE0ZGI1ODcxYzM0YjZhNmMzZWY3YiIsICJpZCI6ICI2ZTk0Y2ZiNDVkOTQ0MGZhOGFhZjE4NjRiOWUyYjA1YiIsICJwdWJsaWNVUkwiOiAiaHR0cDovLzE0MC4yNDcuMTUyLjIwNzo4MDA0L3YxL2Q1Nzg1ZTQzOTNiYTRkYjU4NzFjMzRiNmE2YzNlZjdiIn1dLCAiZW5kcG9pbnRzX2xpbmtzIjogW10sICJ0eXBlIjogIm9yY2hlc3RyYXRpb24iLCAibmFtZSI6ICJoZWF0In0sIHsiZW5kcG9pbnRzIjogW3siYWRtaW5VUkwiOiAiaHR0cDovLzEwLjMxLjI3LjIyMy9zd2lmdC92MSIsICJyZWdpb24iOiAiUmVnaW9uT25lIiwgImludGVybmFsVVJMIjogImh0dHA6Ly8xMC4zMS4yNy4yMjMvc3dpZnQvdjEiLCAiaWQiOiAiNTYzYzE0NTQyZjBjNGJjNzlmNTI5ZjRmY2Y2ZjBjYjEiLCAicHVibGljVVJMIjogImh0dHA6Ly8xNDAuMjQ3LjE1Mi4yMjMvc3dpZnQvdjEifV0sICJlbmRwb2ludHNfbGlua3MiOiBbXSwgInR5cGUiOiAib2JqZWN0LXN0b3JlIiwgIm5hbWUiOiAic3dpZnQifSwgeyJlbmRwb2ludHMiOiBbeyJhZG1pblVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3OjM1MzU3L3YyLjAiLCAicmVnaW9uIjogIlJlZ2lvbk9uZSIsICJpbnRlcm5hbFVSTCI6ICJodHRwOi8vMTAuMzEuMjcuMjA3OjUwMDAvdjIuMCIsICJpZCI6ICIwNjYxOTY3M2M5NmI0NGE5YWRiNGYwODI1N2JiOTBiMCIsICJwdWJsaWNVUkwiOiAiaHR0cDovLzE0MC4yNDcuMTUyLjIwNzo1MDAwL3YyLjAifV0sICJlbmRwb2ludHNfbGlua3MiOiBbXSwgInR5cGUiOiAiaWRlbnRpdHkiLCAibmFtZSI6ICJrZXlzdG9uZSJ9XSwgInVzZXIiOiB7InVzZXJuYW1lIjogImRkdDA1MjMiLCAicm9sZXNfbGlua3MiOiBbXSwgImlkIjogIjE3MDQ3YTlkYzE1NjRhNjZhMzdlYTVmZDllNWE3YjA3IiwgInJvbGVzIjogW3sibmFtZSI6ICJfbWVtYmVyXyJ9XSwgIm5hbWUiOiAiZGR0MDUyMyJ9LCAibWV0YWRhdGEiOiB7ImlzX2FkbWluIjogMCwgInJvbGVzIjogWyI5ZmUyZmY5ZWU0Mzg0YjE4OTRhOTA4NzhkM2U5MmJhYiJdfX19MYIBgTCCAX0CAQEwXDBXMQswCQYDVQQGEwJVUzEOMAwGA1UECAwFVW5zZXQxDjAMBgNVBAcMBVVuc2V0MQ4wDAYDVQQKDAVVbnNldDEYMBYGA1UEAwwPd3d3LmV4YW1wbGUuY29tAgEBMAcGBSsOAwIaMA0GCSqGSIb3DQEBAQUABIIBACHIr3ZnbedqK6Maoj21Z25F0BcibXU0fuicG1HLgPzMTcZe6a5YeVUM9OYcb4OpkvI2AN51EScUpWneZK5kSgoizcFg2HHVaMniwVYja8b-C6eXiRoAx9o+YueG0fABQ1vEyGk9zUKip3ivb-hKU4gi1VzJvO2NJi4Onfvd+q3vB7XqqKMlEqJQjNkkYcagZc9ycfGERitoeLqSXgHhNt7ikNW654z6sNqrr8tpouBzf27nROFckBRQxrN5fPUEjlGhs5rIQU-C65FkCWHjOHjQPOEknfYIujZ7LKYgp+lUAL8SX+vh0VvSB2tqMVMBjI4DN9QLAzUuCwT6GVrhf1I='

def connect_swift(token):			###for createing connection to the account and getting an object to work on swift.
	print token
	con = client.Connection(preauthurl='http://140.247.152.223/swift/v1' ,preauthtoken=token,auth_version='2', retries=10,)
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
def get_container(con, container): ### for listing a container's objects and information.
	try:
		headers, result = con.get_container(container)
		return str(result),200
	except ClientException as e:
		return e.msg, e.http_status
	else:
		return "", 204

def get_account(con):
	try:
		headers, result = con.get_account()
		#print "wetwerewr"
		#print result
		#print type(result)
		return str(result), 200
		#return str(result),200
	except ClientException as e:
		print e.msg		
		return e.msg, e.http_status
	else:
		"", 204
def get_object(con,container,obj):  ### for download an object from the container
        try:
		
                headers,result = con.get_object(container, obj)
		return str(result),200
        except ClientException as e:
		
                return e.msg, e.http_status
        else:
		
                return "object find", 204

################### Update contaner, object, and account require testing                
def update_containerMetaData(con, container,headers): ###update container metadata 
	try:
		con.post_container(container,headers)
	except ClientException as e:
                return e.msg, e.http_status
	else:
		return "", 204

def update_objectMetaData(con, container, obj,headers): ###update objects metadata
	try:
		con.post_object(container, obj,headers)
	except ClientException as e:
                return e.msg, e.http_status
	else:
		return "", 204
			
def update_accountMetaData(con,headers): ###update objects metadata- Not sure if its implemented properly
	try:
		con.post_account(headers)
	except ClientException as e:
                return e.msg, e.http_status
	else:
		return "", 204
			

def upload_object(con, container,obj,objct):		###method to upload the objects in container.	
	try:
		ret = con.put_object(container, obj,objct)
	except ClientException as e:

		return e.msg, e.http_status
	else:

                return "", 204

def delete_object(con,container,obj):			###method to delete the objects in container.
	try:
		con.delete_object(container, obj)
	except ClientException as e:

		return e.msg, e.http_status
	else:

                return "", 204
              
def head_account(con):### show account metadata
                try:
			headers=con.head_account()
			##print headers
			return headers,200
		except ClientException as e:
			print e.msg
			return e.msg,e.http_status
		else:
			return "",204

def head_container(con,container):### show container metadata
                try:
			headers=con.head_container(container)
			##print headers
			return headers,200
		except ClientException as e:
			return e.msg,e.http_status
		else:
			return "",204
def head_object(con,container,obj):### show object metadata
                try:
			headers=con.head_object(container,obj)
			return headers,200
		except ClientException as e:
			return e.msg,e.http_status
		else:
			return "",204

##################################################################################################### flask:

from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'HEAD'])
def func1():
	if request.method == 'GET':
		token=request.headers.get('X-Auth-Token')
		con = connect_swift(token)
		return get_account(con)
	elif request.method == 'POST':
		token=request.headers.get('X-Auth-Token')
		con = connect_swift(token)
		return update_accountMetaData(con)
	elif request.method=='Head':
		token=request.headers.get('X-Auth-Token');
 		con=connect_swift(token)
		head,status =  head_account(con)
		print head
		return "", status, head
	elif request.method == "POST":
		token=request.headers.get('X-Auth-Token');
		con = connect_swift(token)
		head = request.headers
		headers = {}
		for key in head:
			headers[key[0]] = key[1]
		
		return update_accountMetaData(con,headers)
	
	else:
		return "Not yet implemented", 501

@app.route("/<container>", methods=['PUT', 'DELETE', 'GET', 'POST', 'HEAD'])
def func2(container):
        if request.method == 'PUT':
		token=request.headers.get('X-Auth-Token');
                con = connect_swift(token)
                return create_container(con, container)
        elif request.method == 'DELETE':
		token=request.headers.get('X-Auth-Token');
                con = connect_swift(token)
                return delete_container(con, container)
	elif request.method == 'GET':
		token=request.headers.get('X-Auth-Token');
		con = connect_swift(token)
		return get_container(con, container)
	elif request.method == "POST":
		token=request.headers.get('X-Auth-Token');
		con = connect_swift(token)
		head = request.headers
		headers = {}
		for key in head:
			headers[key[0]] = key[1]
		
		return update_containerMetaData(con, container,headers)
	
	elif request.method=='HEAD':
		token=request.headers.get('X-Auth-Token');
		con=connect_swift(token)
		head,status=head_container(con,container)
		return "",status,head
        else:
                return "Not yet implemented", 501


@app.route("/<container>/<obj>", methods=[ 'PUT', 'DELETE', 'GET', 'POST', 'HEAD', 'COPY'])
def func3(container, obj):
        if request.method=='GET':
		token=request.headers.get('X-Auth-Token');
                con=connect_swift(token)
                return get_object(con,container,obj)
	elif request.method == 'PUT':	
		token=request.headers.get('X-Auth-Token');			###method to upload/replace the objects in container.
		con = connect_swift(token)
		objct = request.get_data()
		return upload_object(con,container,obj,objct)
	elif request.method == 'DELETE':
		token=request.headers.get('X-Auth-Token');			###method to delete an object from a container.
		con = connect_swift(token)
		return delete_object(con,container,obj)
	elif request.method == 'COPY':   ###method to copy an object
		token=request.headers.get('X-Auth-Token');
		con = connect_swift(token)
		p=request.headers.get('Destination')
		p1=str(p).split('/')
		#print p1
		header,result = con.get_object(container,obj)
		return upload_object(con,p1[0],p1[1],result)
	elif request.method=='HEAD':
		token=request.headers.get('X-Auth-Token');
		con=connect_swift(token)
		head,status=get_object(con,container,obj)
		return "",status,head
	elif request.method == "POST":
		token = request.headers.get('X-Auth-Token')
		print type(token)
		str(token)
		con = connect_swift(str(token))
		head = request.headers
		headers = {}
		for key in head:
			headers[key[0]] = key[1]
		
		return update_objectMetaData(con, container, obj,headers)
	

        else:
        	return "Not Yet Implemented", 501

	




if __name__ == "__main__":
        app.run(None,5001,True)
