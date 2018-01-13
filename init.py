from sense_hat import SenseHat
from time import sleep
from lib.weather_icons import rain_cloud_display

sense = SenseHat()

# init
sense.clear()
sense.set_rotation(180)

# get Sense HAT temp
temperature = sense.get_temperature()
# sense.show_message(str(round(temp)) + 'C')

sense.set_pixels(rain_cloud_display())

# Display image on pixel screen
# sense.load_image('/home/pi/Desktop/bullet.gif')

# sense.clear()
