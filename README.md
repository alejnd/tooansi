# TOOANSI 
### A Rest service to convert pngs into ansi color characters.
Tooansi is a rest endpoint to deliver png images and gives you plain text ansi encoded color
characters to make nice ascii art. Written in python using Flask
Supports 256 colors and alpha channel but your terminal must be capable of this (like gnome-terminal)

Usage example:

service start: python run.py 

send request: curl -F "file=@image.png"  localhost:5000/upload

 Have fun!