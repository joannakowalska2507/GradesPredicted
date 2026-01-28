import joblib
from fastapi import FastAPI,Depends
from pydantic import BaseModel
import numpy as np
from pathlib import Path
from src.utils import label_from_num
from sqlalchemy.orm import session, Session
from database import SessionLocal,engine,Base,Prediction

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
model_path = BASE_DIR / "model" / "model.pkl"
with open(model_path, "rb") as f:
    model = joblib.load(f)

class PredictionRequest(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float
    feature5: float

@app.post("/predict")
def predict(data: PredictionRequest,db=Depends(get_db)):

    features=np.array([[data.feature1,data.feature2,data.feature3,data.feature4,data.feature5]])
    prediction = model.predict(features)[0]
    prediction=label_from_num(prediction)
    db_pred=Prediction(
        math=data.feature1,
        reading=data.feature2,
        writing=data.feature3,
        attendance=data.feature4,
        homework=data.feature5,
        grade=prediction
    )
    db.add(db_pred)
    db.commit()
    db.refresh(db_pred)

    return {"prediction":prediction}

@app.get("/predictions")
def read_predictions(db: Session = Depends(get_db)):
    return db.query(Prediction).all()
@app.delete("/predictions")
def delete_predictions(db: Session = Depends(get_db)):
    db.query(Prediction).delete()
    db.commit()
    return {"status": "ok"}