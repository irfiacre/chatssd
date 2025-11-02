from flask import Flask, request
from src.ussd import handleUssdConversation

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def index():
  return {"message": "Welcome to Chatssd", "status": "up"}

@app.route("/ussd", methods = ['POST'])
def ussd():
  session_id = request.values.get("sessionId", None)
  serviceCode = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  network_code = request.values.get("networkCode", None)
  text = request.values.get("text", "default")

  return handleUssdConversation(
     text=text,
     phone_number=phone_number,
     session_id=session_id,
     serviceCode=serviceCode,
     network_code=network_code
    )

if __name__ == '__main__':
    app.run(debug=True)
