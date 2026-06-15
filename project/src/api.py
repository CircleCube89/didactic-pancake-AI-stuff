from fastapi import FastAPI, HTTPException
import pickle
from  pydantic import BaseModel, Field
import os
import myConfig
import logging
os.chdir(myConfig.absPath)
app = FastAPI()
wheights_file= "artifacts/regression.sav"
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:     %(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)
class PredictRequest(BaseModel):
    

    Hours_Studied: int = Field(default=23)
    Attendance: int = Field(ge=0,le= 100 ,default=84)
    Parental_Involvement:str = Field(default="Low")
    Access_to_Resources:str = Field(default="High")
    Extracurricular_Activities:bool =Field(default=False)
    Sleep_Hours:int = Field(default=7)
    Previous_Scores:int = Field(default=73)
    Motivation_Level:str = Field(default="Low")
    Internet_Access:bool = Field(default=True)
    Tutoring_Sessions:int = Field(default=0)
    Family_Income:str= Field(default="Low")
    Teacher_Quality:str = Field(default="Medium")
    School_Type:str = Field(default="Public")
    Peer_Influence:str = Field(default="Positive")
    Physical_Activity:int = Field(default=3)
    Learning_Disabilities:bool = Field(default=False)
    Parental_Education_Level:str = Field(default="High School")
    Distance_from_Home:str = Field(default="Near")
    Gender:str = Field("Male")
    

@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Простейший health-check сервиса."""
    try:
        pickle.load(open(wheights_file, 'rb'))
        return {
        "status": "ok",
        "weigts_file": wheights_file,
        "version": "0.1.0",
    }
    except:{
        "status": "error, failed to load model",
        "weigts_file": wheights_file,
        "version": "0.1.0",}
@app.get("/")
def read_root():
    return {"message": "Привет мир!"}

@app.post("/predict")
def predict(req:PredictRequest):
    model = pickle.load(open(wheights_file, 'rb'))
    data = []
    
    if req.Gender=="Male":
        data.append(1)
        data.append(0)
    elif req.Gender =="Female":
        data.append(0)
        data.append(1)
    else:
        logger.warning("Wrong gender")
        return HTTPException(status_code=422,detail="Wrong gender")
    

    if req.Learning_Disabilities:
        data.append(1)
        data.append(0)
    else:
        data.append(0)
        data.append(1)


    if req.Distance_from_Home=="Near":
        data.append(1)
        data.append(0)
        data.append(0)
    elif req.Distance_from_Home=="Moderate":
        data.append(0)
        data.append(1)
        data.append(0)
    elif req.Distance_from_Home=="Far":
        data.append(0)
        data.append(0)
        data.append(1)
    else:
        logger.warning("Wrong distance")
        return HTTPException(status_code=422,detail="Wrong distance")
    
    if req.Parental_Education_Level=="Postgraduate":
        data.append(1)
        data.append(0)
        data.append(0)
    elif req.Parental_Education_Level=="High School":
        data.append(0)
        data.append(1)
        data.append(0)
    elif req.Parental_Education_Level=="College":
        data.append(0)
        data.append(0)
        data.append(1)
    else:
        logger.warning("Wrong Parental_Education_Level")
        return HTTPException(status_code=422,detail="Wrong Parental_Education_Level")
    
    if req.Peer_Influence=="Positive":
        data.append(1)
        data.append(0)
        data.append(0)
    elif req.Peer_Influence=="Neutral":
        data.append(0)
        data.append(1)
        data.append(0)
    elif req.Peer_Influence=="Negative":
        data.append(0)
        data.append(0)
        data.append(1)
    else:
        logger.warning("Wrong Peer_Influence")
        return HTTPException(status_code=422,detail="Wrong Peer_Influence")
    if req.School_Type=="Public":
        data.append(1)
        data.append(0)
    elif req.School_Type=="Private":
        data.append(0)
        data.append(1)
    else:
        logger.warning("Wrong School_Type")
        return HTTPException(status_code=422,detail="Wrong School_Type")
    if req.Teacher_Quality=="Medium":
        data.append(1)
        data.append(0)
        data.append(0)
    elif req.Teacher_Quality=="Low":
        data.append(0)
        data.append(1)
        data.append(0)
    elif req.Teacher_Quality=="High":
        data.append(0)
        data.append(0)
        data.append(1)
    else:
        logger.warning("Wrong Teacher_Quality")
        return HTTPException(status_code=422,detail="Wrong Teacher_Quality")
    
    if req.Family_Income=="Medium":
        data.append(1)
        data.append(0)
        data.append(0)
    elif req.Family_Income=="Low":
        data.append(0)
        data.append(1)
        data.append(0)
    elif req.Family_Income=="High":
        data.append(0)
        data.append(0)
        data.append(1)
    else:
        logger.warning("Wrong Family_Income")
        return HTTPException(status_code=422,detail="Wrong Family_Income")
    if req.Internet_Access:
        data.append(1)
        data.append(0)
    elif not req.Internet_Access:
        data.append(0)
        data.append(1)

    if req.Motivation_Level=="Medium":
        data.append(1)
        data.append(0)
        data.append(0)
    elif req.Motivation_Level=="Low":
        data.append(0)
        data.append(1)
        data.append(0)
    elif req.Motivation_Level=="High":
        data.append(0)
        data.append(0)
        data.append(1)
    else:
        logger.warning("Wrong Motivation_Level")
        return HTTPException(status_code=422,detail="Wrong Motivation_Level")
    if req.Extracurricular_Activities:
        data.append(1)
        data.append(0)
    elif not req.Extracurricular_Activities:
        data.append(0)
        data.append(1)
    if req.Access_to_Resources=="Medium":
        data.append(1)
        data.append(0)
        data.append(0)
    elif req.Access_to_Resources=="Low":
        data.append(0)
        data.append(1)
        data.append(0)
    elif req.Access_to_Resources=="High":
        data.append(0)
        data.append(0)
        data.append(1)
    else:
        logger.warning("Wrong Access_to_Resources")
        return HTTPException(status_code=422,detail="Wrong Access_to_Resources")
    

    if req.Parental_Involvement=="Medium":
        data.append(1)
        data.append(0)
        data.append(0)
    elif req.Parental_Involvement=="Low":
        data.append(0)
        data.append(1)
        data.append(0)
    elif req.Parental_Involvement=="High":
        data.append(0)
        data.append(0)
        data.append(1)
    else:
        logger.warning("Wrong Parental_Involment")
        return HTTPException(status_code=422,detail="Wrong Parental_Involment")
    data.append(req.Hours_Studied)
    data.append(req.Attendance)
    data.append(req.Sleep_Hours)
    data.append(req.Previous_Scores)
    data.append(req.Tutoring_Sessions)
    data.append(req.Physical_Activity)

    pred_score=model.predict([data,])
    return {"exam_score": pred_score[0]}