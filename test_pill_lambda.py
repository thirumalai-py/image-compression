from PIL import Image
import io
import os

def lambda_handler(event, context):
    try:
        # Create a simple RGB image (100x100) with red color
        image = Image.new('RGB', (100, 100), color='red')
        
        # Save the image to /tmp/ (Lambda writable dir)
        image_path = "/tmp/test_image.jpg"
        image.save(image_path)

        # Return confirmation and path
        return {
            'statusCode': 200,
            'body': f'Pillow loaded and image created at {image_path}'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
