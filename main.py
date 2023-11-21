import sys
import getpass

# Twilio API SID
# TODO replace with environment variables
twilio_sid = ''

# Request Twilio Key from user
twilio_key_input = getpass.getpass("Enter Twilio Auth Token: ")

# Sanity check input
if len(twilio_key_input) != 32:
    sys.exit("Invalid Auth Key format")
else:
    print("Key is set")