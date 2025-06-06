from flask import Flask, request

app = Flask(__name__)

@app.route('/shipment/callback', methods=['POST'])
def shipment_callback():
    data = request.json
    print("Received Webhook Data:", data)
    return '', 200

if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

