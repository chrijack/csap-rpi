#!/usr/bin/python
###########################################################################
#Filename      :relay_with_led.py
#Description   :control led with relay
#Author        :alan
#Website       :www.osoyoo.com
#Update        :2017/06/28
############################################################################

import RPi.GPIO as GPIO
import time

# set BCM_GPIO 17 as relay pin
RelayPin = 17

#print message at the begining ---custom function
def print_message():
    print ('|**********************************************|')
    print ('|                     Relay                    |')
    print ('|        -----------------------------------   |')
    print ('|        GPIO17 connected to relay control pin |')
    print ('|        led connected to relay NormalOpen pin |')
    print ('|        5V connected to relay COM pin         |')
    print ('|        Relay controls an led                 |')
    print ('|        -----------------------------------   |')
    print ('|                                              |')
    print ('|                                        OSOYOO|')
    print ('|**********************************************|\n')
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')
    print ('\n')

#setup function
def setup():
    GPIO.setwarnings(False)
    #set the gpio modes to BCM numbering
    GPIO.setmode(GPIO.BCM)
    #set RelayPin's mode to output,and initial level to LOW(0V)
    GPIO.setup(RelayPin,GPIO.OUT,initial=GPIO.LOW)

#main function
def main():
    #print info
    print_message()
    while True:
        print ('|******************|')
        print ('|  ...Relay closed |')
        print ('|******************|\n')

        #Closed
        GPIO.output(RelayPin,GPIO.LOW)
        time.sleep(1)

        print ('|*****************|')
        print ('|  Relay open...  |')
        print ('|*****************|\n')
        print ('')
        #Open
        GPIO.output(RelayPin,GPIO.HIGH)
        time.sleep(1)

#destroy function to clean up everything after the script has finished
def destroy():
    #turn off relay
    GPIO.output(RelayPin,GPIO.LOW)
    #release resource
    GPIO.cleanup()
#
# Script Execution:
if __name__ == '__main__':
    setup()
    try:
            main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        destroy()
