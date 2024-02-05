from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import sqliteDB

app = FastAPI()

class newUrl(BaseModel):
    url: str
    alias: str


@app.get("/")
def root():
    return({ "message": "hello world" })


@app.post("/create_url")
def create_url(entriee: newUrl):
    
    if [x for x in sqliteDB.get_all_urls() if x["url"]==entriee.url]:
        return { "message": "the an alias has already been created for that url"}    
    else:
        sqliteDB.add_url(entriee.url, entriee.alias)
        return { "url": entriee.url, "alias": entriee.alias }
    

@app.get("/delete_url/{alias}")
def delete_url(alias: str):
    
    if [x for x in sqliteDB.get_all_urls() if x["alias"]==alias]:
        sqliteDB.delete_url(alias)
        return { "message": "the shorten url has be deleted successfully"}    
    else:
        return { "message": "the url is not found" }
    

@app.get("/find/{alias}")
def find_url(alias: str):
    try: 
        return {"url": sqliteDB.get_url(alias) }
    
    except:
        return { "message": "the url is not found" }
    

@app.get("/list_all")
def list_all():
    return sqliteDB.get_all_urls()


if __name__ == "__main__":
    uvicorn.run("server:app", port=8080, reload=True)
    
