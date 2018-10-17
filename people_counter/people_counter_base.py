"""
--------------------------------------------------------------------------
People Counter
--------------------------------------------------------------------------
License:   
Copyright 2018 <Your Name>

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Use the HT16K33 Display and a button to create a digital people counter

Requirements:
  - Increment the counter by one each time the button is pressed
  - If button is held for more than 5s, reset the counter

"""
import time

import Adafruit_BBIO.GPIO as GPIO

import ht16k33_i2c as HT16K33


# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

BUTTON0                      = "P2_2"

RESET_TIME                   = 2.0


# ------------------------------------------------------------------------
# Main Tasks
# ------------------------------------------------------------------------

def setup():
    """Setup the hardware components."""
    
    # Initialize Display

    # Initialize Button

# End def


def task():
    """Execute the main program."""
    people_count                 = 0        # Number of people to be displayed
    button_press_time            = 0.0      # Time button was pressed (in seconds)
    
    while(1):

        # Wait for button press
        
        # Record time
        
        # Wait for button release
        
        # Compare time to increment or reset people_count
        
        # Update the display
        
# End def


def cleanup():
    """Cleanup the hardware components."""
    
    # Set Display to something fun to show program is complete
    HT16K33.display_set_digit(0, 13)        # "D"
    HT16K33.display_set_digit(1, 14)        # "E"
    HT16K33.display_set_digit(2, 10)        # "A"
    HT16K33.display_set_digit(3, 13)        # "D"
    
# End def


# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    setup()
    
    try:
        task()
    except KeyboardInterrupt:
        pass

    cleanup()
    print("Program Complete.")

