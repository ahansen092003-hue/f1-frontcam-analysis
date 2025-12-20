# F1 Front Camera Analysis

Computer vision pipeline for automated Formula 1 car detection in onboard cockpit footage using YOLOv8.

## Features
- Real-time car detection using YOLOv8
- Configurable confidence thresholds
- Bounding box visualization
- Docker containerization for reproducible deployment

## Technologies
- Python 3.10
- YOLOv8 (Ultralytics)
- OpenCV
- Docker

## Quick Start

### Docker
```bash
# Using docker-compose (recommended)
docker-compose up

# Or build and run manually
docker build -t f1-analysis .
docker run --rm \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/models:/app/models \
  -v $(pwd)/output:/app/output \
  f1-analysis testvid1.mp4 0.15
```

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run detection
python -m src.main <video_filename> [confidence_threshold]
```

## Project Structure
```
├── src/               # Source code
├── data/input/        # Input videos
├── output/videos/     # Processed videos
├── models/            # YOLO models
└── Dockerfile         # Container definition
```

## Future Work
- Multi-object tracking across frames
- Speed estimation from position changes
- Distance calculation using camera calibration
- Track positioning analysis