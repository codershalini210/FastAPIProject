from pydantic import BaseModel, ConfigDict
class TicketCreate(BaseModel):
    title:str
    status :str
    description:str
   

class TicketResponse(BaseModel):
    id:int
    title:str
    status :str
    description:str
    model_config = ConfigDict(from_attributes=True)