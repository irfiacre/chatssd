from src.agent import handleAgentResponse
from src.utils import getCountry

def handleUssdConversation(session_id: str, serviceCode: str, phone_number:str, text:str, network_code: str) -> str:
    """
    This is a method to handle USSD code only
    """
    country = getCountry(phoneNumber=phone_number)
    response = ""
    if text == '':
      # This is the first request. Note how we start the response with CON
      response  = "Welcome to ChatSSD (choose language) \n"
      response += "1. English (Recommended) \n"
      response += "2. Kinyarwanda" + network_code + serviceCode

    elif text == '1':
        # English agent
        response = "English Agent"
        # response = handleAgentResponse()
    elif text == '2':
        # This is a terminal request. Note how we start the response with END
        response = "Kinyarwanda Agent" + phone_number

    elif text:
        response = handleAgentResponse(question=text, country=country)

    else:
        response = "END Invalid choice"

    return str(response)
