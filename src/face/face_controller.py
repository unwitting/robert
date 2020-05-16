import asyncio
import os
from PIL import Image

if os.getenv('ENVIRONMENT', 'production') == 'production':
    from .st7789_screen_controller import ST7789ScreenController as ScreenController
else:
    from .mock_screen_controller import MockScreenController as ScreenController


class FaceController:
    def __init__(self):
        self._log("Initialising")
        self._screen = ScreenController()
        self._images = {
            "BLANK": self._create_block_colour_image((0, 0, 0)),
            "BOOT_INDICATOR": self._load_image_file("gears.jpg"),
            "BOOT_COMPLETE_INDICATOR": self._load_image_file("tick.png"),
            "RED": self._create_block_colour_image((255, 0, 0)),
        }
        self._log("Finished initialising")

    async def boot(self):
        self._log("Booting")
        await self._screen.boot()
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
        self._screen.display_pil_image(self._images[image_key])

    def _create_block_colour_image(self, colour: tuple):
        return Image.new('RGB', self._screen.dimensions(), color=colour)

    def _load_image_file(self, asset_path: str):
        self._log("Loading image file at asset path '{}'".format(asset_path))
        absolute_path = os.path.join(os.getcwd(), "assets/images", asset_path)
        return Image.open(absolute_path).resize(self._screen.dimensions())

    def _log(self, s: str):
        print('FaceController : {}'.format(s))
