
from fastapi import FastAPI, UploadFile, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import openai
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

openai.api_key = os.getenv("AZURE_OPENAI_KEY")
api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_DEPLOYMENT")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask_question(file: UploadFile, question: str = Form(...)):
    content = await file.read()
    context = content.decode()

    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    response = openai.ChatCompletion.create(
        engine=deployment,
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message["content"]
    return {"answer": answer}
