from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

db = create-engine("postgreSQL:///chinook")
base = declarative_base()

Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)

#Now that we have the file set up, we can start to build our class-based models.
#These will be quite similar to how we did them in the last lesson, but this time, we
#get to simply build a normal Python object, that subclasses 'base'.

