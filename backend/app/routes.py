from fastapi import APIRouter
from app.openai_client import ask_bot
from pydantic import BaseModel


router = APIRouter()


class Bot(BaseModel):
    text: str



@router.post("api/chat") # endpoint 
async  def send_message(message: Bot):
    answer = await  ask_bot(message.text)
    return {"answer" , answer}
