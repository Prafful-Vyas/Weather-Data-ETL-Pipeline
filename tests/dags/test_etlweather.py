import pytest
from unittest.mock import patch, MagicMock
from dags.etlweather import extract_weather_data, transform_weather_data, load_weather_data

# Sample API JSON response
mock_api_response = {
    "current_weather": {
        "temperature": 20.5,
        "windspeed": 5.2,
        "winddirection": 180,
        "weathercode": 1
    }
}

@pytest.fixture
def sample_transformed_data():
    return {
        'latitude': '51.5074',
        'longitude': '-0.1278',
        'temperature': 20.5,
        'windspeed': 5.2,
        'winddirection': 180,
        'weathercode': 1
    }

def test_extract_weather_data():
    """Test weather data extraction using mocked HttpHook."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_api_response

    with patch("weather_dag.HttpHook") as mock_hook:
        mock_hook.return_value.run.return_value = mock_response
        result = extract_weather_data().execute()
        assert result == mock_api_response
        mock_hook.assert_called_once()

def test_transform_weather_data():
    """Test weather data transformation."""
    result = transform_weather_data(mock_api_response).execute()
    expected = {
        'latitude': '51.5074',
        'longitude': '-0.1278',
        'temperature': 20.5,
        'windspeed': 5.2,
        'winddirection': 180,
        'weathercode': 1
    }
    assert result == expected

def test_load_weather_data(sample_transformed_data):
    """Test loading data into PostgreSQL by mocking PostgresHook."""
    mock_cursor = MagicMock()
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    with patch("weather_dag.PostgresHook") as mock_pg_hook:
        mock_pg_hook.return_value.get_conn.return_value = mock_conn

        load_weather_data(sample_transformed_data).execute()

        assert mock_cursor.execute.call_count == 2
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
