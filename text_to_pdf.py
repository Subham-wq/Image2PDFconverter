from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def text_to_pdf(text, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)

    # Set font properties (optional)
    font_name = "Helvetica"
    font_size = 12
    line_spacing = 14

    # Position and margins
    x_margin = 50
    y_margin = 50
    x_position = x_margin
    y_position = letter[1] - y_margin

    # Split the text into lines
    lines = text.split("\n")

    # Write each line to the PDF
    for line in lines:
        c.setFont(font_name, font_size)
        c.drawString(x_position, y_position, line)
        y_position -= line_spacing

        # Check if we need to start a new page
        if y_position <= y_margin:
            c.showPage()
            y_position = letter[1] - y_margin

    c.save()

if __name__ == "__main__":
    # Replace this with your desired text
    input_text = """This is a sample text to be converted to a PDF file.
    You can add multiple paragraphs or long text, and the script will automatically wrap it within the page boundaries."""

    output_path = "output.pdf"

    text_to_pdf(input_text, output_path)
