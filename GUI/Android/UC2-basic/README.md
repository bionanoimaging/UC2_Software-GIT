# UC2 remote controller via the MQTT-protocol

This is the Android Remote Control for ***TheBox*** was on this [repository](https://github.com/ismenc/esp8266-mqtt-control) with an attached relay. This allows us to remote turn on any electric device.
<p align="center">
<img src="./images/Android_GUI.png" width="200" alt="">
</p>

You can enter the IP-address of the local MQTT-Broker (e.g. Mosquitto), then hit Go! It automatically subscribes to all topics necessary by the actuators in "TheBox". It gives basic control functions to the following parts:

- The S-Stage found [here](https://github.com/bionanoimaging/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_Z-STAGE_v2)
- The Z-Stage found [here](https://github.com/bionanoimaging/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_S-STAGE_v2)
- The LED-Array found [here](https://github.com/bionanoimaging/UC2-GIT/tree/master/CAD/ASSEMBLY_CUBE_LED_Matrix_v2)

## Diagram

The general control scheme looks like this:
<p align="center">
<img src="./images/MQTT_GUI.png" width="500" alt="">
</p>

## Code for ESP32
The code for the ESP32's in order to control the motors and LEDS can be found [here](./../../../HARDWARE_CONTROL/ESP32).

## Signed APK
The latest version of the signed **APK** of the app can be downloaded [here](./app/build/outputs/apk/debug/app-debug.apk)

## Tutorial to make it work

1. Install the free App **MQTT Broker App** from the [Play Store](https://play.google.com/store/apps/details?id=server.com.mqtt&hl=de)
2. Install the UC2 controler APP using this [link](./app/build/outputs/apk/debug/app-debug.apk)
3. Setup the WiFi-Acces Point (AP) on your Android Phone (Sometimes called wifi-sharing or Hotspot) under **Settings** -> **Tethering&mobile Hotspot** -> **WiFi Hotspot**
4. The settings should be the following: 
5. SSID: **Blynk**
6. Password: **12345678**
7. Start the Hotspot 
8. Open the **MQTT Broker App** and hit start 
9. A message "*mqtt>Broker URL - 0.0.0.0:1883*" appears -> Great! 
10. Open the **UC2 Controler APP** and enter the IP-address as *0.0.0.0* and hit **Go!**
11. A message which says **Connected** should appear 
12. All set! 

## Troubleshooting

- Close the app and restart it (really remove the panel from the task manager)

### MQTT-Commands sent externally

You can send the commands using 3rd party apps for debugging. The general topic-structure is: 
- ```/<S><INT3>/<DEV><INT2>/COMD```
with S=Setup, DEV=Device, COMD=Command (delimited by "+" sign) and INT3=3 integers, INT2=2 integers. A COMD is built by a ```<COMMANDSEQUENCE>+<VAL1>+<VAL2>+...+<VALn>```. Here are some examples:

- **Motor: Z-Stage**: ```/S013/MOT01/RECM DRVZ+-50```, *-100..100*
- **Motor: S-Stage**: ```/S013/MOT02/RECM DRVZ+-50```, *-100..100*
- **Fluo LED**: ```/S013/MOT01/RECM NA+10966```, *0..25600*
- **LED-Array**: ```/S013/LAR01/RECM NA+1```, *0,1,2,3,4*

The COMD ```STATS``` or ```ANNO``` are used for inter-device-communication and bug-fixing. 