from PIL import Image

#ANSI scape codes
SETBGCOLOR = "\x1b[48;2"
CRESET     = "\033[0m"


def convert (filename):
    ansibuff = ''
    img = Image.open(filename, 'r').convert("RGBA")
    pix_val = list(img.getdata())
    _, _, xmax, ymax = img.getbbox()
    
    for y in range(ymax):
        for x in range(xmax):
            r, g, b, a = img.getpixel((x,y))
            if a ==  0: ansibuff += '{0!s} '.format(CRESET)
            else: ansibuff += '{!s};{!s};{!s};{!s}m '.format(SETBGCOLOR, r, g, b)
        ansibuff += CRESET+'\n'

    return ansibuff