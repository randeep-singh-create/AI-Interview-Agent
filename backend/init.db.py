# database nu chlaun te create krn lei use krde ha ( for initialize the database )
from database import engine
from model import Base

Base.metadata.create_all(bind=engine)
