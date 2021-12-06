from PIL import Image


def main():
    im = Image.open('./input/US_invoice_example_abc_design.jpg')
    im.save('./output/US_invoice_example_abc_design.png', dpi=(300, 300), quality=100, format='png')
    im.save('./output/US_invoice_example_abc_design.jpg', dpi=(300, 300), quality=100)
    im = Image.open('./output/US_invoice_example_abc_design.png')
    im.save('./output/US_invoice_example_abc_design_png.jpg', dpi=(300, 300), quality=100)


if __name__ == '__main__':
    main()
