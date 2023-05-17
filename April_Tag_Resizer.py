from PIL import Image
import os

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f"The original image size is {width}x{height}")

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print(f"The resized image size is {width}x{height}")
    resized_image.show()
    resized_image.save(output_image_path)

tag_dir = '.'  # directory containing the tag images
for filename in os.listdir(tag_dir):
    if filename.endswith('.png'):
        resize_image(os.path.join(tag_dir, filename), 
                     os.path.join(tag_dir, 'resized', filename), 
                     (238, 238))  # 85mm = 238 pixels at 72 dpi
