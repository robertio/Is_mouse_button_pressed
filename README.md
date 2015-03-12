# Is_mouse_button_pressed?
<h1> Cheap and simple solution to power off your linux box when usb left mouse button pressed. </h1>

http://mousebuttonshutdown.blogspot.hu/2015/02/cheap-and-simple-solution-to-power-off.html

Python program to check if left mouse button pressed, if yes then power off. 
This is for embeded linux systems, without onboard buttons or keyboard, but you wants to shutdown with proper way.
Cheap and simple solution: use an usb mouse button to power off your linux box.

Connect a mouse to your linux box. If /dev/input/mouse is exist then run this program and when left mosue button pressed program will issue "poweroff" linux command.


<h1> Prerequsites: </h1>

<h2> 1. Install Python. </h2>
<pre>
apt-get install python
</pre>

<h2> 2. Download the python program. </h2>
<pre>
cd /usr/local/bin
wget --no-check-certificate https://raw.githubusercontent.com/robertio/Is_mouse_button_pressed/master/mouse_pressed.py
wget --no-check-certificate https://raw.githubusercontent.com/robertio/Is_mouse_button_pressed/master/midmousebutt.sh
chmod 755 mouse_pressed.py midmousebutt.sh 
</pre>

<h2> 3. Download shell script allow to run when system statup. </h2>
<pre>
cd /etc/init.d
wget --no-check-certificate https://raw.githubusercontent.com/robertio/Is_mouse_button_pressed/master/mouse_pressed.sh
chmod 755 mouse_pressed.sh
update-rc.d mouse_pressed.sh defaults
</pre>

<h2> 4. Start first time manually </h2>
<pre>
/etc/init.d/mouse_pressed.sh status         # first time will report error - 'casue not running.
/etc/init.d/mouse_pressed.sh start        # or reboot
</pre>

If LEFT mouse button pressed - shut down system

If RIGHT mouse button pressed - Reboots system

If MIDDLE mouse button pressed - run a midmousebutt.sh script in /usr/local/bin directory (actually plays music)

* source of python mouse handling : http://stackoverflow.com/questions/4855823/get-mouse-deltas-using-python-in-linux 
