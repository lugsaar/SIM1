import os
import json
import time
import RPi.GPIO as GPIO
import pigpio # start the daemon with sudo pigpio

# start with - sudo pigpiod - the daemon zto address the servos

# https://github.com/rm-hull/luma.examples/blob/master/examples/demo.py
from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, sh1107, ws0010
#from PIL import ImageDraw


# rev.1 users set port=0
# substitute spi(device=0, port=0) below if using that interface
# substitute bitbang_6800(RS=7, E=8, PINS=[25,24,23,27]) below if using that interface
serial = i2c(port=1, address=0x3C)

# substitute ssd1331(...) or sh1106(...) below if using that device
device = sh1106(serial)

#    device.hide()
#    time.sleep(0.5)
#    device.show()

servoPINArm = 12
servoPINPan = 13

pwm = pigpio.pi()
pwm.set_mode(servoPINArm,pigpio.OUTPUT)
pwm.set_mode(servoPINPan,pigpio.OUTPUT)
pwm.set_PWM_frequency(servoPINArm, 50)
pwm.set_PWM_frequency(servoPINPan, 50)

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(servoPINArm, GPIO.OUT)
#GPIO.setup(servoPINPan, GPIO.OUT)



#pArm = GPIO.PWM(servoPINArm, 50) # GPIO 23 als PWM mit 50Hz
#pArm.start(7.5) # Initialisierung auf Mitte = 90 Grad
#dutycycleArmOld = 7.5      

# 0 degres = 500, 90 degres = 1500, 180 degres = 2500
pwm.set_servo_pulsewidth(servoPINArm, 1500) #90 degres
pwm.set_servo_pulsewidth(servoPINPan, 1500) #90 degres

#pPan = GPIO.PWM(servoPINPan, 50) # GPIO 24 als PWM mit 50Hz
#pPan.start(7.5) # Initialisierung auf Mitte = 90 Grad
dutycyclePanOld = 1500
dutycycleArmOld = 1500 





def ServoArm(start, ziel):
  #round (ziel, 2)
  if start < ziel:
      while start < ziel:
          start = start + 11.11 # 11,11 = 1 degres
          #round (start, 2)
          #pArm.ChangeDutyCycle(start)
          pwm.set_servo_pulsewidth(servoPINArm, start) # 
          time.sleep(0.02)
          #print("Arm1 ", start, " -> ", ziel)
          
  elif start > ziel:
      while start > ziel:
          start = start - 11.11
          #round (start, 2)
          pwm.set_servo_pulsewidth(servoPINArm, start)
          #pArm.ChangeDutyCycle(start)
          time.sleep(0.02)
          #print("Arm2 ", start, " -> ", ziel)
          

 

  
def ServoPan(start, ziel):
  #round (ziel, 2)
  if start < ziel:
      while start < ziel:
          start = start + 11.11
          #round (start, 2)
          pwm.set_servo_pulsewidth(servoPINPan, start)
          #pPan.ChangeDutyCycle(start)
          time.sleep(0.02)
          #print("Pan1 ", start, " -> ", ziel)
  elif start > ziel:
      while start > ziel:
          start = start - 11.11
          #round (start, 2)
          #pPan.ChangeDutyCycle(start)
          pwm.set_servo_pulsewidth(servoPINPan, start)
          time.sleep(0.02)
          #print("Pan2 ", start, " -> ", ziel
          
  # turning off servo        
  #pwm.set_PWM_dutycycle(servoPINPan, 0)
  #pwm.set_PWM_frequency(servoPINPan, 0)
          



#take json file
with open('sim1_theatre_file_wakeup.json', 'r') as read_file:
    
    data = json.load(read_file)


for chunks in data['chunks']:
    
    servoArmLeft = chunks['servoArmLeft']
    dutycycle = 1500 + 11.11 * servoArmLeft
    #dutycycle = round((servoArmLeft+90)*0.05555+2.5, 2)
    
    ServoArm(dutycycleArmOld, dutycycle)
    dutycycleArmOld =dutycycle
    
    servoPan = chunks['servoPan']
    #dutycycle = round((servoPan+90)*0.05555+2.5, 2)
    dutycycle = 1500 + 11.11 * servoPan
    
    ServoPan(dutycyclePanOld, dutycycle)
    dutycyclePanOld= dutycycle
    #pPan.ChangeDutyCycle(0)
    
    
    with canvas(device) as draw:
        draw.rectangle((2,22,126,42),outline=0, fill="white")
    sleeptime = chunks['timer']    
    time.sleep(sleeptime)
    string = chunks['speakText']
    print(string)
    
    mouth = chunks['mouth']
    if mouth == "speak":
        with canvas(device) as draw:
            draw.rectangle((10,17,118,57),outline=0, fill="white")
    
    
# sim1 speaks
        os.system('espeak -s 120 -vmb-us1 "{}"'.format(string))

        with canvas(device) as draw:
            draw.rectangle((2,22,126,42),outline=0, fill="white")

        time.sleep(sleeptime)
