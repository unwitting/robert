from drv8830 import DRV8830, I2C_ADDR1, I2C_ADDR2, I2C_ADDR3, I2C_ADDR4  # pylint: disable=import-error


class DRV8830MotorController:
    SPEED_MIN = 0
    SPEED_MAX = 5

    def __init__(self, **kwargs):
        serial_address_index = kwargs.get('serial_address_index', 1)
        self._address = [I2C_ADDR1, I2C_ADDR2, I2C_ADDR3,
                         I2C_ADDR4][serial_address_index - 1]
        self._motor = DRV8830(self._address)

    def begin_forward(self, speed):
        voltage = self._voltage_from_proportionate_speed(speed)
        self._motor.set_voltage(voltage)
        self._motor.forward()

    def begin_reverse(self, speed):
        voltage = self._voltage_from_proportionate_speed(speed)
        self._motor.set_voltage(voltage)
        self._motor.reverse()

    def stop(self, coast: bool = False):
        if coast:
            self._motor.coast()
        else:
            self._motor.brake()
        self._motor.set_voltage(self.SPEED_MIN)

    def _voltage_from_proportionate_speed(self, speed):
        return min(
            self.SPEED_MAX,
            max(self.SPEED_MIN, self.SPEED_MIN +
                ((self.SPEED_MAX - self.SPEED_MIN) * (speed / 100.0)))
        )
