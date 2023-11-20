from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_data', methods=['POST'])
def receive_data():
    # Check if the request contains the expected data
    if 'arduino_data' not in request.form:
        return 'Invalid request'

    arduino_data = request.form['arduino_data']
    print("Received data from Arduino:", arduino_data)

    # Process the Arduino data and print different outputs based on different conditions
    if arduino_data == 'LED_ON':
        print("Turning on the LED!")
        # Add code to control your LED here

    elif arduino_data == 'LED_OFF':
        print("Turning off the LED!")
        # Add code to turn off your LED here

    elif arduino_data.startswith('SENSOR_DATA'):
        # Assuming SENSOR_DATA format: SENSOR_DATA=temperature:22.5&humidity:40.0
        sensor_data = arduino_data.split('=')[1]
        sensor_values = dict(pair.split(':') for pair in sensor_data.split('&'))
        print("Received sensor data - Temperature:", sensor_values.get('temperature'), "Humidity:", sensor_values.get('humidity'))

    else:
        print("Unknown command:", arduino_data)

    return 'Data received successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
