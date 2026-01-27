from .config import FOCAL_LENGTH, F1_TIRE_DIAMETER, F1_CAR_HEIGHT, TIRE_HEIGHT_RATIO

def estimate_distance(pixel_height, real_height_meters):
    return (real_height_meters * FOCAL_LENGTH) / pixel_height

def estimate_distance_average(bbox_height_pixels):
    if bbox_height_pixels <= 0:
        return None
    return (estimate_distance(bbox_height_pixels * TIRE_HEIGHT_RATIO, F1_TIRE_DIAMETER) + 
            estimate_distance(bbox_height_pixels, F1_CAR_HEIGHT)
            ) / 2
