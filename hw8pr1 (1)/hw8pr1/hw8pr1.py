# hw8pr1.py
# Lab 8
#
# Name:
#

# keep this import line...
from cs5png3 import *


#
# a test function...
#
def test_fun():
    """ algorithmic image-creation one pixel at a time...
        this is a test function: it should output
        an image named test.png in the same directory
    """
    im = PNGImage(300,200)  # creates an image of width=300, height = 200

    # Nested loops!
    for r in range(200):  # loops over the rows with runner-variable r
        for c in range(300):  # loops over the cols with c
            if  c == r:   
                im.plotPoint( c, r, (255,0,0))
            #else:
            #    im.plotPoint( c, r, (255,0,0))
                
    im.saveFile()

#
# start your Lab 8 functions here:
#
def mult(c, n):
    """ mult uses only a loop and addition 
         to multiply c by the positive integer n
    """
    result = 0
    for i in range(n):
        # update the value of result here in the loopdef mult(c, n):
        result += c
    return result

def update(c, n):
    """ update starts with z=0 and runs z = z**2 + c
         for a total of n times. It returns the final z. 
    """
    z = 0
    for i in range(n):
        z = z**2 + c
    return z

def inMSet(c, n):
    """ inMSet accepts
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step
        Then, it returns
            False as soon as abs(z) gets larger than 2
            True if abs(z) never gets larger than 2 (for n iterations)"""
    z = 0
    for i in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

def weWantThisPixel(col, row):
    """ a function that returns True if we want
         the pixel at col, row and False otherwise
    """
    if col%10 == 0  and  row%10 == 0:
        return True
    else:
        return False

def test():
    """ a function to demonstrate how
        to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # create a loop in order to draw some pixels
    
    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row):
                image.plotPoint(col, row)

    # we looped through every image pixel; we now write the file

    image.saveFile()

def scale(pix, pixelMax, floatMin, floatMax):
    """ scale accepts
            pix, the CURRENT pixel column (or row)
            pixMax, the total # of pixel columns
            floatMin, the min floating-point value
            floatMax, the max floating-point value
        scale returns the floating-point value that
            corresponds to pix
    """
    if pix == 0:
        return floatMin
    elif pix == floatMax:
        return floatMax
    else:
        r = floatMax - floatMin
        s = pix / pixelMax
        return (r*s) + floatMin

def mset():
    """ creates a 300x200 image of the Mandelbrot set
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    numiter = 25
    xmin = -2.0
    xmax = 1.0
    ymin = -1.0
    ymax = 1.0

    # create a loop in order to draw some pixels
    
    for col in range(width):
        for row in range(height):
            # here is where you will need
            # to create the complex number, c!
            # Use scale twice:
            #   once to create the real part of c (x)
            #   once to create the imag. part of c (y)
            # THEN, test if it's in the M. Set:
            x = scale(col, width, xmin, xmax)
            y = scale(row, height, ymin, ymax)
            c = x + y*1j
            if inMSet(c, numiter):
                image.plotPoint(col, row)

    # we looped through every image pixel; we now write the file
    image.saveFile()
        



