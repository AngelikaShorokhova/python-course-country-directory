"""
Тестирование функций сбора информации о погоде.
"""

import pytest
from collectors.collector import WeatherCollector
from collectors.models import LocationDTO


class TestWeatherCollector:
    """
    Тестирование функций сбора информации о погоде.
    """

    location = LocationDTO(
        capital="London",
        alpha2code="gb",
    )

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        self.collector = WeatherCollector()

    @pytest.mark.asyncio
    async def test_collect_weather(self, mocker):
        """
        Тестирование функции получения информации о погоде.
        """

        await self.collector.collect(frozenset([self.location]))

    @pytest.mark.asyncio
    async def test_read_weather(self, mocker):
        """
        Тестирование функции чтения информации о погоде.
        """

        weather = await self.collector.read(self.location)
        assert weather is not None
        assert weather.timezone == 0
