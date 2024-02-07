from fastapi import FastAPI, Request
import uvicorn
import sqliteDB as helpers

app = FastAPI()


@app.get("/")
def root():
    return({ "message": "hello world" })


@app.post("/create_url")
async def create_url(request: Request):
    
    data = await request.json()
    
    if helpers.already_exist(request["alias"]):
        return { "message": "please create a unique alias"}    
    else:
        helpers.add_url(request["url"], request["alias"])
        return { "url": request["url"], "alias": request["alias"] }
    

@app.get("/delete_url/{alias}")
def delete_url(alias: str):
    
    if helpers.already_exist(alias):
        helpers.delete_url(alias)
        return { "message": "the shorten url has be deleted successfully"}    
    else:
        return { "message": "the url is not found" }
    

@app.get("/find/{alias}")
def find_url(alias: str):
    try: 
        return {"url": helpers.get_url(alias) }
    
    except:
        return { "message": "the url is not found" }
    

@app.get("/list_all")
def list_all():
    return helpers.get_all_urls()


if __name__ == "__main__":
    uvicorn.run("server:app", port=8080, reload=True)
