import asyncio

from ..face import FaceController
from ..motion import MotionController

class Robert:
    POST_BOOT_PAUSE_SECS = 2

    def __init__(self):
        self._log("Initialising")
        self._face_controller = FaceController()
        self._motion_controller = MotionController()
        self._log("Finished initialising")
    
    async def boot(self):
        self._log("Performing boot")
        await self._face_controller.boot()

        self._face_controller.show_boot_indicator()
        await self._motion_controller.boot()
        self._face_controller.show_boot_complete_indicator()
        self._log("Boot complete, pausing briefly")

        await asyncio.sleep(self.POST_BOOT_PAUSE_SECS)
        self._face_controller.clear()

    def _log(self, s: str):
        print('Robert : {}'.format(s))
