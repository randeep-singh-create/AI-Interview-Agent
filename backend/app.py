
from fastapi import FastAPI
import json

from pydantic import BaseModel
from requests_toolbelt import sessions

# to store in the database
from database import SessionLocal
from model import Interview

from graph import *
sessions={}

app = FastAPI()

class StartRequest(BaseModel):
    name:str
    role:str
    experience:str


@app.post("/start")
def start(data:StartRequest):
    state={
        "role":data.role,
        "experience":data.experience,
        "question_no":1,
        "history":[],
        "current_question":""
    }
    result=graph.invoke(state)
    sessions[data.name] = result
    state["current_question"] = result.get("current_question")
    print("session")
    return {"question":state["current_question"]}


class AnswerRequest(BaseModel):
    name:str
    answer:str

@app.post("/answer")
def answer(req:AnswerRequest):
    if req.name not in sessions:
        sessions[req.name]={}
        return {"error":"invalid candidate"}
    session=sessions[req.name]
    evaluation =evaluate_answer(session["current_question"], req.answer)
    session["history"].append({
        "question":session["current_question"],
        "answer":req.answer,
        "evaluation":evaluation
    })
    if session["question_no"]>=2:
        report=generate_report(session["history"])

        db=SessionLocal()
        interview=Interview(Candidate_Name=req.name,Role=session["role"],Report=json.dumps(report))

        db.add(interview)
        db.commit()
        db.close()
        del sessions[req.name]
        return{"completed":True,"report":report}
    session["question_no"]+=1
    next_state={
        "role":session["role"],
        "experience":session["experience"],
        "question_no":session["question_no"],
        "history":session["history"],
        "current_question":""
    }

    result=graph.invoke(next_state)
    session["current_question"]=result.get("current_question")
    return {"completed":False,
            "question_no":session["question_no"],
            "evaluation":evaluation,
            "next_question":session["current_question"]}

