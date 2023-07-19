from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_images_to_pdf(image_paths, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)

    for image_path in image_paths:
        try:
            img = Image.open(image_path)
            width, height = img.size
            aspect_ratio = width / height
            max_width, max_height = 500, 700  # Adjust these values to your preference

            if aspect_ratio >= 1:
                width = min(width, max_width)
                height = width / aspect_ratio
            else:
                height = min(height, max_height)
                width = height * aspect_ratio

            c.drawImage(image_path, 50, 50, width, height)
            c.showPage()
        except Exception as e:
            print(f"Error processing image {image_path}: {str(e)}")

    c.save()

if __name__ == "__main__":
    image_paths = [
        r"E:\images\image_10551.png",
        r"E:\images\image_10552.png",
        r"E:\images\image_10553.png"
    ]
    output_path = " output.pdf"
    convert_images_to_pdf(image_paths, output_path)
