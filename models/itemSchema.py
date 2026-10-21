from pydantic import BaseModel, ConfigDict
class ItemCreate(BaseModel):
    name:str
    price :int
    in_stock:bool

class ItemResponse(BaseModel):
    id:int
    name:str
    price :int
    in_stock:bool
    model_config = ConfigDict(from_attributes=True)