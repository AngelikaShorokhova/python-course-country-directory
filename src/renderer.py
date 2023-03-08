"""
Функции для формирования выходной информации.
"""
from datetime import datetime, timedelta, timezone
from decimal import ROUND_HALF_UP, Decimal
from prettytable import PrettyTable

from collectors.models import LocationInfoDTO


class Renderer:
    """
    Генерация результата преобразования прочитанных данных.
    """

    def __init__(self, location_info: LocationInfoDTO) -> None:
        """
        Конструктор.

        :param location_info: Данные о географическом месте.
        """

        self.location_info = location_info

    async def render(self) -> tuple[str, ...]:
        """
        Форматирование прочитанных данных.

        :return: Результат форматирования
        """
        tableCountry = PrettyTable()
        tableCountry.field_names = ["Параметр", "Значение"]
        tableCountry.add_rows(
            [
                ["Страна:", f"{self.location_info.location.name}"],
                ["Площадь:", f"{self.location_info.location.area}"],
                [f"Регион:", f"{self.location_info.location.subregion}"],
                [f"Языки:", f"{await self._format_languages()}"],
                [f"Население страны:", f"{await self._format_population()} чел."],
            ]
        )
        tableCountry.align["Параметр"] = "l"
        tableCountry.align["Значение"] = "l"

        tableCapital = PrettyTable()
        tableCapital.field_names = ["Параметр", "Значение"]
        tableCapital.add_rows(
            [
                [f"Столица:", f"{self.location_info.location.capital}"],
                [f"Географические координаты:", f"{self.location_info.location.latitude}°, {self.location_info.location.longitude}°"],
                [f"Часовой пояс:", f"{timezone(timedelta(hours=int(self.location_info.weather.timezone / 3600)))}"],
                [f"Текущее время:", f"{(datetime.utcnow() + timedelta(hours=int(self.location_info.weather.timezone / 3600))).strftime('%H:%M (%d.%m.%Y)')}"],
            ]
        )
        tableCapital.align["Параметр"] = "l"
        tableCapital.align["Значение"] = "l"

        tableWeather = PrettyTable()
        tableWeather.field_names = ["Параметр", "Значение"]
        tableWeather.add_rows(
            [
                ["Погода:", f"{self.location_info.weather.temp} °C"],
                ["Описание погоды:", f"{self.location_info.weather.description}"],
                ["Видимость:", f"{self.location_info.weather.humidity} м."],
                ["Скорость ветра:", f"{self.location_info.weather.wind_speed} м/с"],
            ]
        )
        tableWeather.align["Параметр"] = "l"
        tableWeather.align["Значение"] = "l"

        tableNews = PrettyTable()
        tableNews.field_names = ["Параметр", "Значение"]
        for i in 0, 1, 2:
            tableNews.add_row(["Заголовок:", f"{self.location_info.news[i].title}"])
            tableNews.add_row(["Ссылка:", f"{self.location_info.news[i].url}"])
            tableNews.add_row(["Источник:", f"{self.location_info.news[i].source}"])
            tableNews.add_row(["Дата публикации:", f"{self.location_info.news[i].publishedAt}"])
        tableNews.align["Параметр"] = "l"
        tableNews.align["Значение"] = "l"

        tableCountry._max_width = {"Параметр": 30, "Значение": 70}
        tableCapital._max_width = {"Параметр": 30, "Значение": 70}
        tableWeather._max_width = {"Параметр": 30, "Значение": 70}
        tableNews._max_width = {"Параметр": 30, "Значение": 70}
        tableCountry._min_width = {"Параметр": 30, "Значение": 70}
        tableCapital._min_width = {"Параметр": 30, "Значение": 70}
        tableWeather._min_width = {"Параметр": 30, "Значение": 70}
        tableNews._min_width = {"Параметр": 30, "Значение": 70}

        output_table = []  # Сводная таблица для вывода
        output_table.append("Информация о стране:")
        output_table.append(tableCountry)
        output_table.append("Информация о столице:")
        output_table.append(tableCapital)
        output_table.append("Информация о погоде:")
        output_table.append(tableWeather)
        output_table.append("Новости:")
        output_table.append(tableNews)

        return output_table

    async def _format_languages(self) -> str:
        """
        Форматирование информации о языках.

        :return:
        """

        return ", ".join(
            f"{item.name} ({item.native_name})"
            for item in self.location_info.location.languages
        )

    async def _format_population(self) -> str:
        """
        Форматирование информации о населении.

        :return:
        """

        # pylint: disable=C0209
        return "{:,}".format(self.location_info.location.population).replace(",", ".")


