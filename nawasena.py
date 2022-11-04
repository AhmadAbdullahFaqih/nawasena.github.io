from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def root():
    return 'Hello World, by PABW 7B2 Nawasena'
