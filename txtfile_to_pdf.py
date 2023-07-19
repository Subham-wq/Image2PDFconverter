from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def textfile_to_pdf(input_path, output_path):
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

    # Read text from the file
    with open(input_path, "r") as file:
        lines = file.readlines()

    # Write each line to the PDF
    for line in lines:
        c.setFont(font_name, font_size)
        c.drawString(x_position, y_position, line.strip())
        y_position -= line_spacing

        # Check if we need to start a new page
        if y_position <= y_margin:
            c.showPage()
            y_position = letter[1] - y_margin

    c.save()

if __name__ == "__main__":
    input_file_path = "input.txt"  # Replace this with the path to your text file
    output_file_path = "output.pdf"  # Replace this with the desired name and path for the PDF file

    textfile_to_pdf(input_file_path, output_file_path)
