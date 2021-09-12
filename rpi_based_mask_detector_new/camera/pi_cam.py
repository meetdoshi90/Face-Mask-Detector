from cv2 import cv2
from imutils.video.pivideostream import PiVideoStream
import time
from tf_lite import Model
import numpy as np
import RPi.GPIO as GPIO
from time import sleep
from cv2 import resize
from picamera import PiCamera
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

class VideoCamera(object):
    
    def __init__(self):
        self.cap = PiVideoStream().start()
        time.sleep(0.1)
        print("Initialising Raspberry Pi...")
        GPIO.output(11,1)
        print("LED Red Testing")
        time.sleep(1.0)
        GPIO.output(11,0)
        GPIO.output(13,1)
        print("LED Green Testing")
        time.sleep(1.0)
        GPIO.output(13,0)
        GPIO.output(15,1)
        print("LED Blue Testing")
        time.sleep(1.0)
        GPIO.output(15,0)



    def __del__(self):
        self.cap.stop()

    def get_frame(self):
        frame = self.cap.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def get_object(self, classifier):
        frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        objects = classifier.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the objects
        for (x, y, w, h) in objects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 140, 125), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def get_mask(self):
        frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        
        model = Model()
        interpreter = model.load_interpreter()
        input_details = model.input_details()
        output_details = model.output_details()
        input_shape = input_details[0]['shape']

        label_dict = {0: 'MASK', 1: "NO MASK"}
        eye_img = gray
        resized = cv2.resize(eye_img, (100,100))
        normalized = resized / 255.0
        reshaped = np.reshape(normalized, input_shape)
        reshaped = np.float32(reshaped)
        interpreter.set_tensor(input_details[0]['index'], reshaped)
        interpreter.invoke()
        result = interpreter.get_tensor(output_details[0]['index'])
        result = 1 - result
        label = np.argmax(result, axis=1)[0]
        if label==0:
            cv2.putText(frame, label_dict[label], (75,150),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (250, 240, 255), 2)
            GPIO.output(15,1)
            print(label_dict[label])
            time.sleep(0.1)
            GPIO.output(15,0)
        elif label==1:
            cv2.putText(frame, label_dict[label], (75,150),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (250, 240, 255), 2)
            GPIO.output(13,1)
            print(label_dict[label])
            time.sleep(0.1)
            GPIO.output(13,0)
            


        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()


