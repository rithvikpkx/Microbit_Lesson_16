from microbit import *

#16.2
import music
#Import music module

while True:
	#16.5
	if button_a.is_pressed():
    	music.stop()
	#If button a is pressed stop music, else move on
    
    	#16.6
    	if button_b.is_pressed():
        	break
    	#If button b is pressed break out of the loop, else move on
   	 
	#16.6    
	else:
    	x = accelerometer.get_x()
	#If neither buttons a or b on the microbit are pressed, get the value of x from the accelerometer
   	 
    	#16.6
    	freq = x + 1024
    	if freq < 10:
        	freq = 10
    	#The variable freq equals the value of x + 1024
		#If value of freq is less than 10, set freq to 10, else move on
   	 
    	#16.6
    	music.pitch(freq, -1) # ← New
    	#Set the pitch of the music to a frequency of value freq and for an infinite duration