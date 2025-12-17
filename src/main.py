from ultralytics import YOLO
import cv2
import os
import numpy as np
import sys

from detector import Detector
from video_processor import VideoProcessor

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Too few args. Usage: python main.py <input_path> [confidence_threshold]")
        sys.exit(1)

    video_filename = sys.argv[1]
    if len(sys.argv) >= 3:
        confidence = float(sys.argv[2])
    else:
        confidence = 0.4

    processor = VideoProcessor(video_filename)
    detector = Detector(confidence_threshold=confidence)
    
    while True:
        frame = processor.read_frame()
        if frame is None:
            break

        results = detector.detect(frame)
        processor.write_frame(frame)