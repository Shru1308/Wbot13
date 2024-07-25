Build an AI chatbot with the OpenAI API that can engage with customers on WhatsApp. With this chatbot, you'll be able to provide customers with intelligent responses to their inquiries. 
This AI chatbot is a ChatGPT-like interface but on WhatsApp. Setting up the backend using FastAPI and SQLAlchemy to create a PostgreSQL database to store customers' conversations. 
Integrating Twilio's WhatsApp Messaging API, allowing customers to initiate conversations with the WhatsApp chatbot.

Prerequisites :
- Python 3.7+
- PostgreSQL 
- A Twilio account set up
- An OpenAI API key
- ngrok

Command to run the app : 
- uvicorn main:app --reload

 
 To host your app on a public server :
 - ngrok http 8000

