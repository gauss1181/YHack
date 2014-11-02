import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class SampleListener(Leap.Listener):
    lastSwipeType="Up"
    lasttime=0.0
    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        controller.config.set("Gesture.Swipe.MinLength", 50.0)
        controller.config.set("Gesture.Swipe.MinVelocity", 150)
        controller.config.save()

    def on_frame(self, controller):
        # print "Frame available"
        frame = controller.frame()
        gestures = frame.gestures()
        if len(gestures)>0:
            for gesture in gestures:
                if gesture.type is Leap.Gesture.TYPE_SWIPE and frame.hands.rightmost.is_right:
                    gesture = SwipeGesture(gesture)
                    tempdirection = getDirection(gesture.direction)
                    if tempdirection!=self.lastSwipeType:
                        self.lastSwipeType = tempdirection
                        deltat = time.time()-self.lasttime
                        self.lasttime=time.time()
                        print "speed: " + str(deltat/0.25)
                    # print gesture.direction
                    
        # if gestures.length>0:
            # print gestures
def getDirection(vector):
    if vector[1]<-.95:
        return "Down"
    elif vector[1]>.95:
        return "Up"
    elif vector[0]>.95:
        return "right"
    elif vector[0]>-.95:
        return "left"
    elif abs(vector[0]-.5)<.2 and abs(vector[1]+.5)<.2:
        return "right down"
    elif abs(vector[0]+.5)<.2 and abs(vector[1]+.5)<.2:
        return "left down"
    elif abs(vector[0]-.5)<.2 and abs(vector[1]-.5)<.2:
        return "right up"
    elif abs(vector[0]+.5)<.2 and abs(vector[1]-.5)<.2:
        return "left up"
    else:
        return 0
def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

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