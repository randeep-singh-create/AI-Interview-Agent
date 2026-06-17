from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,Text
Base = declarative_base() # table de sare function is d help nal chlde ne(save,update,delete)
class Interview(Base):
    __tablename__ = 'interview'
    id = Column(Integer,primary_key=True)
    Candidate_Name=Column(String)
    Role=Column(String)
    Report=Column(Text)
