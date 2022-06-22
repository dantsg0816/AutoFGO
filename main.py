import argparse
from tabnanny import check
import cv2
from numpy import ndarray
import adbkit
import stage
import time
import select_card

if __name__ == '__main__':
    #stg = stage.Stage()
    #stg.run()
    while True:
        for i in range(70):
            adbkit.tap(540, 520)
            time.sleep(0.5)
        adbkit.tap(1392, 305)
        time.sleep(0.5)
        adbkit.tap(1050, 700)
        time.sleep(1.5)
        adbkit.tap(800, 700)
        time.sleep(2)