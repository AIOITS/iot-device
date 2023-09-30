import RPi.GPIO as GPIO

def button_callback(channel):
    print(channel)

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Add event detection for each button
GPIO.add_event_detect(26, GPIO.RISING, callback=button_callback, bouncetime=500)
GPIO.add_event_detect(19, GPIO.RISING, callback=button_callback, bouncetime=500)
GPIO.add_event_detect(13, GPIO.RISING, callback=button_callback, bouncetime=500)
GPIO.add_event_detect(12, GPIO.RISING, callback=button_callback, bouncetime=500)
GPIO.add_event_detect(9, GPIO.RISING, callback=button_callback, bouncetime=500)
GPIO.add_event_detect(11, GPIO.RISING, callback=button_callback, bouncetime=500)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
