import asyncio
import os
from PIL import Image  # pylint: disable=import-error
import ST7789 as ST7789  # pylint: disable=import-error

class FaceController:
    def __init__(self):
        self._log("Initialising")
        self._display = ST7789.ST7789(
            port=0,
            cs=ST7789.BG_SPI_CS_FRONT,
            dc=9,
            backlight=19,
            spi_speed_hz=80*1000*1000
        )
        self._display_width = self._display.width
        self._display_height = self._display.height
        self._display_dimensions = (self._display_width, self._display_height)
        self._images = {
            "BLANK": self._create_block_colour_image((0, 0, 0)),
            "BOOT_INDICATOR": self._load_image_file("gears.jpg"),
            "BOOT_COMPLETE_INDICATOR": self._load_image_file("tick.png"),
            "RED": self._create_block_colour_image((255, 0, 0)),
        }
        self._log("Finished initialising")
    
    async def boot(self):
        self._log("Booting")
        self._display.begin()
        self.clear()
        self._log("Finished booting")
    
    def show_boot_complete_indicator(self):
        self._display_image_file('BOOT_COMPLETE_INDICATOR')
    
    def show_boot_indicator(self):
        self._display_image_file('BOOT_INDICATOR')
    
    def clear(self):
        self._display_image_file("BLANK")
    
    def _display_image_file(self, image_key: str):
        self._log("Displaying image {}".format(image_key))
        self._display.display(self._images[image_key])
    
    def _create_block_colour_image(self, colour: tuple):
        return Image.new('RGB', self._display_dimensions, color=colour)

    def _load_image_file(self, asset_path: str):
        self._log("Loading image file at asset path '{}'".format(asset_path))
        absolute_path = os.path.join(os.getcwd(), "assets/images", asset_path)
        return Image.open(absolute_path).resize(self._display_dimensions)

    def _log(self, s: str):
        print('FaceController : {}'.format(s))
