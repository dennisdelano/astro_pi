from exif import Image

image_path = r'C:\Users\maxg1\Desktop\astro_pi\.venv\53244805352_976129d3b3_o.jpg'

with open(image_path, 'rb') as f:
    img = Image(f)

print(img.has_exif)
