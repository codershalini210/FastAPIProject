from sqlalchemy import Column,Integer,String,Boolean
from models.database import Base
class Item(Base):
    __tablename__ = "items"   
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable = False)
    price = Column(Integer,nullable=False)
    in_stock= Column(Boolean,nullable=False)