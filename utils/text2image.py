from PIL import Image, ImageDraw, ImageFont
import os,sys

async def text_to_image(text, font_path, font_size, image_format,sys_path):
    font = ImageFont.truetype(font_path, font_size)
    left, top, right, bottom = font.getbbox(text)
    image_height = bottom - top
    lines = text.splitlines()
    im = Image.new("RGB", (100, 100))
    draw = ImageDraw.Draw(im)
    line_widths = []
    for line in lines:
        line_width = draw.textlength(line, font)
        line_widths.append(line_width)
    image_width = line_widths[0]
    for line_width in line_widths:
        if line_width > image_width:
            image_width = line_width
    image_width = int(image_width)
    image_height = len(lines)*image_height
    image = Image.new("RGB", (image_width, image_height + 10), "white")
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font, fill="black")
    image.save(sys_path+"/static/output."+image_format)
