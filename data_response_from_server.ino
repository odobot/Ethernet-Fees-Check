#include <ArduinoHttpClient.h>
#include <Ethernet.h>
#include <SPI.h>

// Replace these variables with your server details
#define SERVER_IP "172.16.59.111"
#define SERVER_PORT 5000
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

EthernetClient client;

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    while (1);
  }

  delay(1000);
  Serial.println("Arduino is ready to send data to the server.");
}

void loop() {
  // Read data from Serial Monitor
  Serial.println("Enter data to send to the server:");
  while (!Serial.available()) {
    // Wait for user input
  }

  String dataToSend = Serial.readStringUntil('\n');
  
  // Send data to the server
  sendDataToServer(dataToSend);

  // Wait for server response
  waitForServerResponse();
}

void sendDataToServer(String data) {
  Serial.print("Sending data to server: ");
  Serial.println(data);

  if (client.connect(SERVER_IP, SERVER_PORT)) {
    Serial.println("Connected to server");
    
    // Send the data to the server
    client.print(data);
    client.println();
  } else {
    Serial.println("Connection failed");
    return;
  }
}

void waitForServerResponse() {
  Serial.println("Waiting for server response...");

  while (client.connected() && !client.available()) {
    // Wait for data from the server
  }

  while (client.available()) {
    char c = client.read();
    Serial.write(c);
  }

  client.stop();
  Serial.println("\nServer response received.");
}
