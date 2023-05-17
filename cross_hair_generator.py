from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

def draw_circles_and_crosshairs(c, x, y, radius_mm, num_circles, size_mm):
    # Convert sizes to points (since ReportLab uses points)
    radius_pt = radius_mm * mm
    size_pt = size_mm * mm

    # Create boarder offsets for the first crosshair
    offset_x = 10 * mm
    offset_y = 10 * mm

    # Calculate center point of the square
    center_x = x + offset_x + size_pt / 2 
    center_y = y + offset_y + size_pt / 2

    # Draw the circles
    for i in range(num_circles):
        c.circle(center_x, center_y, radius_pt * (i + 1), fill=0)

    # Draw the crosshairs
    c.line(center_x - size_pt / 2, center_y, center_x + size_pt / 2, center_y)
    c.line(center_x, center_y - size_pt / 2, center_x, center_y + size_pt / 2)

    # Draw a border around the entire set
    c.rect(x + offset_x, y + offset_y, size_pt, size_pt, fill=0)

def generate_pdf(output_file, radius_mm, num_circles, size_mm, num_sets):
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    # Calculate the size of each set in points
    size_pt = size_mm * mm

    # Calculate the number of rows and columns
    num_rows = num_cols = int(num_sets ** 0.5)

    # Draw each set of circles and crosshairs
    for i in range(num_rows):
        for j in range(num_cols):
            x = j * size_pt
            y = i * size_pt
            draw_circles_and_crosshairs(c, x, y, radius_mm, num_circles, size_mm)

    c.save()

generate_pdf('output_crosshairs.pdf', 10, 3, 85, 4)
