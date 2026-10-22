from sqlalchemy import Column,Integer,String,Boolean
from models.database import Base
class Ticket(Base):
    __tablename__ = "tickets"   
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable = False)
    status = Column(String,nullable=False)
    description= Column(String,nullable=False)