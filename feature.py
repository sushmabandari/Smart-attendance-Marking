import os
import face_recognition
from PIL import Image, ImageDraw

# Input and output folders
input_folder = "input_folder"
output_folder = "output_folder"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to process an image
def process_image(input_image_path, output_image_path):
    try:
        # Load the image
        image = face_recognition.load_image_file(input_image_path)

        # Find all face locations in the image
        face_locations = face_recognition.face_locations(image)

        # Load the image with PIL for drawing
        pil_image = Image.open(input_image_path)
        draw = ImageDraw.Draw(pil_image)

        # Loop through each face found in the image
        for face_location in face_locations:
            # Extract face features
            face_encoding = face_recognition.face_encodings(image, [face_location])[0]

            # Draw a box around the face
            top, right, bottom, left = face_location
            draw.rectangle(((left, top), (right, bottom)), outline="red", width=3)

            # Use the same filename for both the image and encoding features
            base_filename = os.path.splitext(os.path.basename(input_image_path))[0]
            encoding_output_path = os.path.join(output_folder, f"{base_filename}.txt")
            image_output_path = os.path.join(output_folder, f"{base_filename}.jpg")

            # Save the face feature encoding
            with open(encoding_output_path, "w") as encoding_file:
                for value in face_encoding:
                    encoding_file.write(f"{value}\n")

        # Save the image with boxes drawn around faces
        pil_image.save(image_output_path)

    except Exception as e:
        print(f"Error processing {input_image_path}: {str(e)}")

# Process all images in the input folder
for filename in os.listdir(input_folder):
    input_image_path = os.path.join(input_folder, filename)
    process_image(input_image_path, None)  # output_image_path is not used in this case

print("Processing complete.")
