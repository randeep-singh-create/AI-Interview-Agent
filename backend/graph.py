from typing import TypedDict,List # 1.  state da schema define krn lei 1
from langchain_groq import ChatGroq  # 3
import os
from dotenv import load_dotenv

from langgraph.graph import END

load_dotenv()
api_key=os.getenv('GROQ_API_KEY')
llm=ChatGroq(model="llama-3.3-70b-versatile",api_key=api_key,temperature=0.3) # temp for creativity

class InterviewState(TypedDict):   # 2
    role:str
    experience:str
    question_no:int
    history:List[dict]
    current_question:str

def generate_question(state): # 4. nodes de vich state carry hundi h
    pry_qus="\n".join([item["question"] for item in state["history"]])
    prompt=f"""
Generate Interview Question Number{state["question_no"]}
Role:
{state["role"]}
Experience:
{state["experience"]}
Focus on:
-Python
-Machine Learning
-Deep Learning
-Generative AI
Previous Question:
{pry_qus}
Rules:
Do not repeat previous question
Return only Question
"""
    response=llm.invoke(prompt)
    state["current_question"]=response.content
    return state

from pydantic import BaseModel

class Evaluation(BaseModel): # output de formats llm is trha return krega
    score:int
    strength:List[str]
    weakness:List[str]
    feedback:str

class InterviewReport(BaseModel): # jdo v aci fastapi da endpoint tao output deae kriye ta specific format ch aaye
    overall_score:int
    grade:str
    strength: List[str]
    weakness: List[str]
    recommendation:str

evaluation_llm=llm.with_structured_output(Evaluation)
report_llm=llm.with_structured_output(InterviewReport)

def evaluate_answer(question,answer):
    prompt=f"""
You are a technical interviewer.
Question: 
{question}
Answer:
{answer}
Evaluate the answer.
Give:
1.Score out of 10
2.Strengths
3.Weaknesses
4.Feedback
"""
    result=evaluation_llm.invoke(prompt)
    return result.model_dump() # jehra class da object aaya hai oh vapis json bn jave, ta ke api endpoints de through pass ho ske

def generate_report(history):
    prompt=f"""
Interview History
{history}

Generate final interview report.
Return:
-overall score (integer out of 20)
-grade
-strength (list of at least 3 strengths)
-weakness (list of at least 3 weaknesses)
-hiring recommendation

Do not leave any field empty.
"""
    result=report_llm.invoke(prompt)
    return result.model_dump()

from langgraph.graph import StateGraph

builder=StateGraph(InterviewState)
builder.add_node("generate_question",generate_question)
builder.set_entry_point("generate_question")
builder.add_edge("generate_question", END)
graph=builder.compile()


