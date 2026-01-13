import cv2
from pathlib import Path
from .config import INPUT_DIR, VIDEOS_DIR

class VideoProcessor:
    def __init__(self, video_filename: str):
        self.input_path = INPUT_DIR / video_filename
        self.output_path = VIDEOS_DIR / f"{video_filename.split('.')[0]}_processed.mp4"
        
        self.capture = cv2.VideoCapture(str(self.input_path))
        if not self.capture.isOpened():
            raise FileNotFoundError(f"Could not open video: {self.input_path}")
        
        self.width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = int(self.capture.get(cv2.CAP_PROP_FPS))
            
        self.writer = cv2.VideoWriter(str(self.output_path), cv2.VideoWriter_fourcc(*'mp4v'), self.fps, (self.width, self.height))
        
    ##For editing later
    def read_frame(self):
        success, frame = self.capture.read()
        if success:
            return frame
        return None

    ##For editing later
    
    def write_frame(self, frame):
        self.writer.write(frame)
        