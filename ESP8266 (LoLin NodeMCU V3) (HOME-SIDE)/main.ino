//USING ARDUINO
//This code is just used for testing and proof of concept 

#include <PubSubClient.h>
#include <ESP8266WiFi.h>

#define led 2

void callback(char* topic, byte* payload, unsigned int length);

const char* ssid = "Android";
const char* password =  "123456789";

const char* mqttServer = "test.mosquitto.org";
const int mqttPort = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

void setup()
{
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.println();

//Connect to wifi
  WiFi.begin(ssid, password); //Specify wifi name & password

  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());
// ********************************

//Connect to MQTT Broker
  client.setServer(mqttServer, mqttPort); //Set broker URL & port
  client.setCallback(callback);

  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
 
    if (client.connect("AliAmaim")) {
 
      Serial.println("Successfully Connected");  
 
    } else {
 
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);
 
    }
//**********************************

//Testing publishing
    client.publish("a000/office/temperature", "21");
//Testing subscribing
    client.subscribe("a000/office/light");

  }
  digitalWrite(led, HIGH);
}

//Called whenever a message arrives
void callback(char* topic, byte* payload, unsigned int length) {
 
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
 
  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  char ledState = (char)payload[0];
  if(ledState == '0')
  {
    digitalWrite(led, HIGH);
  }
  else if(ledState == '1')
  {
    digitalWrite(led, LOW);
  }
 
  Serial.println();
  Serial.println("-----------------------");
 
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("AliAmaim")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("a000/office/temperature", "30");
      // ... and resubscribe
      client.subscribe("a000/office/light");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void loop() 
{
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  delay(500);
}
