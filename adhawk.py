import time
import threading
import pygame
import serial

import adhawkapi
import adhawkapi.frontend
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mpl

class GazeVisualizer:
    def __init__(self):
        # Create a black screen
        plt.style.use('dark_background')
        self.fig, self.ax = plt.subplots()
        self.arduinoData = serial.Serial('com14', 115200)

        [x.set_linewidth(0.2) for x in self.ax.spines.values()]
        
        self.ax.set_facecolor('black')
        self.ax.set_xlim(-500, 500)  # Adjust the limits as needed based on your screen size
        self.ax.set_ylim(-500, 500)

        # Initialize the circle representing gaze
        self.circle = plt.Circle((0, 0), radius=20, color='white', fill=False)
        self.ax.add_artist(self.circle)

        # Set plot properties
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')
        

        # Initialize the animation
        self.ani = None

    def update(self, x, y):
        # Generate random gaze data for demonstration purposes
        #
        # self.circle.set_center((x, y))
        # self.ani = FuncAnimation(self.fig, self.circle, blit=True, interval=50)
        # print(f"x: {x}, y:{y})")

        x_current_direction = 'nonex'
        y_current_direction = 'noney'
        if x < -23:
            x_current_direction = 'left'
        elif x > 23:
            x_current_direction = 'right'

        if y < -15 :
            y_current_direction = 'down'
        elif y > 44:
            y_current_direction = 'up'

        x_data = x_current_direction+'\r'
        self.arduinoData.write(x_data.encode())
        print(f"Giving {x_current_direction} to x")

        y_data = y_current_direction+'\r'
        self.arduinoData.write(y_data.encode())
        print(f"Giving {y_current_direction} to y")

    def show(self):
        # Show the plot
        plt.show()

gaze_visualize = GazeVisualizer()


# Called when data is captured
def output_data(x, y): 
    #print(f"X: {x*5}, Y: {y*5}")
    if not np.isnan(x) and not np.isnan(y):
        gaze_visualize.update(x*10, y*10)

    # cmd = f"[{x}, {y}]"+'\r'
    # arduinoData.write(cmd.encode())
# print("send")
# test = f"hey" + '\r'
# arduinoData.write(test.encode())
# print("Done")
class FrontendData:
    ''' BLE Frontend '''

    def __init__(self):
        # Instantiate an API object
        self._api = adhawkapi.frontend.FrontendApi(ble_device_name='ADHAWK MINDLINK-282')

        # Tell the api that we wish to receive eye tracking data stream
        # with self._handle_et_data as the handler
        self._api.register_stream_handler(adhawkapi.PacketType.EYETRACKING_STREAM, self._handle_et_data)

        # Tell the api that we wish to tap into the EVENTS stream
        # with self._handle_events as the handler
        self._api.register_stream_handler(adhawkapi.PacketType.EVENTS, self._handle_events)

        # Start the api and set its connection callback to self._handle_tracker_connect/disconnect.
        # When the api detects a connection to a MindLink, this function will be run.
        self._api.start(tracker_connect_cb=self._handle_tracker_connect,
                        tracker_disconnect_cb=self._handle_tracker_disconnect)

    def shutdown(self):
        '''Shutdown the api and terminate the bluetooth connection'''
        self._api.shutdown()

    @staticmethod
    def _handle_et_data(et_data: adhawkapi.EyeTrackingStreamData):
        ''' Handles the latest et data '''
        if et_data.gaze is not None:
            xvec, yvec, zvec, vergence = et_data.gaze
            # print(f'Gaze=x={xvec:.2f},y={yvec:.2f},z={zvec:.2f},vergence={vergence:.2f}')
            output_data(xvec, yvec)

        # if et_data.eye_center is not None:
        #     if et_data.eye_mask == adhawkapi.EyeMask.BINOCULAR:
        #         rxvec, ryvec, rzvec, lxvec, lyvec, lzvec = et_data.eye_center
        #         print(f'Eye center: Left=(x={lxvec:.2f},y={lyvec:.2f},z={lzvec:.2f}) '
        #               f'Right=(x={rxvec:.2f},y={ryvec:.2f},z={rzvec:.2f})')

        # if et_data.pupil_diameter is not None:
        #     if et_data.eye_mask == adhawkapi.EyeMask.BINOCULAR:
        #         rdiameter, ldiameter = et_data.pupil_diameter
        #         print(f'Pupil diameter: Left={ldiameter:.2f} Right={rdiameter:.2f}')

        # if et_data.imu_quaternion is not None:
        #     if et_data.eye_mask == adhawkapi.EyeMask.BINOCULAR:
        #         x, y, z, w = et_data.imu_quaternion
        #         print(f'IMU: x={x:.2f},y={y:.2f},z={z:.2f},w={w:.2f}')

    @staticmethod
    def _handle_events(event_type, timestamp, *args):
        if event_type == adhawkapi.Events.BLINK:
            duration = args[0]
            # print(f'Got blink: {timestamp} {duration}')
        if event_type == adhawkapi.Events.EYE_CLOSED:
            eye_idx = args[0]
            # print(f'Eye Close: {timestamp} {eye_idx}')
        if event_type == adhawkapi.Events.EYE_OPENED:
            eye_idx = args[0]
            # print(f'Eye Open: {timestamp} {eye_idx}')

    def _handle_tracker_connect(self):
        print("Tracker connected")
        self._api.set_et_stream_rate(20, callback=lambda *args: None)

        self._api.set_et_stream_control([
            adhawkapi.EyeTrackingStreamTypes.GAZE,
            adhawkapi.EyeTrackingStreamTypes.EYE_CENTER,
            adhawkapi.EyeTrackingStreamTypes.PUPIL_DIAMETER,
            adhawkapi.EyeTrackingStreamTypes.IMU_QUATERNION,
        ], True, callback=lambda *args: None)

        self._api.set_event_control(adhawkapi.EventControlBit.BLINK, 1, callback=lambda *args: None)
        self._api.set_event_control(adhawkapi.EventControlBit.EYE_CLOSE_OPEN, 1, callback=lambda *args: None)

    def _handle_tracker_disconnect(self):
        print("Tracker disconnected")



# def main():
    ''' App entrypoint '''
    # frontend = FrontendData()

    # try:
    #     while True:
    #         time.sleep(1)
    # except (KeyboardInterrupt, SystemExit):
    #     frontend.shutdown()

def eye_tracking_thread():
    frontend = FrontendData()

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        frontend.shutdown()


eye_tracking_thread = threading.Thread(target=eye_tracking_thread)
eye_tracking_thread.daemon = True  # This allows the thread to exit when the main program exits
eye_tracking_thread.start()

def main():
    gaze_visualize.show()
 


if __name__ == '__main__':
    main()
