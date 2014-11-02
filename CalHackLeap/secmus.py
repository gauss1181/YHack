import pyglet
import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class SampleListener(Leap.Listener):
    lastSwipeType="Up"
    lasttime=0.0
    track1=pyglet.media.Player()
    track2=pyglet.media.Player()
    def __init__(self, track1, track2):
        super(SampleListener,self).__init__()
        self.track1 = track1
        self.track2 = track2
    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);

    def on_frame(self, controller):
        # print "Frame available"
        frame = controller.frame()
        gestures = frame.gestures()
        if len(gestures)>0:
            for gesture in gestures:
                circle = Leap.CircleGesture(gesture)
                if (circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2):
                    self.clockwiseness = "clockwise"
                    if gesture.hands[0].is_right:
                        newtime  = self.track1.time+.2*gesture.duration/300000
                        if newtime>0 and newtime<self.track1.length:
                            self.track1.seek(newtime)
                    elif gesture.hands[0].is_left:
                        newtime  = self.track2.time+.2*gesture.duration/300000
                        if newtime>0 and newtime<self.track2.length:
                            self.track2.seek(newtime)
                else:
                    self.clockwiseness = "counterclockwise"
                    if gesture.hands[0].is_right:
                        newtime  = self.track1.time-.2*gesture.duration/300000
                        if newtime>0 and newtime<self.track1.length:
                            self.track1.seek(newtime)      # print gesture.direction
                    elif gesture.hands[0].is_left:
                        newtime  = self.track2.time-.2*gesture.duration/300000
                        if newtime>0 and newtime<self.track2.length:
                            self.track2.seek(newtime)
        # if gestures.length>0:
            # print gestures
def main():
    music1 = pyglet.resource.media('Mamma Mia.mp3')
    player1 = music1.play()
    music2 = pyglet.resource.media('Super Trouper.mp3')
    player2 = music2.play()
    listener = SampleListener(player1, player2)
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    pyglet.app.run()
    # Create a sample listener and controller

# player1.seek(5)
    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()