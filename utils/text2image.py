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


if __name__ == "__main__":
    text = '''Hello World! wowo存根图像插件\n FitsStubImagePlugin 已被移除。
    无需处理器即可读取FITS图像 FitsImagePlugin 取而代之的是。字体大小和偏移方法自 9.2.
    0 版本弃用.Removed in version 10.0.0删除了几个用于计算呈现文本的大小和偏移量的函数：'''
    font_path = "../static/SmileySans-Oblique.ttf"
    font_size = 32
    image_format = "png"
    text_to_image(text, font_path, font_size, image_format)