import asyncio
from drv8830 import DRV8830, I2C_ADDR1, I2C_ADDR2, I2C_ADDR3, I2C_ADDR4  # pylint: disable=import-error

class MotionController:
    LEFT_MOTOR_ADDR = I2C_ADDR1
    RIGHT_MOTOR_ADDR = I2C_ADDR2

    RIGHT_MOTOR_LIST_CORRECT = 1.11

    SPEED_STOP = 0
    SPEED_SLOW = 0.5
    SPEED_STANDARD = 1.5
    SPEED_FAST = 2.25
    SPEED_SUPERFAST = 4

    def __init__(self):
        self._log("Initialising")
        self._left_motor = DRV8830(self.LEFT_MOTOR_ADDR)
        self._right_motor = DRV8830(self.RIGHT_MOTOR_ADDR)
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
        self._left_motor.set_voltage(speed or self.SPEED_STANDARD)
        self._right_motor.set_voltage((speed or self.SPEED_STANDARD) * self.RIGHT_MOTOR_LIST_CORRECT)
        self._left_motor.reverse()
        self._right_motor.forward()
    
    def forward(self, speed: float = None):
        self._log("forward()")
        self._left_motor.set_voltage(speed or self.SPEED_STANDARD)
        self._right_motor.set_voltage((speed or self.SPEED_STANDARD) * self.RIGHT_MOTOR_LIST_CORRECT)
        self._left_motor.forward()
        self._right_motor.reverse()

    def turn_clockwise(self, speed: float = None):
        self._log("turn_clockwise()")
        self._left_motor.set_voltage(speed or self.SPEED_STANDARD)
        self._right_motor.set_voltage(speed or self.SPEED_STANDARD)
        self._left_motor.forward()
        self._right_motor.forward()
    
    def turn_anticlockwise(self, speed: float = None):
        self._log("turn_anticlockwise()")
        self._left_motor.set_voltage(speed or self.SPEED_STANDARD)
        self._right_motor.set_voltage(speed or self.SPEED_STANDARD)
        self._left_motor.reverse()
        self._right_motor.reverse()
    
    def stop(self):
        self._log("stop()")
        self._left_motor.brake()
        self._right_motor.brake()
        self._left_motor.set_voltage(self.SPEED_STOP)
        self._right_motor.set_voltage(self.SPEED_STOP)
    
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
