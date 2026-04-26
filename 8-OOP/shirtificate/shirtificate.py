from fpdf import FPDF


def main():
    user = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    img_w = 100
    x_pos = (pdf.w - img_w) / 2
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", style="B", size=16)
    pdf.cell(0, 10, "CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", x=x_pos, y=50, w=img_w)
    pdf.set_text_color(255, 255, 255)
    text = f"{user} took CS50"
    text_width = pdf.get_string_width(text)
    x = (pdf.w - text_width) / 2
    pdf.text(x, 85, text)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
