from pathlib import Path
from PIL import Image

def compress_image(input_path: Path, output_path: Path, target_size: int = 1500, quality: int = 85) -> None:
    """Compress an image to a target size in bytes."""
    with Image.open(input_path) as img:
        # Convert RGBA to RGB if needed
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        # Save the image with initial quality
        img.save(output_path, 'PNG', quality=quality, optimize=True)
        
        # Check file size and adjust quality if necessary
        while output_path.stat().st_size > target_size and quality > 10:
            quality -= 5  # Reduce quality by 5% each iteration
            img.save(output_path, 'PNG', quality=quality, optimize=True)

# Define input and output paths
input_path = Path('shapes.png')
output_path = Path('shapes_compressed.png')

# Compress the image
compress_image(input_path, output_path, target_size=1500)

# Check the final file size
print(f"Final file size: {output_path.stat().st_size} bytes")