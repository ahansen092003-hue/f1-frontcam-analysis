from pathlib import Path
from ultralytics import YOLO

from .config import YOLOV8S_MODEL_PATH

class Detector:
    def __init__(self, confidence_threshold, model_path=YOLOV8S_MODEL_PATH, target_class=[2]):
        self.model = YOLO(model_path)
        self.confidence_threshold = confidence_threshold
        self.target_class = target_class
        
    def detect(self, frame) -> list:
        results = self.model.predict(source=frame, conf=self.confidence_threshold, classes=self.target_class, verbose=False)
    
        detections = []
        for box in results[0].boxes:
            detection = {
                'bbox': box.xyxy[0].tolist(),  # [x1, y1, x2, y2]
                'confidence': float(box.conf[0]),
                'class_id': int(box.cls[0])
            }
            detections.append(detection)
    
        return detections