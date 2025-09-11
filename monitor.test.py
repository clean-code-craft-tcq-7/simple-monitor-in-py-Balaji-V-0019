"""
Test cases for checking the monitor module.
"""
import unittest
from monitor import (vitals_ok, is_temperature_ok, is_pulse_rate_ok, 
                     is_spo2_ok)


class MonitorTest(unittest.TestCase):
    """
    Test cases for the monitor module.
    """
    
    def test_vitals_ok_when_all_within_range(self):
        """
        Test that vitals_ok returns True when all vitals are within range.
        """
        # Test with normal values
        self.assertTrue(vitals_ok(98.1, 70, 98, alert_callback=None))
        self.assertTrue(vitals_ok(99, 80, 95, alert_callback=None))
        
    def test_vitals_not_ok_when_any_vital_out_of_range(self):
        """
        Test that vitals_ok returns False when any vital is out of range.
        """
        # Test with one vital out of range
        self.assertFalse(vitals_ok(99, 102, 70, alert_callback=None))
        self.assertFalse(vitals_ok(94, 70, 98, alert_callback=None))
        self.assertFalse(vitals_ok(98.1, 70, 89, alert_callback=None))

    def test_temperature_boundary_values(self):
        """
        Test temperature boundary values.
        """
        # Test exact boundary values
        self.assertTrue(is_temperature_ok(95, alert_callback=None))  # min
        self.assertTrue(is_temperature_ok(102, alert_callback=None))  # max
        self.assertTrue(is_temperature_ok(98.6, alert_callback=None))  # normal
        
        # Test out of range
        self.assertFalse(is_temperature_ok(94.9, alert_callback=None))
        self.assertFalse(is_temperature_ok(102.1, alert_callback=None))

    def test_pulse_rate_boundary_values(self):
        """
        Test pulse rate boundary values.
        """
        # Test exact boundary values
        self.assertTrue(is_pulse_rate_ok(60, alert_callback=None))  # min
        self.assertTrue(is_pulse_rate_ok(100, alert_callback=None))  # max
        self.assertTrue(is_pulse_rate_ok(80, alert_callback=None))  # normal
        
        # Test out of range
        self.assertFalse(is_pulse_rate_ok(59, alert_callback=None))
        self.assertFalse(is_pulse_rate_ok(101, alert_callback=None))

    def test_spo2_boundary_values(self):
        """
        Test SPO2 boundary values.
        """
        # Test exact boundary values
        self.assertTrue(is_spo2_ok(90, alert_callback=None))  # min
        self.assertTrue(is_spo2_ok(100, alert_callback=None))  # normal
        self.assertTrue(is_spo2_ok(95, alert_callback=None))  # normal
        
        # Test out of range (only lower bound)
        self.assertFalse(is_spo2_ok(89, alert_callback=None))
        self.assertFalse(is_spo2_ok(85, alert_callback=None))

    def test_temperature_out_of_range(self):
        """
        Test that vitals_ok returns False when temperature is out of range.
        """
        self.assertFalse(vitals_ok(94, 70, 98, alert_callback=None))
        self.assertFalse(vitals_ok(103, 70, 98, alert_callback=None))

    def test_pulse_rate_out_of_range(self):
        """
        Test that vitals_ok returns False when pulse rate is out of range.
        """
        self.assertFalse(vitals_ok(98.1, 59, 98, alert_callback=None))
        self.assertFalse(vitals_ok(98.1, 101, 98, alert_callback=None))

    def test_spo2_out_of_range(self):
        """
        Test that vitals_ok returns False when spo2 is out of range.
        """
        self.assertFalse(vitals_ok(98.1, 70, 89, alert_callback=None))
        
    def test_edge_cases(self):
        """
        Test edge cases with extreme values.
        """
        # Test with zero values
        self.assertFalse(is_temperature_ok(0, alert_callback=None))
        self.assertFalse(is_pulse_rate_ok(0, alert_callback=None))
        self.assertFalse(is_spo2_ok(0, alert_callback=None))
        
        # Test with negative values
        self.assertFalse(is_temperature_ok(-10, alert_callback=None))
        self.assertFalse(is_pulse_rate_ok(-5, alert_callback=None))
        self.assertFalse(is_spo2_ok(-1, alert_callback=None))
        
        # Test with very high values
        self.assertFalse(is_temperature_ok(150, alert_callback=None))
        self.assertFalse(is_pulse_rate_ok(200, alert_callback=None))

    def test_alert_callback_called_when_out_of_range(self):
        """
        Test that alert callback is called when values are out of range.
        """
        alert_messages = []
        
        def mock_alert(duration, message):
            alert_messages.append(message)
        
        # Test temperature alert
        is_temperature_ok(94, alert_callback=mock_alert)
        self.assertEqual(len(alert_messages), 1)
        self.assertIn('Temperature is out of range!', alert_messages[0])
        
        # Test pulse rate alert
        alert_messages.clear()
        is_pulse_rate_ok(101, alert_callback=mock_alert)
        self.assertEqual(len(alert_messages), 1)
        self.assertIn('Pulse Rate is out of range!', alert_messages[0])
        
        # Test SPO2 alert
        alert_messages.clear()
        is_spo2_ok(89, alert_callback=mock_alert)
        self.assertEqual(len(alert_messages), 1)
        self.assertIn('Oxygen Saturation is out of range!', alert_messages[0])

    def test_no_alert_when_values_in_range(self):
        """
        Test that no alert is called when values are in range.
        """
        alert_messages = []
        
        def mock_alert(duration, message):
            alert_messages.append(message)
        
        # Test all vitals in range
        result = vitals_ok(98.6, 75, 98, alert_callback=mock_alert)
        self.assertTrue(result)
        self.assertEqual(len(alert_messages), 0)


if __name__ == '__main__':
    unittest.main()
