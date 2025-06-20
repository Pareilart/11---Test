import unittest
from unittest.mock import patch, Mock
from weather_service import get_temperature
import requests

class TestWeather(unittest.TestCase):

    def setUp(self):
        """Fixture : prépare les données avant chaque test"""
        # Données météo types
        self.sample_weather_data = {
            'main': {
                'temp': 18.7
            }
        }
        # Ville de test
        self.test_city = "Lyon"

    @patch('weather_service.requests.get')
    def test_get_temperature_success(self, mock_get):
        """Test avec données de la fixture"""
        fake_response = Mock()
        fake_response.status_code = 200
        # Utilisez la fixture
        fake_response.json.return_value = self.sample_weather_data

        mock_get.return_value = fake_response

        # Utilisez la ville de test
        result = get_temperature(self.test_city)

        # Complétez les assertions
        self.assertEqual(result, 18.7)
        mock_get.assert_called_once_with(
            'http://api.openweathermap.org/data/2.5/weather',
            params={
                'q': self.test_city,
                'appid': 'fake_api_key',
                'units': 'metric'
            }
        )
        
    @patch('weather_service.requests.get')
    def test_get_temperature_city_not_found(self, mock_get):
        """Test quand la ville n'existe pas"""
        # Créez un Mock qui retourne status_code = 404
        fake_response = Mock()
        fake_response.status_code = 404
        # Configurez mock_get.return_value
        mock_get.return_value = fake_response
        # Testez get_temperature("VilleInexistante")
        result = get_temperature("VilleInexistante")
        # Vérifiez que le résultat est None
        self.assertIsNone(result)

    @patch('weather_service.requests.get')
    def test_get_temperature_network_error(self, mock_get):
        """Test quand il y a une erreur réseau"""
        # Configurez le mock pour lever une exception réseau
        mock_get.side_effect = requests.exceptions.RequestException()
        # Testez que votre fonction gère l'exception (retourne None)
        result = get_temperature("Paris")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()