"""
Created by Martin McLaren c2645410
No AI was used in the creation of this code
"""
import time
import smbus2

I2C_BUS = smbus2.SMBus(1)  # The I2C bus

# The sensor addresses
SENSOR_UPPER = 0x6A  # The upper part of the limb, e.g. upper arm in arm test
SENSOR_LOWER = 0x6B  # The lower part of the limb, e.g. lower arm in arm test.
# DO (or D0) has to be high power to be this address: Connect to 3Vo

"""
VARIABLE MEANINGS
ACCEL   - Accelerometer data
GYRO    - Gyro data
LOW     - Lower half (low byte) of data
HIGH    - High half (high byte) of data
X, Y, Z - Axes
Example:
ACCEL_LOW_X
This is accelerometer data, the low byte of said data, for the X axis 
"""

# Data output addresses
ACCEL_LOW_X = 0x28
ACCEL_HIGH_X = 0x29
ACCEL_LOW_Y = 0x2A
ACCEL_HIGH_Y = 0x2B
ACCEL_LOW_Z = 0x2C
ACCEL_HIGH_Z = 0x2D

GYRO_LOW_X = 0x22
GYRO_HIGH_X = 0x23
GYRO_LOW_Y = 0x24
GYRO_HIGH_Y = 0x25
GYRO_LOW_Z = 0x26
GYRO_HIGH_Z = 0x27

CTRL_ACCEL = 0x10
ACCEL_CONFIG = 0b01000000

CTRL_GYRO = 0x11
GYRO_CONFIG = 0b01000000


def read_register(sensor_address, register):
    return read_register(sensor_address, register)


def write_register(sensor_address, register, value):
    """
    Write a value to a register of a sensor using smbus2
    :param sensor_address: The sensor to write to
    :param register: The register to write to
    :param value: The value to write
    :return:
    """
    I2C_BUS.write_byte_data(sensor_address, register, value)


def initial_config():
    write_register(SENSOR_UPPER, CTRL_ACCEL, ACCEL_CONFIG)
    time.sleep(0.1)
    write_register(SENSOR_LOWER, CTRL_ACCEL, ACCEL_CONFIG)
    time.sleep(0.1)
    write_register(SENSOR_UPPER, CTRL_GYRO, GYRO_CONFIG)
    time.sleep(0.1)
    write_register(SENSOR_LOWER, CTRL_GYRO, GYRO_CONFIG)
    time.sleep(0.1)
    print("Config Complete:")
    print(
        f"""
    UPPER ACCEL: {read_register(SENSOR_UPPER, CTRL_ACCEL)}
    LOWER ACCEL: {read_register(SENSOR_LOWER, CTRL_ACCEL)}
    UPPER GYRO: {read_register(SENSOR_UPPER, CTRL_GYRO)}
    LOWER GYRO: {read_register(SENSOR_LOWER, CTRL_GYRO)}
    """
    )


if __name__ == "__main__":
    initial_config()


class LSM6DSOX:
    """ """

    address = 0x00

    def __init__(self, address):
        if address != 0x6A or address != 0x6B:
            raise ValueError("Invalid address")
        self.address = address

    def initial_config(self):
        write_register(CTRL_ACCEL, ACCEL_CONFIG)
        time.sleep(0.1)
        write_register(CTRL_GYRO, GYRO_CONFIG)
        print("Config Complete:")
        print(
            f"""
        UPPER ACCEL: {read_register(SENSOR_UPPER, CTRL_ACCEL)}
        LOWER ACCEL: {read_register(SENSOR_LOWER, CTRL_ACCEL)}
        """
        )

    def write_register(self, register, value):
        """
        Write a value to a register of a sensor using smbus2
        :param sensor_address: The sensor to write to
        :param register: The register to write to
        :param value: The value to write
        :return:
        """
        I2C_BUS.write_byte_data(self.address, register, value)

    def read_register(self, register):
        return I2C_BUS.read_word_data(self.address, register)
