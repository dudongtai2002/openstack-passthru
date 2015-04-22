import os
import pdb#;pdb.set_trace()
import socket
#pdb.set_trace()
from cinderclient import client
import json



#cinderurl= 'http://10.31.27.207:8776/v2/d5785e4393ba4db5871c34b6a6c3ef7b'

version='2'
uname=username
pwd=password
ten = 'EC500-openstack-passthru'
authurl = 'http://140.247.152.207:35357/v2.0'



def connect_cinder(): #########works
	con=client.Client(version, uname, pwd , ten, authurl)
	return con


from cinderclient import exceptions

def get_volumes(con):
	try:                              ###########needs modification
		vlist=con.volumes.list()
#		print vlist[1]
#		print vlist[0]
		volumes=[]
		for i in range(len(vlist)):
			vdict=vlist[i].__dict__
			vol=[]
			vol.append(vdict['id'].encode('ascii','ignore'))
			vol.append(vdict['name'].encode('ascii','ignore'))
			vol.append(vdict['size'])
			print vol
			volumes.append(vol)
		return str(volumes),200
	except exception as e:
		return e.msg, e.http_status
	else:
		return "", 204



def create_volume(con,name1,size1):
	try:
		p=str(con.volumes.create(size1,name=name1))
		return p,200
	except exception as e:
		return e.msg, e.http_status
	else:
		return "", 204
          


			
##################################################################################################### flask:

from flask import Flask, request
app = Flask(__name__)


@app.route("/v2/<tenantid>/volumes", methods=[ 'GET', 'POST'])
def func2(tenantid): 
#####GET: curl -X GET http://localhost:5003/v2/EC500-openstack-passthru/volumes
#####POST: curl -X POST http://localhost:5003/v2/EC500-openstack-passthru/volumes -H "Volume-Name:test3" -H "Volume-Size:1"		        
        if  request.method == 'GET':		
		con=connect_cinder()
		return get_volumes(con)
	elif request.method == "POST":
		con=connect_cinder()
		name=request.headers.get('Volume-Name').encode('ascii','ignore')
		size=int(request.headers.get('Volume-Size'))
		print type(name)
		return 	create_volume(con,name,size)
        else:
                return "No Such Function", 501




	




if __name__ == "__main__":
        app.run(None,5003,True)
