import asyncio
from drv8830 import DRV8830, I2C_ADDR1, I2C_ADDR2, I2C_ADDR3, I2C_ADDR4  # pylint: disable=import-error

class MotionController:
    LEFT_MOTOR_ADDR = I2C_ADDR1
    RIGHT_MOTOR_ADDR = I2C_ADDR1  # TODO change

    VOLTAGE_OFF = 0
    VOLTAGE_STANDARD = 2.5
    VOLTAGE_FAST = 5

    def __init__(self):
        self._log("Initialising")
        self._left_motor = DRV8830(self.LEFT_MOTOR_ADDR)
        self._right_motor = DRV8830(self.RIGHT_MOTOR_ADDR)
        self._log("Finished initialising")

    async def boot(self):
        self._log("Booting")
        await self.forward_for(1.5)
        await self.backward_for(1.5)
        self._log("Finished booting")
    
    def backward(self):
        self._log("backward()")
        self._left_motor.set_voltage(self.VOLTAGE_STANDARD)
        self._right_motor.set_voltage(self.VOLTAGE_STANDARD)
        self._left_motor.reverse()
        self._right_motor.forward()
    
    def forward(self):
        self._log("forward()")
        self._left_motor.set_voltage(self.VOLTAGE_STANDARD)
        self._right_motor.set_voltage(self.VOLTAGE_STANDARD)
        self._left_motor.forward()
        self._right_motor.reverse()
    
    def stop(self):
        self._log("stop()")
        self._left_motor.brake()
        self._right_motor.brake()
        self._left_motor.set_voltage(self.VOLTAGE_OFF)
        self._right_motor.set_voltage(self.VOLTAGE_OFF)
    
    async def backward_for(self, secs: float):
        self._log("backward_for({})".format(secs))
        self.backward()
        await asyncio.sleep(secs)
        self.stop()
    
    async def forward_for(self, secs: float):
        self._log("forward_for({})".format(secs))
        self.forward()
        await asyncio.sleep(secs)
        self.stop()
    
    def _log(self, s: str):
        print('MotionController : {}'.format(s))
