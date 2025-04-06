from PIL import Image
import os

def compress_image(input_path, output_path=None, quality=70, optimize=True):
    """
    Compresses an image and saves it to the output path.
    
    Parameters:
    - input_path (str): Path to the original image.
    - output_path (str): Path to save the compressed image. Defaults to input_path.
    - quality (int): Quality for the output image (1–95).
    - optimize (bool): Whether to optimize the image.
    """
    try:
        img = Image.open(input_path)

        # If no output path, overwrite the input file
        if not output_path:
            output_path = input_path

        # Create output folder if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Convert to RGB if needed (e.g., for PNG)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.save(output_path, quality=quality, optimize=optimize)
        print(f"✅ Image compressed and saved to: {output_path}")

    except Exception as e:
        print(f"❌ Error compressing image: {e}")

# Example usage
if __name__ == "__main__":
    input_file = "example.jpg"  # Change this to your image path
    output_file = "thumbnail/example_compressed.jpg"  # New directory
    compress_image(input_file, output_file, quality=60)
