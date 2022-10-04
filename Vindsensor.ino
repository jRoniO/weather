/************************************************************************
 Seriell överföring initieras för att seriell kommunikation ska fungera.
*************************************************************************/
void setup()
{
  Serial.begin(9600); 
}
/********************************************************************************************************
 Data läses från analogPin (A0) och sparas som en float i variabeln sensorValue.
 Sensorns analoga värde omvandlas sedan till en spänning och sparas som en float i variabeln voltage.
**********************************************************************************************************/
void loop()
{
  float sensorValue = analogRead(A0); 
  float voltage = (sensorValue / 1023) * 5; 
  
/******************************************************************************************************************* 
  Vindhastigheten startar på 1m/s vid 0,4V med max 32,4m/s runt 2.
  Arduino har en inbyggd map() funktion, men map() fungerar inte för float, så vi har en enkel mapFloat() funktion.
  Mappningen sparas som en float i variabeln wind_speed.
  Därefter skrivs wind_speed ut.
*********************************************************************************************************************/
  float wind_speed = mapfloat(voltage, 0.4, 2, 0, 32.4);
  Serial.println(wind_speed);
  delay(100);
}
/***********************************************************************************
 Mapp funktionen används för att spara variabeln som en float.
************************************************************************************/
 float mapfloat(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
