
import os
import json
from sqlalchemy import Column, String, Integer, Boolean, create_engine
from flask_sqlalchemy import SQLAlchemy


database_name = 'books'
database_path = 'postgres://{}:{}@{}/{}'.format(
'victor',
'cyberfalcon', 
"localhost:5432", database_name)


db = SQLAlchemy()

'''
  binds a flask application and SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  db.init_app(app)
  db.create_all()



'''
Book Class:
'''
class Book(db.Model):
  __tablename__ = 'books'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  author = Column(String)
  rating = Column(String)

  def __init__(self, title, author, rating):
    self.title = title
    self.author = author
    self.rating = rating

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()
  
  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  def format(self):
    return {
      "id": self.id,
      "title": self.title,
      "author": self.author,
      "rating": self.rating
    }


