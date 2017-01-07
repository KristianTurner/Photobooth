
import time
import RPi.GPIO as GPIO  ## Import GPIO library
import picamera
import pysftp
from time import gmtime, strftime


led_pin = 7
btn_pin = 23


# SFTP setup
cnopts2 = pysftp.CnOpts()
cnopts2.hostkeys = None

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT) # LED
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(led_pin, True) #for some reason the pin turns on at the beginning of the program. Why?

#Will toggle the LED status#
def photo_start():
    GPIO.output(7, False) # Turn on GPIO pin 7    
    time.sleep(0.75)
    GPIO.output(7, True) # Turn on GPIO pin 7    
    time.sleep(0.75)
    GPIO.output(7, False) # Turn on GPIO pin 7    
    time.sleep(0.75)
    GPIO.output(7, True) # Turn on GPIO pin 7    
    time.sleep(0.75)
    GPIO.output(7, False) # Turn on GPIO pin 7  
      
    file_name = "newyears3"
    file_name += strftime("%H-%M-%S", gmtime())
    file_name += '.jpg'
    print('Taking photo')

    with picamera.PiCamera() as camera:
        camera.resolution = (1920, 1080)
        #camera.rotation = 180
        #camera.saturation = 100
        camera.capture(file_name)
    print('Photo done')
    print('Uploading...')
    with pysftp.Connection(
        'YOURADDRESS',
        username='YOURUSER',
        password='YOURPASSWORD',
        cnopts=cnopts2) as sftp:
        with sftp.cd('/web/newyears/media'):
            sftp.put(file_name)
        print('Succes')
    sftp.close()
    GPIO.output(7, True) # Turn on GPIO pin 7

try:
    while True:
        GPIO.wait_for_edge(btn_pin, GPIO.FALLING)
        print("Button pressed")
        photo_start()
        time.sleep(0.2)
except (KeyboardInterrupt, SystemExit):
    GPIO.cleanup()
    raise
