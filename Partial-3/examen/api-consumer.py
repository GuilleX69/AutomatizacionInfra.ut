import requests

# URL of your Flask server
url = 'http://localhost:5000/send-whatsapp'

# Data to send in the request
data = {
    'phone_number': '+524445149668',
    'message': 'Hola'
}

# Send POST request
response = requests.post(url, json=data)

# Check response status
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Error:", response.json()['message'])
