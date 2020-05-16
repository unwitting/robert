import asyncio
import os

if os.getenv('ENVIRONMENT', 'production') == 'production':
    from .drv8830_motor_controller import DRV8830MotorController as MotorController
else:
    from .mock_motor_controller import MockMotorController as MotorController


class MotionController:
    RIGHT_MOTOR_LIST_CORRECT = 1.11

    SPEED_STOP = 0
    SPEED_SLOW = 10
    SPEED_STANDARD = 25
    SPEED_FAST = 50
    SPEED_SUPERFAST = 100

    def __init__(self):
        self._log("Initialising")
        self._left_motor = MotorController(serial_address_index=1)
        self._right_motor = MotorController(serial_address_index=2)
        self._log("Finished initialising")

    async def boot(self):
        self._log("Booting")
        await self.forward_for(1, self.SPEED_STANDARD)
        await asyncio.sleep(0.25)
        await self.backward_for(1, self.SPEED_STANDARD)
        await asyncio.sleep(0.25)

        await self.turn_clockwise_for(1.25, self.SPEED_STANDARD)
        await asyncio.sleep(0.25)
        await self.turn_anticlockwise_for(2.5, self.SPEED_STANDARD)
        await asyncio.sleep(0.25)
        await self.turn_clockwise_for(1.25, self.SPEED_STANDARD)
        await asyncio.sleep(0.25)
        self._log("Finished booting")

    def backward(self, speed: float = None):
        self._log("backward()")
        self._left_motor.begin_reverse(speed or self.SPEED_STANDARD)
        self._right_motor.begin_forward(speed or self.SPEED_STANDARD)

    def forward(self, speed: float = None):
        self._log("forward()")
        self._left_motor.begin_forward(speed or self.SPEED_STANDARD)
        self._right_motor.begin_reverse(speed or self.SPEED_STANDARD)

    def turn_clockwise(self, speed: float = None):
        self._log("turn_clockwise()")
        self._left_motor.begin_forward(speed or self.SPEED_STANDARD)
        self._right_motor.begin_forward(speed or self.SPEED_STANDARD)

    def turn_anticlockwise(self, speed: float = None):
        self._log("turn_anticlockwise()")
        self._left_motor.begin_reverse(speed or self.SPEED_STANDARD)
        self._right_motor.begin_reverse(speed or self.SPEED_STANDARD)

    def stop(self, coast: bool = False):
        self._log("stop()")
        self._left_motor.stop(coast)
        self._right_motor.stop(coast)

    async def backward_for(self, secs: float, speed: float = None):
        self._log("backward_for({})".format(secs))
        self.backward(speed)
        await asyncio.sleep(secs)
        self.stop()

    async def forward_for(self, secs: float, speed: float = None):
        self._log("forward_for({})".format(secs))
        self.forward(speed)
        await asyncio.sleep(secs)
        self.stop()

    async def turn_clockwise_for(self, secs: float, speed: float = None):
        self._log("turn_clockwise_for({})".format(secs))
        self.turn_clockwise(speed)
        await asyncio.sleep(secs)
        self.stop()

    async def turn_anticlockwise_for(self, secs: float, speed: float = None):
        self._log("turn_anticlockwise_for({})".format(secs))
        self.turn_anticlockwise(speed)
        await asyncio.sleep(secs)
        self.stop()

    def _log(self, s: str):
        print('MotionController : {}'.format(s))
