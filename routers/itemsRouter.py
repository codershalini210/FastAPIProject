from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import session 
from models.database import get_db
from models.itemModel import Item
from models.itemSchema import ItemCreate,ItemResponse

router = APIRouter()
# create a item 
# find meaning of status code 201
@router.post("/item",response_model = ItemResponse,status_code = 201)
def create_Item(item:ItemCreate,db:session=Depends(get_db)):
    new_item = Item(
        name=item.name,
        price =item.price,
        in_stock = item.in_stock
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)  # it will update this new item with id created by db 
    return new_item
