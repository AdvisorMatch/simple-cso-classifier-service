from fastapi import FastAPI
from cso_classifier import CSOClassifier
from pydantic import BaseModel

class Paper(BaseModel):
    title: str
    abstract: str

cc = CSOClassifier(modules="both", enhancement="first", explanation=True)

app = FastAPI()



@app.post("/extract")
async def extract(paper: Paper):
    return cc.run(paper.dict())

