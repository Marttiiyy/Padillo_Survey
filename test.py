from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine
from fastapi.middleware.cors import CORSMiddleware

from models import FoodPreference

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost:3000",  # React development server
    "https://example.com",    # Production frontend
    "*"
] # Define allowed origins (domains that can access your API)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow these origins
    allow_credentials=True,       # Allow cookies, authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)



@app.get("/FoodPreference")
async def root():
    return {"message": "FoodPreference"}


@app.get("/FoodPreference/{id}")
async def add_food(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        user = session.get("FoodPreference", id)
        return {"message": FoodPreference}
    

@app.post("/customers")
async def root(FoodPreference  : FoodPreference):
    with Session(engine) as session:
        session.add(FoodPreference)
        session.commit()
        session.refresh(FoodPreference)
        return {"message": FoodPreference}
    
@app.post("/customers")
async def root(users  : FoodPreference):
    with Session(engine) as session:

        print()
        statement = select(FoodPreference)
        results = session.exec(statement)

        # if(results)

        # print('-----------------------------')
        # print(Users.password , users.password)
        # print('-----------------------------')

        result = results.first()
        print(result)

        if (result == None):
            return {"status":"failed"}


        return {
            "status":"success",
            "data": result
            }
    