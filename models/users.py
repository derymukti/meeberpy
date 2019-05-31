from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text
from datetime import datetime
from main import db
class Users(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = db.Column(db.String(20), nullable=False,unique=True)
    password = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)    
    def __repr__(self):
        return '<Users %r>' % self.id