import pyvisa
from datetime import datetime

class DS1054Z:

    def __init__(self):
        self.rm = pyvisa.ResourceManager('@py')
        self.inst = self.rm.open_resource('TCPIP0::192.168.0.127::INSTR')
        print(self.inst.query('*IDN?'))

    def get_screenshot(self):
        buffer = self.inst.query_binary_values(':DISPlay:DATA?', datatype='s', container=bytes)

        try:
            timestamp = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
            with open(f'Screenshot_{timestamp}.png', 'xb') as f:
                f.write(buffer)
        except FileExistsError as f:
            print("File already exists")


if __name__ == '__main__':
    scope = DS1054Z()
    scope.get_screenshot()
