from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from uuid import uuid4
from datetime import datetime
from ..extensions import db


Base = declarative_base()

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
