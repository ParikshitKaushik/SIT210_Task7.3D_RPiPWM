import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
Trigger = 17
Echo = 18
Buzzer = 2
GPIO.setup(Trigger, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
GPIO.setup(Buzzer, GPIO.OUT)
pwm = GPIO.PWM(Buzzer, 1000)
pwm.start(0)
duty_cycle = 0

def getDistance():
    GPIO.output(Trigger, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(Trigger, GPIO.LOW)

    while GPIO.input(Echo) == False:
        startTime = time.time()

    while GPIO.input(Echo) == True:
        finishTime = time.time()

    totalTime = finishTime - startTime
    distance = (totalTime * 34300) / 2

    return distance

try:
    while True:
        distance = getDistance()
        print(distance)
        
        if distance > 100:
            distance = 100

        if distance < 0:
            distance = 0

        if distance >= 100:
            pwm.ChangeDutyCycle(0)  
        else:
            duty_cycle = 100 - (distance / 100) * 100
            pwm.ChangeDutyCycle(duty_cycle)

        print(f"Distance: {distance} cm, Duty Cycle: {duty_cycle}%")

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()