from models.articles import Articles
from main import db
def seed_data():
    try:
        articles=Articles(title='Test Post',description='This is a description')
        db.session.add(articles)
        db.session.commit()
        print("success seed data")
    except Exception as err:
        exit(err)