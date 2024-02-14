from fastapi import FastAPI, Request
from args import get_args
import uvicorn
import sqliteDB as helpers
import logging
import time

app = FastAPI()
db = "database.db"
args = get_args()

@app.get("/")
def root():
    return({ "message": "hello world" })


@app.post("/create_url")
async def create_url(request: Request):
    
    data = await request.json()
    
    if "alias" not in data:
        data["alias"] = ""
    if helpers.already_exist(db, data["alias"]):
        return { "message": "please create a unique alias"} 
    
    helpers.add_url(db, data["url"], data["alias"])
    return { "url": data["url"], "alias": data["alias"] }
    
    
@app.get("/delete_url/{alias}")
def delete_url(alias: str):
    
    if helpers.already_exist(db, alias):
        helpers.delete_url(db, alias)
        return { "message": "the shorten url has be deleted successfully"}    
    else:
        return { "message": "the url is not found" }
    

@app.get("/find/{alias}")
def find_url(alias: str):
    try: 
        return {"url": helpers.get_url(db, alias) }
    
    except:
        return { "message": "the url is not found" }
    

@app.get("/list_all")
def list_all():
    return helpers.get_all_urls(db)


logging.Formatter.converter = time.gmtime
logging.basicConfig(
    format="%(asctime)s.%(msecs)03dZ %(levelname)s:%(name)s:%(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    level= logging.ERROR - (args.verbose*10),
)

if __name__ == "__main__":
    uvicorn.run("server:app", host=args.host, port=args.port, reload=args.reload)
