#include <WiFi.h>
#include <WiFiUdp.h>

#define PIN_ANALOGICO_X 34
#define PIN_ANALOGICO_Y 35

// Datos de la red e.g., ssid = ("RED-WiFi" ) y password = "PASSWORD"
const char* ssid = "RED-WiFi";
const char* password = "PASSWORD";

// Datos del dispositivo receptor (e.g., la computadora)
const char* hostIP = "192.0.0.0"; // 
const int udpPort = 4210;

//Socket UDP
WiFiUDP udp;

void setup() {
  // Inicia comunicación serial para el monitor serial
  Serial.begin(115200);
  
  // Inicia WiFi
  WiFi.begin(ssid, password);
  Serial.print("Conectando a Wifi");
  
  //Espera hasta que se conecte bien a la red Wifi
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.print(".");
    }
    Serial.println("\nWiFi conectado. IP: "+ WiFi.localIP().toString());
}

void loop() {
  int valor_x = analogRead(PIN_ANALOGICO_X);
  int valor_y = analogRead(PIN_ANALOGICO_Y);
  float x = (float)valor_x / 4095.0;
  float y = (float)valor_y / 4095.0;
  
  // Formato: "x, y" ->"0.025, 0.364"
  String data = String(x)+ "," + String(y);
  
  // Formato JSON
  //String data = "{\"x\": " + String(x, 4) + ", \"y\": " + String(y, 4) + "}";
  
  udp.beginPacket(hostIP, udpPort);
  udp.print(data);
  udp.endPacket();
  delay(20);
}
