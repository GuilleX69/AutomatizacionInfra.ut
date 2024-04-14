from flask import Flask, request, jsonify
import pywhatkit

app = Flask(__name__)

@app.route('/send-whatsapp', methods=['POST'])
def send_whatsapp_message():
    try:
        data = request.get_json()
        phone_number = data.get('phone_number')
        message = data.get('message')

        pywhatkit.sendwhatmsg_instantly(phone_number, message)

        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
