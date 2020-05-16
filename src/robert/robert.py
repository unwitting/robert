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

    def begin_forward_move(self, speed: float = MotionController.SPEED_STANDARD):
        self._motion_controller.forward(speed)

    def begin_backward_move(self, speed: float = MotionController.SPEED_STANDARD):
        self._motion_controller.backward(speed)

    def begin_anticlockwise_turn(self, speed: float = MotionController.SPEED_STANDARD):
        self._motion_controller.turn_anticlockwise(speed)

    def begin_clockwise_turn(self, speed: float = MotionController.SPEED_STANDARD):
        self._motion_controller.turn_clockwise(speed)

    def begin_brake(self):
        self._motion_controller.stop()

    def begin_coast_to_stop(self):
        self._motion_controller.stop(coast=True)

    async def dance(self):
        m = self._motion_controller
        await m.forward_for(1, MotionController.SPEED_STANDARD)
        await asyncio.sleep(0.25)
        await m.backward_for(1, MotionController.SPEED_STANDARD)
        await asyncio.sleep(0.25)

        await m.turn_clockwise_for(1.25, MotionController.SPEED_STANDARD)
        await asyncio.sleep(0.25)
        await m.turn_anticlockwise_for(2.5, MotionController.SPEED_STANDARD)
        await asyncio.sleep(0.25)
        await m.turn_clockwise_for(1.25, MotionController.SPEED_STANDARD)
        await asyncio.sleep(0.25)

    def _log(self, s: str):
        print('Robert : {}'.format(s))
