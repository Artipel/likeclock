# likeclock

This repository contains files required to run AlfaZeta's 10 digit display. It has install.sh script that:

1.  Creates a clock.sh file that is an entry point for the service
2.  Adjusts service unit to this machine
3.  Copies config.json file to /boot partition. config.json is a configuration file for the display.
4.  Copies service unit to /etc/systemd/system
5.  Enables and starts unit

To run installation type sh `install.sh`
