# Is_mouse_button_pressed?
Cheap and simple solution to power off your linux box when usb mouse button pressed. 

Python program to check if left mouse button pressed, if yes then power off. 
This is for embeded linux systems, without onboard buttons or keyboard, but you wants to shutdown with proper way.
Cheap and simple solution: use an usb mouse button to power off your linux box.

Connect a mouse to your linux box. If /dev/input/mouse is exist then run this program and when left mosue button pressed program will issue "poweroff" linux command.


Prerequsites:

apt-get install python

cd /usr/local/bin

wget --no-check-certificate https://github.com/robertio/Is_mouse_button_pressed/blob/master/mouse_pressed.py

chmod 755 mouse_pressed.py

cd /etc/init.d

wget --no-check-certificate https://github.com/robertio/Is_mouse_button_pressed/blob/master/mouse_pressed.sh

chmod 755 mouse_pressed.sh

update-rc.d mouse_pressed.sh defaults

/etc/init.d/mouse_pressed.sh status         # first time will report error - 'casue not running.

/etc/init.d/mouse_pressed.sh start        # or reboot

If LEFT mouse button pressed - shut down system

If RIGHT mouse button pressed - Reboots system

* source of python mouse handling : http://stackoverflow.com/questions/4855823/get-mouse-deltas-using-python-in-linux 
