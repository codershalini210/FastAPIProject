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

@router.get("/items",response_model = list[ItemResponse])
def get_all_items(db:session=Depends(get_db)):
    items= db.query(Item).all()
    return items

@router.get("/item/{item_id}",response_model=ItemResponse)
def get_item(item_id:int,db:session=Depends(get_db)):
    item = db.query(Item).filter(Item.id==item_id).first()
    if item is None:
        raise HTTPException(
            status_code = 404,
            detail="Item not found "
        )
    return item

@router.put("/item/{item_id}",response_model = ItemResponse)
def update_item(item_id:int,item_data: ItemCreate, db:session=Depends(get_db)):
    item = db.query(Item).filter(Item.id==item_id).first()
    if item is None:
            raise HTTPException(
                status_code = 404,
                detail="Item not found "
            )
    item.name = item_data.name
    item.price = item_data.price
    item.in_stock = item_data.in_stock
    db.commit()
    db.refresh(item)
    return item

@router.delete("/item/{item_id}")
def delete_item(item_id: int,db:session =Depends(get_db)):
    item = db.query(Item).filter(Item.id==item_id).first()
    if item is None:
            raise HTTPException(
                status_code = 404,
                detail="Item not found "
            )
    db.delete(item)
    db.commit()
    return {
        "message":"Item deleted Successfully",
        "id":item_id
    }