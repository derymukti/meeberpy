from flask import Response
import json,os,uuid
def response(data=None,code=200,message='Success'):
	server = str(uuid.uuid3(uuid.NAMESPACE_DNS,str(os.getpid())))
	res = {"data":data,
    		'meta': {
    			'message': message,
				'code': code,
				'server':server
				}
			}
	result = json.dumps(res)
	resp = Response(result, status=code, mimetype='application/json')
	return resp