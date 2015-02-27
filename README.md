# Is_mouse_button_pressed
Cheap and simple solution to power off your linux box using usb mouse button. 

Python program to check if left mouse button pressed, if yes then power off. 
This is for embeded linux systems, without onboard buttons or keyboard, but you wants to shutdown with proper way.
Cheap and simple solution: use an usb mouse button to power off your linux box.

Connect a mouse to your linux box. If /dev/input/mouse is exist then run this program and when left mosue button pressed program will issue "poweroff" linux command.

