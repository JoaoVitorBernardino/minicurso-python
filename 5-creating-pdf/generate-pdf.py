from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

fileName = 'test.pdf'
documentTitle = 'test'
title = 'Test Test'
subTitle = 'generate pdf test'
textLines = [
    'Lorem ipsum dolor sit amet. A cumque ratione quo',
    'dicta enim a facere optio. Eum sunt mollitia ut',
    'blanditiis quasi ut assumenda blanditiis qui',
    'voluptate quia et libero molestiae non dolorem',
    'vitae ea eveniet tempore. ',
]
image = 'cat.png'

pdf = canvas.Canvas(fileName)

pdf.setTitle(documentTitle)

pdf.drawCentredString(300, 770, title)

pdf.setFillColorRGB(0, 0, 255)
pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290, 720, subTitle)

pdf.line(30, 710, 550, 710)

text = pdf.beginText(40, 680)
text.setFont("Courier", 18)
text.setFillColor(colors.red)

for line in textLines:
    text.textLine(line)

pdf.drawText(text)

pdf.drawInlineImage(image, 130, 370)
pdf.save()