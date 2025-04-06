from PIL import Image

def lambda_handler():
    img = Image.new('RGB', (100, 100), color='red')
    img.save("test/test.jpg")
    return {
        'statusCode': 200,
        'body': 'Pillow works!'
    }
    
# Example usage
if __name__ == "__main__":
    lambda_handler()
