from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"
SRC_DIR = PROJECT_ROOT / "src"
CACHE_DIR = DATA_DIR / "cache"
INPUT_DIR = DATA_DIR / "input"
DETECTIONS_DIR = OUTPUT_DIR / "detections"
VIDEOS_DIR = OUTPUT_DIR / "videos"

YOLOV8S_MODEL_PATH = PROJECT_ROOT / "models" / "yolov8s.pt"


for directory in [DATA_DIR, OUTPUT_DIR, SRC_DIR, CACHE_DIR, INPUT_DIR, DETECTIONS_DIR, VIDEOS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
        
