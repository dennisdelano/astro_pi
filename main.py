from image_speed_def import calculate_speed
from take_photos import take_photos

take_photos(2, 1)

image_1 = "sequence1.jpg"
image_2 = "sequence2.jpg"

GSD = 12648
nfeatures = 1000

### Create result.txt file and write the estimate_kmps to the file ###
estimate_kmps = calculate_speed(image_1, image_2, GSD, nfeatures)

# Format the estimate_kmps to have a precision
# of 5 significant figures
estimate_kmps_formatted = "{:.4f}".format(estimate_kmps)

# Create a string to write to the file
output_string = estimate_kmps_formatted

# Write to the file
file_path = "result.txt"  # Replace with your desired file path
with open(file_path, "w") as file:
    file.write(output_string)

print("Data written to", file_path)
