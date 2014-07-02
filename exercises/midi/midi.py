
## Original code (pygame example): https://bitbucket.org/pygame/pygame/src/25e3f2cee879/examples/midi.py
# Is also found in the local installation at Python27/Lib/site-packages/pygame/examples/midi.py

import pygame
from pygame import midi
import time, sys

def main():
    pass
    

pygame.init()
midi.init()

print "Devices:", midi.get_count()
out_device = midi.get_default_output_id()

print "Uses:", out_device

output = midi.Output( out_device )

GRAND_PIANO = 0
CHURCH_ORGAN = 19

try:
    output.set_instrument( CHURCH_ORGAN )
    output.note_on( 64, 100 )
    time.sleep( 1 )
    output.note_off( 64, 0 )
finally:
    del output
    midi.quit()
