import epd1in54
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def main():
    epd = epd1in54.EPD()
    epd.init(epd.lut_full_update)
    image = Image.open('bobby.bmp')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(
        '/usr/share/fonts/truetype/freefont/dejavu/DejaVuSans-Bold.ttf',
        26
    )
    draw.text((0, 0), 'Bobby!', font=font, fill=0) 
    
    epd.clear_frame_memory(0xFF)
    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()
    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()


if __name__ == '__main__':
    main()

