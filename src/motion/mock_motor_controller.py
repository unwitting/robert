class MockMotorController:
    def __init__(self, **kwargs):
        pass

    def begin_forward(self, speed):
        pass

    def begin_reverse(self, speed):
        pass

    def stop(self, coast: bool = False):
        pass
