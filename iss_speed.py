from exif import Image
from datetime import datetime
import cv2
import math

def get_time(image):
    with open(image, 'rb') as iamge_file:
        img = Image(iamge_file)
        time_str = img.get('datetime_original')
        time = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
        return time
            
def get_time_difference(image1, image2):
    time1 = get_time(image1)
    time2 = get_time(image2)
    return abs((time2 - time1).total_seconds())

def convert_to_cv(image_1, image_2):
    image_1_cv = cv2.imread(image_1, 0)
    image_2_cv = cv2.imread(image_2, 0)
    return image_1_cv, image_2_cv

def get_distance(image1, image2):
    image1_cv, image2_cv = convert_to_cv(image1, image2)
    image1_gray = cv2.cvtColor(image1_cv, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2_cv, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(image1_gray, None)
    kp2, des2 = orb.detectAndCompute(image2_gray, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches[0].distance

def get_speed(image1, image2):
    distance = get_distance(image1, image2)
    time_difference = get_time_difference(image1, image2)
    return distance / time_difference

print(get_speed('Astro_Pi/ExamplePhotos/atlas_photo_012.jpg', 'Astro_Pi/ExamplePhotos/atlas_photo_013.jpg'))