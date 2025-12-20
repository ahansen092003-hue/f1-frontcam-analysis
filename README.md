## F1 Front Camera Analysis (Work in Progress)

This project explores computer vision analysis on Formula 1 onboard
front-camera footage.

docker build -t f1-analysis .   

docker-compose up

docker run --rm \                                                       
  -v /Users/ahansen/Desktop/f1-frontcam-analysis/data:/app/data \
  -v /Users/ahansen/Desktop/f1-frontcam-analysis/models:/app/models \
  -v /Users/ahansen/Desktop/f1-frontcam-analysis/output:/app/output \
  f1-analysis testvid1.mp4 0.15