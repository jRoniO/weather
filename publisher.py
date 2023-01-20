import paho.mqtt.client as mqtt
import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

#callback för connect
def client_on_connect(client, data, flags, return_code):
   if return_code == 1:
      print("failed to connect :(")
   else:
      print("connected :)")
   return

publisherClient = mqtt.Client()
publisherClient.on_connect = client_on_connect

publisherClient.connect("broker.hivemq.com", 1883, 60)
if not publisherClient.is_connected():
   publisherClient.reconnect()

publisherClient.loop_start()

i = 0

while True:
   temperature = str(sensor.get_temperature())
   avrundning = temperature[0:4]
   #print('The temperature is %s celsius' % avrundning)
   msg = publisherClient.publish(topic="yrgo/team2/temp", payload="The temperature is "+str(avrundning)+" celcius "+str(i), qos=1)
   msg.wait_for_publish()
   time.sleep(1)
   i += 1
   pass
