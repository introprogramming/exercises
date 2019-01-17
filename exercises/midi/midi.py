
## Original code (pygame example): https://bitbucket.org/pygame/pygame/src/25e3f2cee879/examples/midi.py
# Is also found in the local installation at Python27/Lib/site-packages/pygame/examples/midi.py

import pygame
from pygame import midi
from pygame.locals import *
import time, sys

# Instruments at http://www.skoogmusic.com/manual/manual1.1/Skoog-Window/navigation/MIDI-Tab/index
GRAND_PIANO = 0
CHURCH_ORGAN = 19
STEEL_GUITAR_AUCOUSTIC = 25

instrument = GRAND_PIANO


def init_keyboard(start_note):
    """Creates a mapping from keyboard keys to music notes."""
    keyboard = {}
    
    keys = [K_TAB, K_1, K_q, K_2, K_w, K_3, K_e,
            K_r, K_5, K_t, K_6, K_y, K_u, K_8, K_i, K_9, K_o, K_0, K_p]
    
    i = start_note
    for k in keys:
        keyboard[k] = i
        i = i+1
    return keyboard

def io_loop(keyboard, output, instrument=GRAND_PIANO):
    """Main program loop. Handles IO."""
    octave = 0
    
    while 1:
            e = pygame.event.wait()
            
            if e.type == pygame.QUIT:
                break
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    break
                elif e.key == pygame.K_z:
                    octave = octave - 1
                elif e.key == pygame.K_x:
                    octave = octave + 1
                elif e.key == K_c:
                    instrument = (instrument - 1)%128
                    output.set_instrument( instrument )
                elif e.key == K_v:
                    instrument = (instrument + 1)%128
                    output.set_instrument( instrument )
                else:
                    try:
                        note = keyboard[e.key]
                        output.note_on(note + 12*octave, 100)
                    except KeyError:
                        pass
            elif e.type == pygame.KEYUP:
                try:
                    note = keyboard[e.key]
                    output.note_off(note + 12*octave, 0)
                except KeyError:
                    pass


def main():
    """Initiates program and loop."""
    pygame.init()
    midi.init()

    print("Number of MIDI devices:", midi.get_count())
    if midi.get_count() == 0:
        print("No MIDI devices detected :P")
        return
    
    out_device = midi.get_default_output_id()
    if out_device == -1:
        print("No MIDI output device detected :P")
        return
    
    print("Uses device no:", out_device)
    try:
        output = midi.Output( out_device )
        output.set_instrument( instrument )
        keyboard = init_keyboard(53)
        
        screen = pygame.display.set_mode([250,80])
        screen.fill((0,0,0))
        pygame.display.set_caption("MIDI Keyboard")
        pygame.display.flip()
        
        io_loop(keyboard, output, instrument)
        
    finally:
        del output
        midi.quit()

main()