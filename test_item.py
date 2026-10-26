import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from main import app 
from models.database import Base,get_db
from models.itemModel import Item

test_engine = create_engine("sqlite://",connect_args={"check_same_thred":False},poolclass=StaticPool)

TestingSessionLocal = sessionmaker(autocommit=False,autoFlush = False,bind = test_engine)

def override_get_db():
    db=TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@pytest.fixture
def client():
    Base.metadata.create_all(bind=test_engine)
    app.dependency_overrides[get_db] = override_get_db
    try: 
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency.overrides.clear()
        Base.metadaba.drop_ll(bind=test_engine)