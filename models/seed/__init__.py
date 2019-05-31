from models.users import Users
from main import db
def seed_data():
    try:
        user=Users(username='dery',password='1234')
        db.session.add(user)
        db.session.commit()
        print "success seed data"
    except Exception as err:
        exit(err)