from fastapi import FastAPI, Request
import uvicorn
import sqliteDB as helpers


app = FastAPI()

db = "database.db"

@app.get("/")
def root():
    return({ "message": "hello world" })


@app.post("/create_url")
async def create_url(request: Request):
    
    data = await request.json()
    
    if "alias" not in data:
        data["alias"] = helpers.generateHash()
    
    
    if helpers.already_exist(db, data["alias"]):
        return { "message": "please create a unique alias"}    
    else:
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


if __name__ == "__main__":
    uvicorn.run("server:app", port=8080, reload=True)
