#include "funciones.h"

unsigned long previousMillis = 0;
const long interval = 5000;

void setup()
{
  setupProyecto();
}

void loop()
{
<<<<<<< Updated upstream
  //inicio();//Descomentar cuando esté todo armado y hecho

  sensorSumergible();
  TempHum();
  sendSerialRasp();
  // Esperamos 4 segundos entre medidas
  delay(4000);
=======
  unsigned long currentMillis = millis();
  int automatico= 0; //0 manual y 1 automático.
  
  //inicio();//Descomentar cuando esté todo armado y hecho
  if (currentMillis - previousMillis >= interval){
    previousMillis = currentMillis;
    sensorSumergible();
    TempHum();
  }
  
  sendSerialRasp();
  
  //Validar que si el sensor de temperatura sumergible baja a cierta temperatura encienda la resistencia por un tiempo para calentar el agua.
  //For the temperature and humidity sensor cause the sensor needs time to measure the data.

>>>>>>> Stashed changes
}

void serialEvent() {
  eventoSerial();
}
