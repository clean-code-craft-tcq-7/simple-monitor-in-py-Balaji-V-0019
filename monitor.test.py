"""
Test cases for checking the monitor module.
"""
import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    """
    Test cases for the monitor module.
    """
    def test_not_ok_when_any_vital_out_of_range(self):
        """
        Test that vitals_ok returns False when any vital is out of range.
        """
        self.assertFalse(vitals_ok(99, 102, 70))
        self.assertTrue(vitals_ok(98.1, 70, 98))

    def test_temperature_out_of_range(self):
        """
        Test that vitals_ok returns False when temperature is out of range.
        """
        self.assertFalse(vitals_ok(94, 70, 98))
        self.assertFalse(vitals_ok(103, 70, 98))

    def test_pulse_rate_out_of_range(self):
        """
        Test that vitals_ok returns False when pulse rate is out of range.
        """
        self.assertFalse(vitals_ok(98.1, 59, 98))
        self.assertFalse(vitals_ok(98.1, 101, 98))

    def test_spo2_out_of_range(self):
        """
        Test that vitals_ok returns False when spo2 is out of range.
        """
        self.assertFalse(vitals_ok(98.1, 70, 89))
        self.assertFalse(vitals_ok(98.1, 70, 101))


if __name__ == '__main__':
    unittest.main()
