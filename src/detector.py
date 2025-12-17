import cv2
from pathlib import Path
from ultralytics import YOLO

from config import MODEL_PATH

class Detector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)