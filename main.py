from fastapi import FastAPI

app = FastAPI()


@app.get("/Hello world!")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaotest")
async def root():
    return {"teste": "Deu muito certo!"}

#novo teste
  
