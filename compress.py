from PIL import Image, ImageDraw, ImageFont

# Set the dimensions of the image
width, height = 50, 20  # Replace with the original image dimensions

# Create a blank image with white background
image = Image.new('RGB', (width, height), color=(255, 255, 255))

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Use a basic font (you might need to adjust the path to a font file)
font = ImageFont.load_default()

# Draw the text
draw.text((10, 0), "1/2", fill="black", font=font)

# Save the image with optimization (lossless compression)
image.save('shapes.png', optimize=True)