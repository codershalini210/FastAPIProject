from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import session 
from models.database import get_db
from models.ticketModel import Ticket
from models.ticketSchema import TicketCreate,TicketResponse

router = APIRouter()
# create a Ticket 
# find meaning of status code 201
@router.post("/ticket",response_model = TicketResponse,status_code = 201)
def create_Ticket(Ticket1:TicketCreate,db:session=Depends(get_db)):
    new_Ticket = Ticket(
        title=Ticket1.title,
        status =Ticket1.status,
        description = Ticket1.description
    )
    db.add(new_Ticket)
    db.commit()
    db.refresh(new_Ticket)  # it will update this new Ticket with id created by db 
    return new_Ticket

@router.get("/tickets",response_model = list[TicketResponse])
def get_all_Tickets(db:session=Depends(get_db)):
    Tickets= db.query(Ticket).all()
    return Tickets

@router.get("/ticket/{status}",response_model=list[TicketResponse])
def get_Ticket(status:str,db:session=Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.status==status)
    if ticket is None:
        raise HTTPException(
            status_code = 404,
            detail="Ticket not found "
        )
    return ticket

@router.put("/ticket/{Ticket_id}",response_model = TicketResponse)
def update_Ticket(Ticket_id:int,Ticket_data: TicketCreate, db:session=Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id==Ticket_id).first()
    if ticket is None:
            raise HTTPException(
                status_code = 404,
                detail="Ticket not found "
            )
    ticket.title = Ticket_data.title
    ticket.status = Ticket_data.status
    ticket.description = Ticket_data.description
    db.commit()
    db.refresh(ticket)
    return ticket

@router.delete("/ticket/{Ticket_id}")
def delete_Ticket(Ticket_id: int,db:session =Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id==Ticket_id).first()
    if ticket is None:
            raise HTTPException(
                status_code = 404,
                detail="Ticket not found "
            )
    db.delete(ticket)
    db.commit()
    return {
        "message":"Ticket deleted Successfully",
        "id":Ticket_id
    }