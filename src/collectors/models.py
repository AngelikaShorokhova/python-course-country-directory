"""
Описание моделей данных (DTO).
"""
from typing import Optional

from pydantic import Field, BaseModel


class HashableBaseModel(BaseModel):
    """
    Добавление хэшируемости для моделей.
    """

    def __hash__(self) -> int:
        return hash((type(self),) + tuple(self.__dict__.values()))


class LocationDTO(HashableBaseModel):
    """
    Модель локации для получения сведений о погоде.

    .. code-block::

        LocationDTO(
            capital="Mariehamn",
            alpha2code="AX",
        )
    """

    capital: str
    alpha2code: str = Field(min_length=2, max_length=2)  # country alpha‑2 code


class LanguagesInfoDTO(HashableBaseModel):
    """
    Модель данных о языке.

    .. code-block::

        LanguagesInfoDTO(
            name="Swedish",
            native_name="svenska"
        )
    """

    name: str
    native_name: str


class CountryDTO(BaseModel):
    """
    Модель данных о стране.

    .. code-block::

        CountryDTO(
            area = 4343.43
            capital="Mariehamn",
            latitude=56.76,
            longitude=6.87,
            alpha2code="AX",
            alt_spellings=[
              "AX",
              "Aaland",
              "Aland",
              "Ahvenanmaa"
            ],
            flag="http://assets.promptapi.com/flags/AX.svg",
            languages={
                LanguagesInfoDTO(
                    name="Swedish",
                    native_name="svenska"
                )
            },
            name="\u00c5land Islands",
            population=28875,
            subregion="Northern Europe",
            timezones=[
                "UTC+02:00",
            ],
        )
    """

    area: Optional[float]
    capital: str
    latitude: float
    longitude: float
    alpha2code: str
    alt_spellings: list[str]
    flag: str
    languages: set[LanguagesInfoDTO]
    name: str
    population: int
    subregion: str
    timezones: list[str]


class WeatherInfoDTO(BaseModel):
    """
    Модель данных о погоде.

    .. code-block::

        WeatherInfoDTO(
            temp=13.92,
            pressure=1023,
            humidity=54,
            wind_speed=4.63,
            description="scattered clouds",
            timezone=5,
        )
    """

    temp: float
    pressure: int
    humidity: int
    wind_speed: float
    description: str
    timezone: int


class NewsDTO(BaseModel):
    """
    Модель данных о новости.

    .. code-block::

       NewsDTO(
            title = "Majority of English councils plan more cuts at same time as maximum tax rises - The Guardian",
            url="https://news.google.com/rss/articles/CBMib2h0dHBzOi8vd3d3LnRoZWd1YXJkaWFuLmNvbS9zb2NpZXR5LzIwMjMvbWFyLzA3L2VuZ2xpc2gtY291bmNpbHMtY3V0cy1zZXJ2aWNlcy1tYXhpbXVtLXRheC1yaXNlcy1sb2NhbC1maW5hbmNlc9IBb2h0dHBzOi8vYW1wLnRoZWd1YXJkaWFuLmNvbS9zb2NpZXR5LzIwMjMvbWFyLzA3L2VuZ2xpc2gtY291bmNpbHMtY3V0cy1zZXJ2aWNlcy1tYXhpbXVtLXRheC1yaXNlcy1sb2NhbC1maW5hbmNlcw?oc=5",
            source="Google News",
            publishedAt = "2023-03-07T06:00:00Z"
        )
    """

    title: Optional[str]
    url: Optional[str]
    source: Optional[str]
    publishedAt: Optional[str]


class LocationInfoDTO(BaseModel):
    """
    Модель данных для представления общей информации о месте.

    .. code-block::

        LocationInfoDTO(
            location=CountryDTO(
                capital="Mariehamn",
                alpha2code="AX",
                alt_spellings=[
                  "AX",
                  "Aaland",
                  "Aland",
                  "Ahvenanmaa"
                ],
                flag="http://assets.promptapi.com/flags/AX.svg",
                languages={
                    LanguagesInfoDTO(
                        name="Swedish",
                        native_name="svenska"
                    )
                },
                name="\u00c5land Islands",
                population=28875,
                subregion="Northern Europe",
                timezones=[
                    "UTC+02:00",
                ],
            ),
            weather=WeatherInfoDTO(
                temp=13.92,
                pressure=1023,
                humidity=54,
                wind_speed=4.63,
                description="scattered clouds",
            ),
        )
    """

    location: CountryDTO
    weather: WeatherInfoDTO
    news: Optional[list[NewsDTO]]
