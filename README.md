# lumberjack_cheater
Simple Python script in order to beat score of 1000 on Telegram Gamebot's Lumberjack game.
This script uses the mss (multiple screenshots) library because it is quicker than using the Pillow and screencapture (macOS) counterparts.

## macOS
The current script is optimized for macOS. In order to run it off the bat set macOS resolution to the highest one possible (System Preferences > Displays) and open Telegram so that the window takes up all of the screen but without completely expanding it to full screen ("don't press the green button").

## Windows/Linux
If you want to run this script in Windows or a Linux distro you have to import the according mss module. The complete import command can be found [here](https://python-mss.readthedocs.io/usage.html#import).
