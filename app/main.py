from fastapi import FastAPI
import uvicorn
import numpy as np
import joblib
from pydantic.main import BaseModel

app = FastAPI(title="My ML App")

#create end points

@app.get("/")
def home():
    return"API is working as expected!"

class MyData(BaseModel):
    X: int
    
@app.post("/predict")
def predict(data:MyData):
    my_model = joblib.load("app/my_model")
    X = np.array(data.X).reshape(-1,1)
    return str(my_model.predict(X))

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
