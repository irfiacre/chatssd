# works with both python 2 and 3
from __future__ import print_function

API_KEY="atsk_588b81f54875e57a3357b98a1ad1f45ffb40b8ad295a3b7ccfb96830613743c55567bc53"
USERNAME="irfiacre"

import africastalking

class VOICE:
    def __init__(self):
		# Set your app credentials
        self.username = "YOUR_USERNAME"
        self.api_key = API_KEY
		# Initialize the SDK
        africastalking.initialize(self.username, self.api_key)
		# Get the voice service
        self.voice = africastalking.Voice

    def call(self):
        # Set your Africa's Talking phone number in international format
        callFrom = "+250786585608"
        # Set the numbers you want to call to in a comma-separated list
        callTo   = ["+250786585608"]
        try:
			# Make the call
            result = self.voice.call(callFrom, callTo)
            print (result)
        except Exception as e:
            print ("Encountered an error while making the call:%s" %str(e))

if __name__ == '__main__':
    VOICE().call()
