"""
Тестирование функций клиента для получения информации о погоде.
"""

import pytest

from clients.weather import NewsClient
from settings import API_KEY_NEWSAPI


@pytest.mark.asyncio
class TestClientWeather:
    """
    Тестирование клиента для получения информации о погоде.
    """

    base_url = "https://newsapi.org/v2"

    @pytest.fixture
    def client(self):
        return NewsClient()

    async def test_get_base_url(self, client):
        assert await client.get_base_url() == self.base_url

    async def test_get_weather(self, mocker, client):
        mocker.patch("clients.base.BaseClient._request")

        await client.get_weather("gb")
        await client._request(f"{self.get_base_url}/top-headlines?country=gb&apiKey={API_KEY_NEWSAPI}")