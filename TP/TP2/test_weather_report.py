import unittest
from unittest.mock import mock_open, patch
from weather_service import save_weather_report


class TestWeatherReport(unittest.TestCase):
    def setUp(self):
        self.test_city = "Paris"
        self.test_temperature = 20.5
        self.test_timestamp = "2024-01-01T12:00:00"
        self.test_filename = "weather_reports.json"

    @patch('weather_service.datetime')
    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    @patch('weather_service.get_temperature')
    def test_save_weather_report_success(self, mock_get_temp, mock_file, mock_datetime):
        """Test sauvegarde rapport météo - EXERCICE PRINCIPAL"""
        # Configurez mock_get_temp pour retourner 20.5
        mock_get_temp.return_value = self.test_temperature

        # Configurez mock_datetime.now().isoformat() pour retourner une date fixe
        mock_datetime.now.return_value.isoformat.return_value = self.test_timestamp

        # Appelez save_weather_report("Paris")
        result = save_weather_report(self.test_city)

        # Vérifiez que le résultat est True
        self.assertTrue(result)

        # Vérifiez que get_temperature a été appelé avec "Paris"
        mock_get_temp.assert_called_with(self.test_city)

        # Vérifiez que le fichier a été ouvert en lecture puis en écriture
        self.assertTrue(mock_file.call_count >= 2)
        mock_file.assert_any_call(self.test_filename, 'r', encoding='utf-8')
        mock_file.assert_any_call(self.test_filename, 'w', encoding='utf-8')


if __name__ == '__main__':
    unittest.main()
