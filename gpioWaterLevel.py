import RPi.GPIO as GPIO

print "water sensor start"

#GPIO.VERSION
#set up GPIO using BCM numbering
# BCM matches the numbers on the adafruit breakout

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(18, GPIO.IN)

waterSensor = GPIO.input(24)
print(waterSensor)

GPIO.cleanup()

print "water sensor finish"
