from flask import request,Response
from manager.json_response import response
from models.users import Users
from main import db

def hello():
    print request.args
    return "hello"

def stores():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        user = Users(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        user_data = get_user()
        return response(data=user_data,code=200,message="success")
    except Exception as err:
        return response(code=202,message=str(err))

def updates():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        user = Users.query.filter_by(username=username).first()
        user.password = password
        db.session.commit()
        user_data = get_user()
        return response(data=user_data,code=200,message="success")
    except Exception as err:
        return response(code=202,message=str(err))

def deletes():
    try:
        data = request.get_json()
        username = data['username']
        me = Users.query.filter_by(username=username).first()
        db.session.delete(me)
        db.session.commit()
        user_data = get_user()
        return response(data=user_data,code=200,message="success")
    except Exception as err:
        return response(code=202,message=str(err))

def get():
    try:
        user_data = get_user()
        return response(data=user_data,code=200,message="success")
    except Exception as err:
        return response(code=202,message=str(err))

def get_user():
    try:
        try:
            limit = request.args['limit']
        except:
            limit = 10
        user = Users.query.limit(limit).all()
        user_data = []
        for u in user:
            uname = u.username
            pwd = u.password
            usr = {"username":uname,"password":pwd}
            user_data.append(usr)
        return user_data
    except:
        return []