void setup()
{
  Serial.begin(9600); // Seriell överföring.
}
void loop()
{
  float sensorValue = analogRead(A0); // Väljer analog Pin på arduinon.
  float voltage = (sensorValue / 1023) * 5; // Läser sensorns analoga värde och omvandlar den till en spänning.
  
 /************************************************************************************************************************* 
  Vindhastigheten startar på 1m/s vid 0,4V med max 32,4m/s runt 2.
  Arduino har en inbyggd map() funktion, men map() fungerar inte för flöten, så vi har en enkel mapFloat() funktion.
 **************************************************************************************************************************/
  float wind_speed = mapfloat(voltage, 0.4, 2, 0, 32.4);
  Serial.println(wind_speed);
  delay(1000);
}
 float mapfloat(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
