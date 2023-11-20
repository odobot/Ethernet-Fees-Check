from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load fingerprint ID to name mappings from a file
file_path = 'D:\WORKSPACE\EEE Fees Check\Server/fingerprint_data.json'
with open(file_path) as f:
    fingerprint_data = json.load(f)

@app.route('/get_fingerprint_data', methods=['POST'])
def receive_fingerprint_id():
    # Check if the request contains form data or JSON data
    if 'fingerprint_id' in request.form:
        fingerprint_id = request.form['fingerprint_id']
    elif request.is_json and 'fingerprint_id' in request.json:
        fingerprint_id = request.json['fingerprint_id']
    else:
        return jsonify({'error': 'Invalid request'})

    print("Received fingerprint ID:", fingerprint_id)

    # Lookup name based on the received fingerprint ID
    if fingerprint_id in fingerprint_data:
        name = fingerprint_data[fingerprint_id]
        response_data = {'success': True, 'details': f"Details for ID {fingerprint_id}: Name - {name}"}
    else:
        response_data = {'success': False, 'details': f"No details found for ID {fingerprint_id}"}

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
