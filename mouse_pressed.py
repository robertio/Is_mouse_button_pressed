#!/usr/bin/env python
#########################
# shutdown linux system if left mouse button pressed. Reboot for right button.
# https://github.com/robertio/Is_mouse_button_pressed/edit/master/README.md
# put this file as /usr/local/bin/mouse_pressed.py
##########################
import struct,os
file = open( "/dev/input/mice", "rb" );
def getMouseEvent():
  buf = file.read(3);
  button = ord( buf[0] );
  bLeft = button & 0x1;
  bMiddle = ( button & 0x4 ) > 0;
  bRight = ( button & 0x2 ) > 0;
  x,y = struct.unpack( "bb", buf[1:] );
  if int(bLeft) != 0:
   os.system("shutdown -h now")
  elif int(bRight) != 0:
   os.system("shutdown -r now")
while( 1 ):
  getMouseEvent();
file.close();
