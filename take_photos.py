from picamzero import Camera


def take_photos(num_images, interval):
    cam = Camera()
    cam.capture_sequence("sequence", num_images=num_images, interval=interval)
    return
