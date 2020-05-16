class MockScreenController:
    def __init__(self, **kwargs):
        width = kwargs.get('display_width', 250)
        height = kwargs.get('display_height', 250)
        self._display_dimensions = (width, height)

    async def boot(self):
        pass

    def display_pil_image(self, image):
        pass

    def dimensions(self):
        return self._display_dimensions
