#Play Pi Wireless

##A wireless controller for [Play Pi](https://github.com/fredley/play-pi) that uses a [Xino RF](http://cpc.farnell.com/ciseco/xino-rf/arduino-uno-board-with-rf-transceiver/dp/SC13290) and [Slice of Radio](http://shop.ciseco.co.uk/slice-of-radio-wireless-rf-transciever-for-the-raspberry-pi/), as available in the [Raspberry Pi Wireless Inventor's Kit](http://shop.ciseco.co.uk/raswik/).

These files will allow you to create a wireless controller for your raspberry pi, that can be battery controlled or plugged in anywhere to allow basic music playing functionality at the touch of a button. This project is set up with three functions: Play/Pause, Stop, and Jazz - which will play a certain playlist of your choosing (Jazz optional).

##Instructions

* Follow all of the instructions to install Play Pi

* Power off the Pi, attach the Slice of Radio, reboot

* Set up your serial port using `sudo pip install pyserial`, and editing the following two files:  
  /boot/cmdline.txt should be changed to `dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 rootwait`  
  in /etc/inittab comment out the following line: `#2:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100`  
  add the pi user to the dialout group: `sudo usermod -a -G dialout pi`

* Load the playpi.ino sketch onto the Xino RF by whatever means you like.

* Wire the three buttons to D2, D3 and D4, and an LED to D6

* On the pi, fire up a screen and run `./wireless.py`
 
* You should see feedback when buttons are pressed on the wireless board, and the music should be controlled accordingly!

* Edit wireless.py so that the JAZZ button points to your favourite playlist  
