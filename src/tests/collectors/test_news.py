"""
Тестирование функций сбора информации о новостях.
"""

import pytest
from collectors.collector import NewsCollector
from collectors.models import LocationDTO

class TestNewsCollector:
    """
    Тестирование функций сбора информации о новостях.
    """

    location = LocationDTO(
        capital="London",
        alpha2code="gb",
    )

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        self.collector = NewsCollector()

    @pytest.mark.asyncio
    async def test_collect_news(self, mocker):
        """
        Тестирование функции получения информации о новостях.
        """

        await self.collector.collect(frozenset([self.location]))

    @pytest.mark.asyncio
    async def test_read_news(self, mocker):
        """
        Тестирование функции чтения информации о новостях.
        """

        news = await self.collector.read(self.location)
        len(news) > 0
