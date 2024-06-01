import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modules')))

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from args import get_args
import uvicorn
import sqliteDB as helpers
import logging
import time

app = FastAPI()
args = get_args()
db = args.db_path

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return({ "message": "hello world" })

@app.post("/create_url")
async def create_url(request: Request):
    
    data = await request.json()
    
    if "alias" not in data:
        data["alias"] = ""
        
    if helpers.already_exist(db, data["alias"]):
        
        logging.error(f'The alias: {data["alias"]} provided was not unique')
        raise HTTPException(status_code=400, detail="Please enter a unique alias")
    
    helpers.add_url(db, data["url"], data["alias"]) 
    logging.debug(f'Request recieved for creating url with {data["url"]} and {data["alias"]}')
    
    return { "url": data["url"], "alias": data["alias"] }
    
@app.get("/delete_url/{alias}")
def delete_url(alias: str):
    
    logging.debug(f'Request recieved for deleting url with alias: {alias}')
    
    if helpers.already_exist(db, alias):
        helpers.delete_url(db, alias)
        return { "message": "the shorten url has be deleted successfully"}    
    else:
        logging.error(f'The url with the alias: {alias} was not found')
        return { "message": "the url is not found" }
    
@app.get("/find/{alias}")
def find_url(alias: str):
    
    logging.debug(f'Request recieved for finding the url with alias: {alias}')
    
    try: 
        return {"url": helpers.get_url(db, alias) }
    
    except:
        logging.error(f'Request recieved for deleting url with alias: {alias}')
        return { "message": "the url is not found" }
    

@app.get("/list_all")
def list_all():
    
    logging.debug(f'Request recieved for listing all urls')
    return helpers.get_all_urls(db)


logging.Formatter.converter = time.gmtime
logging.basicConfig(
    format="%(asctime)s.%(msecs)03dZ %(levelname)s:%(name)s:%(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    level= logging.ERROR - (args.verbose*10),
)

if __name__ == "__main__":
    uvicorn.run("server:app", host=args.host, port=args.port, reload=args.reload)
