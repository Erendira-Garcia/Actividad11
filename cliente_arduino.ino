// Datos del dispositivo receptor (e.g., la computadora)
const char* hostIP = "192.0.0.0"; 
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
  int valor = 16;
  
  // Formato: "valor"
  String data = String(valor);
  udp.beginPacket(hostIP, udpPort);
  udp.print(data);
  udp.endPacket();
  delay(1000);
}
