import pygame
import time
import pygame.midi
import mido
import threading
from threading import Timer
import subprocess
pygame.midi.init()
player= pygame.midi.Output(0)
player.set_instrument(0,1)
major=[0,4,7,12]
def get_master_volume(self):
    proc = subprocess.Popen('/usr/bin/amixer sget Master', shell=True, stdout=subprocess.PIPE)
    amixer_stdout = proc.communicate()[0].split('\n')[4]
    proc.wait()

    find_start = amixer_stdout.find('[') + 1
    find_end = amixer_stdout.find('%]', find_start)

    return float(amixer_stdout[find_start:find_end])
def set_master_volume(self, widget):
    val = self.volume
    val = float(int(val))
    proc = subprocess.Popen('/usr/bin/amixer sset Master ' + str(val) + '%', shell=True, stdout=subprocess.PIPE)
    proc.wait()
def go(note,velocity,duration):
    speed = 5
    player.note_on(note, 127,1)
    t = Timer(float(duration)/float(speed),closeNote(note))
    print t.interval
    t.start()
def closeNote(note):
    player.note_off(note,127,1)
def arp(base,ints):
    for n in ints:
        go(base+n)

def chord(base, ints):
    player.note_on(base,127,1)
    player.note_on(base+ints[1],127,1)
    player.note_on(base+ints[2],127,1)
    player.note_on(base+ints[3],127,1)
    time.sleep(1)
    player.note_off(base,127,1)
    player.note_off(base+ints[1],127,1)
    player.note_off(base+ints[2],127,1)
    player.note_off(base+ints[3],127,1)
def end():
       pygame.quit()
class playingThread(threading.Thread):
    def __init__(self,track):
        self.track = track
    def run(self):
        for message in track:
            if message.type=='note_on':
                note = message.note
                velocity = message.velocity
                duration = message.time
                go(note,velocity,duration)
# go(50)
# arp(45, [2,5,6,8])
mid = mido.MidiFile('beethoventest.mid')
# output = mido.open_output()
# a = []
# for i in xrange(len(mid.tracks)):
    # try:
        # a[i] = playingThread(mid.tracks[i]).start()
    # except:
        # print "fail"
# for message in track:
    # if message.type=='note_on':
        # note = message.note
        # velocity = message.velocity
        # duration = message.time
        # go(note,velocity,duration)

for message in mid.play():
    if message.type=='note_on':
        note = message.note
        velocity = message.velocity
        duration = message.time
        try:
            go(note,velocity,duration)
        except:
            print "oops"