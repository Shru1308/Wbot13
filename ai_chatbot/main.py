# setting up backend using FastAPI 

# Third-party imports
import openai
from fastapi import FastAPI, Form, Depends
from decouple import config
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

# Internal imports
from models import Conversation, SessionLocal
from utils import send_message, logger


app = FastAPI()

# Setting OpenAI API client
openai.api_key = config("OPENAI_API_KEY")
whatsapp_number = config("TO_NUMBER")

# creating new db session
def get_db():
    try:
        db = SessionLocal()   # from models.py
        yield db
    finally:
        db.close()

@app.post("/message")
async def reply(Body: str = Form(), db: Session = Depends(get_db)):
    # Call the OpenAI API to generate text with GPT-3.5
    response = openai.Completion.create(
        engine="text-davinci-002",          # model used to generate response
        prompt=Body,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # generated text
    chat_response = response.choices[0].text.strip()

    # Store the conversation in db
    try:
        conversation = Conversation(
            sender=whatsapp_number,
            message=Body,
            response=chat_response
            )
        db.add(conversation)
        db.commit()
        logger.info(f"Conversation #{conversation.id} stored in database")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error storing conversation in database: {e}")
    send_message(whatsapp_number, chat_response)      # utils.py
    return ""
