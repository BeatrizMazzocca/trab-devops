from fastapi import FastAPI

app = FastAPI()

@app.get("/Hello world!")
async def hello_world():
    return {"message": "Hello World"}

@app.get("/funcaotest")
async def funcao_test():
    return {"teste": "Deu muito certo!"}


#novo teste
#teste-final
  

