"""
Тестирование функций поиска (чтения) собранной информации в файлах.
"""

import pytest
from reader import Reader
from collectors.models import (
    CountryDTO,
    LocationDTO,
    LocationInfoDTO,
    NewsInfoDTO,
    WeatherInfoDTO,
)

class TestReader:
    location = LocationDTO(
        alpha2code="GB",
        capital="London",
    )

    @pytest.fixture
    def reader(self):
        return Reader()

    @pytest.mark.asyncio
    async def test_find(self, reader):
        location = await reader.find("London")
        assert type(location) == LocationInfoDTO
        assert location.location.name == "United Kingdom of Great Britain and Northern Ireland"
        assert location.location.capital == "London"
        assert location.location.alpha2code == "GB"
        assert len(location.location.languages) != 0
        assert len(location.location.timezones) != 0
        assert location.location.population > 0
        assert location.location.area > 0
        assert len(location.location.alt_spellings) > 0
        assert location.location.subregion == "Northern Europe"
        assert type(location.weather) == WeatherInfoDTO
        assert location.weather.timezone == 0
        assert len(location.news) != 0

    @pytest.mark.asyncio
    async def test_find_not_found(self, reader):
        location = await reader.find("test")
        assert location is None

    @pytest.mark.asyncio
    async def test_get_weather(self, reader):
        weather = await reader.get_weather(self.location)
        assert type(weather) == WeatherInfoDTO
        assert weather.timezone == 0

    @pytest.mark.asyncio
    async def test_get_news(self, reader):
        news = await reader.get_news(self.location)
        assert len(news) != 0

    @pytest.mark.asyncio
    async def test_find_country(self, reader):
        country = await reader.find_country("London")
        assert type(country) == CountryDTO
        assert country.name == "United Kingdom of Great Britain and Northern Ireland"
        assert country.capital == "London"

    @pytest.mark.asyncio
    async def test_find_country_none(self, reader):
        country = await reader.find_country("test")
        assert country is None

