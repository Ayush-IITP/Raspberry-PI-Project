# Raspberry-PI-Project
Two Mini Project Using Raspberry PI

## MEMORY GAME 
This is a fun electronics game in which LED’s glow in certain pattern and if you are successful in repeating the same
pattern you move to the next level where one extra led will glow in comparison to previous state else you end up losing
the game. This file guides through installation and usage of the project.

#### Prerequisites
1. Install RPi.GPIO library for python:

	  $ sudo apt-get update
  
    $ sudo apt-get install rpi.gpio

#### Components Used
1. 5 LED's
2. 5 Resistors 220 ohms
3. 4 Push Buttons
4. PIR motion sensor
5. Jumper Wires
6. Raspberry Pi 3
7. Breadboard

#### Connections
##### Based on GPIO.BCM mode (use BCM pin numbers)
1. Connect pins 6,19,13,26 to ladder LEDS 1 to 4(Red,Yellow,Green,White) respectively.
2. Connect GPIO pins 4,27,17,22 to corresponding switches 1 to 4.
3. Connect GPIO pin 5 to PIR output probe.
4. Connect GPIO pins for ground and Vcc(5V).
5. Connect GPIO pin 9 to LED 5 which will remain on till the end of the script.(Reference LED)

#### Usage
1. Run python pimon.py for playing the game with switch.
2. Start the game with Motion Sensor using Motion and LED no.5 will glow till script has ended. 
3. LED's will glow in certain pattern and according to the level.
4. Now Input using switches/Push Buttons in the same way as LED's Glow (Memory).
5. If you are successful you will move to the next level else Script will ask you to play again or end game.


# BINARY TO GRAY CODE
In this part we are Converting the Binary Representation to Gray code Representation by glowing led in Gray code corresponding to its Binary Input.But,
the fun part is that we are doing this by an Android app made by us.

#### Prerequisites
On the raspberry pi, you should install these things.
1. Install RPi.GPIO library for python
	    
       $ sudo apt-get update
  
	     $ sudo apt-get install rpi.gpio
2. Install Wiring pi
	$ sudo apt-get update
  
        $ cd
        
        $ git clone git://git.drogon.net/wiringPi
3. Install apache and php

	      $ sudo apt-get install apache2 -y
	      $sudo apt-get install php5 libapache2-mod-php5 -y 
4. Remove the index.html file from /var/www/html by using this
	      
        $sudo rm index.html
5. Then you should have php script i.e index.php on your Pi in /var/www/html

Additional things .

2.An android phone.
3.Android studio on computer to put the app on the phone.

####Components Used
1. 4 LED's
2. 4 Resistors 220 ohms
3. Raspberry Pi 3
4. Breadboard
5. Jumper Wires

#### Connections
# Based on GPIO.BCM mode (use BCM pin numbers)0.
1. Connect pins 6,19,13,26 to ladder LEDS 1 to 4(Red,Yellow,Green,White) respectively.
2. Connect GPIO pins for ground.

Note : If you were successful in making the memory game mentioned above then you have no need to change any hardware connection ,just folllow the software part.

#### Usage 
1. Open the App.
2. Type the IP of your Pi on the Edit Text Field. (To check Pi ip use ifconfig)
3. Enter the Binary number whose gray code you want (ON-1/OFF-0).
4. Press Find gray button to turn on the LED's.
5. You will see the Gray code of your input on the circuit.
6. Use reset Button to turn off all the LED's.


