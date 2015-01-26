import RPi.GPIO as GPIO

#GPIO.VERSION
#set up GPIO using BCM numbering
# BCM matches the numbers on the adafruit breakout

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(18, GPIO.IN)

print(GPIO.input(24))

GPIO.cleanup()
