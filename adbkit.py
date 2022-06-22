import cv2
import numpy as np
import subprocess
import time

def wait_until(img, x=0, y=0, w=1600, h=900, waittime=1, timeout=30, msg='timeout'):
    sum_time = 0
    while not check_exist(img, x, y, w, h):
        time.sleep(waittime)
        sum_time += waittime
        if sum_time > timeout:
            print(msg)
            exit()

def check_exist(img, x, y, w, h, threshold=0.8, screenshot=None):
    if img is None:
        return True
    if screenshot is None:
        screenshot = screeshot()
    crop = screenshot[y:y+h, x:x+w]
    res = cv2.matchTemplate(crop, img, cv2.TM_CCOEFF_NORMED)
    if res.max() > threshold:
        return True
    else:
        return False

def tap(x, y):
    subprocess.Popen(f"adb shell input tap {x} {y}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(0.5)

def screeshot():
    pipe = subprocess.Popen("adb shell screencap -p", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #out, err = pipe.communicate()
    #print(out)
    #print(err)
    image_bytes = pipe.stdout.read().replace(b'\r\n', b'\n')
    #print(image_bytes)
    image = cv2.imdecode(np.fromstring(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    return image