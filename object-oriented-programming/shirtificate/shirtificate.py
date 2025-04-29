from fpdf import FPDF

class PDF(FPDF):
    def __init__(self,orientation,unit, format,name):
        super().__init__(orientation, unit, format)
        self.name = f"{name} took CS50"
    def header(self):
        self.set_font("helvetica",style="B",size=26)
        self.cell(100,40,"CS50 Shirtificate",align="C",center=True)
        self.ln(60)
        self.image("./shirtificate.png",60,50,90,70)
        self.set_font("helvetica", size=10)
        self.set_text_color(255,255,255)
        self.cell(80, 10, self.name, align="C", center=True)


def main():
    name = input("Name: ").strip()
    pdf = PDF("P", "mm", "A4",name)
    pdf.add_page()
    pdf.output("shirtificate.pdf")

if __name__=="__main__":
    main()