
# Original code (pygame example): https://bitbucket.org/pygame/pygame/src/25e3f2cee879/examples/midi.py
# Is also found in the local installation at Python27/Lib/site-packages/pygame/examples/midi.py

# Object-oriented implementation of MIDI Keyboard exercise

import pygame
from pygame import midi
from pygame.locals import *
import time, sys

# Instruments at http://www.skoogmusic.com/manual/manual1.1/Skoog-Window/navigation/MIDI-Tab/index
GRAND_PIANO = 0
CHURCH_ORGAN = 19
STEEL_GUITAR_AUCOUSTIC = 25

instrument = GRAND_PIANO

class Keyboard:
    """Class representing the MIDI keyboard."""
    def __init__(self, out_device, instrument=GRAND_PIANO, start_note=53):
        key_dictionary = {}
        
        keys = [K_TAB, K_1, K_q, K_2, K_w, K_3, K_e,
                K_r, K_5, K_t, K_6, K_y, K_u, K_8, K_i, K_9, K_o, K_0, K_p]
        
        i = start_note
        for k in keys:
            key_dictionary[k] = i
            i = i+1
        
        self.key_dictionary = key_dictionary
        self.instrument = instrument
        
        self.out = midi.Output( out_device )
        self.out.set_instrument( instrument )
        
        self.volume = 100
        self.octave = 0
    
    def play(self, key):
        """Pressed down this key: start playing note."""
        try:
            note = self.key_dictionary[key]
            self.out.note_on(note + 12*self.octave, self.volume)
        except KeyError:
            pass
    
    def stop(self, key):
        """Stopped pressing down this key: stop playing note."""
        try:
            note = self.key_dictionary[key]
            self.out.note_off(note + 12*self.octave, 0)
        except KeyError:
            pass
        
    def incr_octave(self):
        """Increase octave (+12)"""
        self.octave = self.octave + 1
        
    def decr_octave(self):
        """Decrease octave (-12)"""
        self.octave = self.octave - 1
    
    def incr_volume(self):
        """Increase volume (+5). Max == 125"""
        self.volume = self.volume + 5
        if self.volume > 125:
            self.volume = 125
        print "Volume", self.volume
        
    def decr_volume(self):
        """Decrease volume (-5). Min == 0"""
        self.volume = self.volume - 5
        if self.volume < 0:
            self.volume = 0
        print "Volume", self.volume
    
    def incr_instrument(self):
        """Change instrument (+1)"""
        self.instrument = (self.instrument + 1)%128
        self.out.set_instrument(self.instrument)
        print "Instrument", self.instrument
    
    def decr_instrument(self):
        """Change instrument (-1)"""
        self.instrument = (self.instrument - 1)%128
        self.out.set_instrument(self.instrument)
        print "Instrument", self.instrument

def help():
    """Help function."""
    print """
-------------------------------------
# Midi keyboard.

White keys are TAB to P. Black keys are on the numbers. Middle C is found on 'r'.

Increase/decrease octave: 'z'/'x'
Change instrument: 'c'/'v'
Increase/decrease volume: 'b'/'n'

Press 'h' to see this help again.
-------------------------------------"""

def io_loop(keyboard):
    """Main program loop. Handles IO."""
    help()
    while 1:
            e = pygame.event.wait()
            
            if e.type == pygame.QUIT:
                break
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    break
                elif e.key == K_h or e.key == K_F1:
                    help()
                elif e.key == pygame.K_z:
                    keyboard.decr_octave()
                elif e.key == pygame.K_x:
                    keyboard.incr_octave()
                elif e.key == K_c:
                    keyboard.decr_instrument()
                elif e.key == K_v:
                    keyboard.incr_instrument()
                elif e.key == K_b:
                    keyboard.decr_volume()
                elif e.key == K_n:
                    keyboard.incr_volume()
                else:
                    keyboard.play(e.key)
            elif e.type == pygame.KEYUP:
                keyboard.stop(e.key)


def main():
    """Initiates program and loop."""
    pygame.init()
    midi.init()

    print "Number of MIDI devices:", midi.get_count()
    if midi.get_count() == 0:
        print "No MIDI devices detected :P"
        return
    
    out_device = midi.get_default_output_id()
    print "Uses device no:", out_device
    keyboard = Keyboard(out_device, instrument)
    
    try:
        screen = pygame.display.set_mode([250,80])
        screen.fill((0,0,0))
        pygame.display.set_caption("MIDI Keyboard")
        pygame.display.flip()
        
        io_loop(keyboard)
        
    finally:
        del keyboard
        midi.quit()

main()