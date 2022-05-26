import argparse
from tabnanny import check
import cv2
from numpy import ndarray
import adbkit
import stage
import time
import select_card

if __name__ == '__main__':
    stg = stage.Stage()
    stg.run()