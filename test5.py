import RPi.GPIO as GPIO

def button_callback(channel):
    print(channel)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Add event detection for each button
GPIO.add_event_detect(17, GPIO.RISING, callback=button_callback, bouncetime=500)
GPIO.add_event_detect(27, GPIO.RISING, callback=button_callback, bouncetime=500)
GPIO.add_event_detect(22, GPIO.RISING, callback=button_callback, bouncetime=500)
GPIO.add_event_detect(18, GPIO.RISING, callback=button_callback, bouncetime=500)
GPIO.add_event_detect(23, GPIO.RISING, callback=button_callback, bouncetime=500)
GPIO.add_event_detect(24, GPIO.RISING, callback=button_callback, bouncetime=500)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
