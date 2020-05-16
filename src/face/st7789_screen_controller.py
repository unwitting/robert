import ST7789 as ST7789  # pylint: disable=import-error


class ST7789ScreenController:
    def __init__(self):
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

    async def boot(self):
        self._display.begin()

    def display_pil_image(self, image):
        self._display.display(image)

    def dimensions(self):
        return self._display_dimensions
