# Mobile & Ubiquitous Computing - Team 9  
### Using Arduino Nano 33 BLE to classify movement to a mobile phone  

Team 9: 
<!-- Write your name followed by 2 spaces and then return -->
- Oliver Firmstone
- Samuel Lawal
- 

In this project, we have collated datasets for the 3 movement types: idle, walking, running. This was done using the **serialreader.py** file, reading the Arduino's accelerometer coordinates which are outputted every 20ms. After collecting 3000+ samples for each dataset, they were then used within our Google Colab page to develop a TinyML classifier which could then be uploaded back to the Arduino.

This meant that any new data from the accelerometer could be classified and communicated to the phone using Bluetooth Low Energy (BLE). We developed a Flutter app to display this classification. 
