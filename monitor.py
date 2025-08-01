"""
Monitor module for checking vital signs.
"""
from time import sleep
import sys


def __display_vital_alert(val, msg):
    """
    Display an alert message for vital signs.
    :parm arg: val: Number of seconds to display the alert.
    :parm arg: msg: Message to display.
    :return: None
    """
    print(msg)
    for _ in range(val):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)


def __is_vital_ok(name, value, min_val, max_val):
    """
    Check if a vital sign is within the acceptable range.
    :parm arg: name: Name of the vital sign.
    :parm arg: value: Value of the vital sign.
    :parm arg: min_val: Minimum acceptable value.
    :parm arg: max_val: Maximum acceptable value.
    :return: True if the vital sign is within range, False otherwise.
    """
    if value < min_val or value > max_val:
        __display_vital_alert(6, f'{name} is out of range!')
        return False
    return True


def is_temperature_ok(temperature):
    """
    Check if the temperature is within the acceptable range.
    :parm arg: temperature: Temperature value to check.
    :return: True if the temperature is within range, False otherwise.
    """
    return __is_vital_ok('Temperature', temperature, 95, 102)


def is_pulse_rate_ok(pulse_rate):
    """
    Check if the pulse rate is within the acceptable range.
    :parm arg: pulse_rate: Pulse rate value to check.
    :return: True if the pulse rate is within range, False otherwise.
    """
    return __is_vital_ok('Pulse Rate', pulse_rate, 60, 100)


def is_spo2_ok(spo2):
    """
    Check if the oxygen saturation is within the acceptable range.
    :parm arg: spo2: Oxygen saturation value to check.
    :return: True if the oxygen saturation is within range, False otherwise.
    """
    return __is_vital_ok('Oxygen Saturation', spo2, 90, float('inf'))


def vitals_ok(temperature, pulse_rate, spo2):
    """
    Check if all vital signs are within the acceptable range.
    :parm arg: temperature: Temperature value to check.
    :parm arg: pulse_rate: Pulse rate value to check.
    :parm arg: spo2: Oxygen saturation value to check.
    :return: True if all vital signs are within range, False otherwise.
    """
    return (
      is_temperature_ok(temperature) and
      is_pulse_rate_ok(pulse_rate) and
      is_spo2_ok(spo2)
    )
