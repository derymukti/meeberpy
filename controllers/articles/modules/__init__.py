from flask import request,Response
from manager.json_response import response
from models.articles import Articles
from main import db

def hello():
    print request.args
    return "hello"

def stores():
    try:
        data = request.get_json()
        title = data['title']
        description = data['description']
        article = Articles(title=title,description=description)
        db.session.add(article)
        db.session.commit()
        article_data = get_articles()
        return response(data=article_data,code=200,message="success")
    except Exception as err:
        return response(code=202,message=str(err))

def updates():
    try:
        data = request.get_json()
        ids=data['id']
        title = data['title']
        description = data['description']
        user = Articles.query.filter_by(id=ids).first()
        user.title = title
        user.description = description
        db.session.commit()
        article_data = get_articles()
        return response(data=article_data,code=200,message="success")
    except Exception as err:
        return response(code=202,message=str(err))

def deletes():
    try:
        data = request.get_json()
        ids=data['id']
        me = Articles.query.filter_by(id=ids).first()
        db.session.delete(me)
        db.session.commit()
        article_data = get_articles()
        return response(data=article_data,code=200,message="success")
    except Exception as err:
        return response(code=202,message=str(err))

def get():
    try:
        article_data = get_articles()
        return response(data=article_data,code=200,message="success")
    except Exception as err:
        return response(code=202,message=str(err))

def get_articles():
    try:
        try:
            limit = request.args['limit']
        except:
            limit = 10
        articles = Articles.query.limit(limit).all()
        article_data = []
        for article in articles:
            ids = str(article.id)
            title = article.title
            description = article.description
            createdAt = article.createdAt.strftime("%m/%d/%Y, %H:%M:%S")
            usr = {"id":ids,"title":title,"description":description,"createdAt":createdAt}
            article_data.append(usr)
        return article_data
    except:
        return []