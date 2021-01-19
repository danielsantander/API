# OpenWeather API

This api requires an API key which can be generated at https://openweathermap.org/api

<br>

# Current Weather Data
- Access current weather data for any location including over 200,000 cities
- We (OpenWeather) collect and process weather data from different sources such as global and local weather models, satelites, radars, and vast network of weather stations
- JSON, XML, and HTML formats
- Available for both Free and paid subscription

> note: each of these current weather methods described below will have an optional `units` argument. 
> The default value is "imperial". To retrieve data in "standard" units, set the `units` argument equal to "standard".

<hr>

## By City Name:
Retrieve the current weather given the city name.

Use the `WeatherAPI.current_weather_by_city_name()` method.

This method has a few optional input arguments:
- `state_code`
- `country_code`
  - use ISO 3166 country codes
- `units`
  - May set equal to "standard", "metric", or "imperial" units.
  - Default is "imperial" units.

Get Current Weather by City Name:
```
import json
from WeatherAPI import WeatherAPI

weather = WeatherAPI(api_key="<enter_your_api_key_here>")
new_york_weather = weather.current_weather_by_city_name(city_name="New York", units="imperial")
print (json.dumps(new_york_weather, indent=4))
```

The response from the code above should look like:
```
{
    "coord": {
        "lon": -74.006,
        "lat": 40.7143
    },
    "weather": [
        {
            "id": 804,
            "main": "Clouds",
            "description": "overcast clouds",
            "icon": "04n"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 42.71,
        "feels_like": 33.42,
        "temp_min": 42.01,
        "temp_max": 44.01,
        "pressure": 1007,
        "humidity": 56
    },
    "visibility": 10000,
    "wind": {
        "speed": 9.22,
        "deg": 270
    },
    "clouds": {
        "all": 90
    },
    "dt": 1610931738,
    "sys": {
        "type": 1,
        "id": 4610,
        "country": "US",
        "sunrise": 1610885809,
        "sunset": 1610920512
    },
    "timezone": -18000,
    "id": 5128581,
    "name": "New York",
    "cod": 200
}
```


<hr>

## By City ID
A list of City ID's can be found within a JSON file in the same directory as this README file, titled `city.list.json`.

Get current Phoenix, AZ weather by the city's ID:
```
import json
from WeatherAPI import WeatherAPI

weather = WeatherAPI(api_key="<enter_your_api_key_here>")
phx = weather.current_weather_by_city_id(city_id=5308655)   # `units` optional agurmnet defaults to "imperial"
print(json.dumps(phx, indent=4))
```

With a response:
```
{
    "coord": {
        "lon": -112.074,
        "lat": 33.4484
    },
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01n"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 66.83,
        "feels_like": 61.61,
        "temp_min": 63,
        "temp_max": 71.01,
        "pressure": 1012,
        "humidity": 19
    },
    "visibility": 10000,
    "wind": {
        "speed": 0.96,
        "deg": 0
    },
    "clouds": {
        "all": 0
    },
    "dt": 1610932982,
    "sys": {
        "type": 3,
        "id": 2008537,
        "country": "US",
        "sunrise": 1610893894,
        "sunset": 1610930704
    },
    "timezone": -25200,
    "id": 5308655,
    "name": "Phoenix",
    "cod": 200
}
```


<hr>

# By ZIP Code
Get San Antonio, Texas weather by ZIP code:
```
import json
from WeatherAPI import WeatherAPI

weather = WeatherAPI(api_key="<enter_your_api_key_here>")
sa_weather = weather.current_weather_by_zip_code(zip_code=78205, country_code="US")
print (json.dumps(sa_weather, indent=4))
```

With the following output:
```
{
    "coord": {
        "lon": -98.4925,
        "lat": 29.4237
    },
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01n"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 55.71,
        "feels_like": 52.07,
        "temp_min": 55,
        "temp_max": 57,
        "pressure": 1018,
        "humidity": 54
    },
    "visibility": 10000,
    "wind": {
        "speed": 2.28,
        "deg": 109
    },
    "clouds": {
        "all": 1
    },
    "dt": 1610935072,
    "sys": {
        "type": 1,
        "id": 5857,
        "country": "US",
        "sunrise": 1610890134,
        "sunset": 1610927944
    },
    "timezone": -21600,
    "id": 0,
    "name": "San Antonio",
    "cod": 200
}
```

<hr>


## Call current weather for several cities
If you request weather data for several locations, you will get the response only in JSON format (XML and HTML formats are not available for these cases).

### Cities within a rectangle zone
API returns the data from cities within the defined rectangle specified by the geographic coordinates.
Use `WeatherAPI.current_weather_data_with_bound_box()`

> There is a limit of 25 square degrees for Free and Startup plans.

```
import json
from WeatherAPI import WeatherAPI

weather = WeatherAPI(api_key="<enter_your_api_key_here>")
bbox_weather_data = weather.current_weather_with_bound_box(lon_left=12, lat_bottom=32, lon_right=15, lat_top=37, zoom=10))
print(json.dumps(bbox_weather_data, indent=4))
```


Will will return a response with output:
```
{
    "cod": 200,
    "calctime": 0.003548206,
    "cnt": 15,
    "list": [
        {
            "id": 2563191,
            "dt": 1610950199,
            "name": "Birkirkara",
            "coord": {
                "Lon": 14.4611,
                "Lat": 35.8972
            },
            "main": {
                "temp": 54.88,
                "feels_like": 35.37,
                "temp_min": 54,
                "temp_max": 55.4,
                "pressure": 1015,
                "humidity": 67
            },
            "visibility": 10000,
            "wind": {
                "speed": 32.2118826055834,
                "deg": 310
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 20
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n"
                }
            ]
        },
        {
            "id": 2210247,
            "dt": 1610950194,
            "name": "Tripoli",
            "coord": {
                "Lon": 13.1875,
                "Lat": 32.8752
            },
            "main": {
                "temp": 52.5,
                "feels_like": 38.26,
                "temp_min": 52.5,
                "temp_max": 52.5,
                "pressure": 1022,
                "sea_level": 1022,
                "grnd_level": 1020,
                "humidity": 61
            },
            "visibility": 10000,
            "wind": {
                "speed": 21.161417322834648,
                "deg": 261
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ]
        },
        {
            "id": 2216885,
            "dt": 1610950194,
            "name": "Zawiya",
            "coord": {
                "Lon": 12.7278,
                "Lat": 32.7522
            },
            "main": {
                "temp": 49.89,
                "feels_like": 36.79,
                "temp_min": 49.89,
                "temp_max": 49.89,
                "pressure": 1023,
                "sea_level": 1023,
                "grnd_level": 1020,
                "humidity": 56
            },
            "visibility": 10000,
            "wind": {
                "speed": 17.694166070150324,
                "deg": 255
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ]
        },
        {
            "id": 2212771,
            "dt": 1610950195,
            "name": "\u015eabr\u0101tah",
            "coord": {
                "Lon": 12.4885,
                "Lat": 32.7933
            },
            "main": {
                "temp": 48.61,
                "feels_like": 36.19,
                "temp_min": 48.61,
                "temp_max": 48.61,
                "pressure": 1023,
                "sea_level": 1023,
                "grnd_level": 1021,
                "humidity": 58
            },
            "visibility": 10000,
            "wind": {
                "speed": 16.374373657838227,
                "deg": 255
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ]
        },
        {
            "id": 2215163,
            "dt": 1610950195,
            "name": "Masall\u0101tah",
            "coord": {
                "Lon": 14,
                "Lat": 32.6167
            },
            "main": {
                "temp": 48.31,
                "feels_like": 31.57,
                "temp_min": 48.31,
                "temp_max": 48.31,
                "pressure": 1022,
                "sea_level": 1022,
                "grnd_level": 994,
                "humidity": 55
            },
            "visibility": 10000,
            "wind": {
                "speed": 23.62204724409449,
                "deg": 266
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ]
        },
        {
            "id": 2219905,
            "dt": 1610950194,
            "name": "Al Khums",
            "coord": {
                "Lon": 14.2619,
                "Lat": 32.6486
            },
            "main": {
                "temp": 53.51,
                "feels_like": 36.45,
                "temp_min": 53.51,
                "temp_max": 53.51,
                "pressure": 1022,
                "sea_level": 1022,
                "grnd_level": 1019,
                "humidity": 55
            },
            "visibility": 10000,
            "wind": {
                "speed": 25.590551181102363,
                "deg": 275
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ]
        },
        {
            "id": 2208425,
            "dt": 1610950195,
            "name": "Zuw\u0101rah",
            "coord": {
                "Lon": 12.082,
                "Lat": 32.9312
            },
            "main": {
                "temp": 50.45,
                "feels_like": 38.25,
                "temp_min": 50.45,
                "temp_max": 50.45,
                "pressure": 1023,
                "sea_level": 1023,
                "grnd_level": 1023,
                "humidity": 59
            },
            "visibility": 10000,
            "wind": {
                "speed": 16.642806012884755,
                "deg": 261
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ]
        },
        {
            "id": 2210221,
            "dt": 1610950195,
            "name": "Tarhuna",
            "coord": {
                "Lon": 13.6332,
                "Lat": 32.435
            },
            "main": {
                "temp": 44.94,
                "feels_like": 29.79,
                "temp_min": 44.94,
                "temp_max": 44.94,
                "pressure": 1023,
                "sea_level": 1023,
                "grnd_level": 975,
                "humidity": 58
            },
            "visibility": 10000,
            "wind": {
                "speed": 20.333750894774518,
                "deg": 265
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ]
        },
        {
            "id": 2208485,
            "dt": 1610950195,
            "name": "Zliten",
            "coord": {
                "Lon": 14.5687,
                "Lat": 32.4674
            },
            "main": {
                "temp": 53.26,
                "feels_like": 38.32,
                "temp_min": 53.26,
                "temp_max": 53.26,
                "pressure": 1022,
                "sea_level": 1022,
                "grnd_level": 1020,
                "humidity": 51
            },
            "visibility": 10000,
            "wind": {
                "speed": 21.161417322834648,
                "deg": 287
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ]
        },
        {
            "id": 2217362,
            "dt": 1610950194,
            "name": "Gharyan",
            "coord": {
                "Lon": 13.0203,
                "Lat": 32.1722
            },
            "main": {
                "temp": 41.56,
                "feels_like": 30.6,
                "temp_min": 41.56,
                "temp_max": 41.56,
                "pressure": 1024,
                "sea_level": 1024,
                "grnd_level": 941,
                "humidity": 65
            },
            "visibility": 10000,
            "wind": {
                "speed": 12.772906227630637,
                "deg": 252
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ]
        },
        {
            "id": 2523693,
            "dt": 1610950198,
            "name": "Pozzallo",
            "coord": {
                "Lon": 14.8499,
                "Lat": 36.7305
            },
            "main": {
                "temp": 42.8,
                "feels_like": 38.55,
                "temp_min": 42.8,
                "temp_max": 42.8,
                "pressure": 1014,
                "humidity": 100
            },
            "visibility": 10000,
            "wind": {
                "speed": 4.608088761632069,
                "deg": 120
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 40
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                }
            ]
        },
        {
            "id": 2524119,
            "dt": 1610950198,
            "name": "Modica",
            "coord": {
                "Lon": 14.774,
                "Lat": 36.8459
            },
            "main": {
                "temp": 42.8,
                "feels_like": 38.55,
                "temp_min": 42.8,
                "temp_max": 42.8,
                "pressure": 1014,
                "humidity": 100
            },
            "visibility": 10000,
            "wind": {
                "speed": 4.608088761632069,
                "deg": 120
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 40
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                }
            ]
        },
        {
            "id": 2208791,
            "dt": 1610950195,
            "name": "Yafran",
            "coord": {
                "Lon": 12.5286,
                "Lat": 32.0633
            },
            "main": {
                "temp": 41.29,
                "feels_like": 32.45,
                "temp_min": 41.29,
                "temp_max": 41.29,
                "pressure": 1024,
                "sea_level": 1024,
                "grnd_level": 943,
                "humidity": 65
            },
            "visibility": 10000,
            "wind": {
                "speed": 8.94774516821761,
                "deg": 254
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                }
            ]
        },
        {
            "id": 2523581,
            "dt": 1610950198,
            "name": "Rosolini",
            "coord": {
                "Lon": 14.9478,
                "Lat": 36.8242
            },
            "main": {
                "temp": 42.8,
                "feels_like": 38.55,
                "temp_min": 42.8,
                "temp_max": 42.8,
                "pressure": 1014,
                "humidity": 100
            },
            "visibility": 10000,
            "wind": {
                "speed": 4.608088761632069,
                "deg": 120
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 40
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                }
            ]
        },
        {
            "id": 2523650,
            "dt": 1610950198,
            "name": "Ragusa",
            "coord": {
                "Lon": 14.7172,
                "Lat": 36.9282
            },
            "main": {
                "temp": 42.8,
                "feels_like": 38.55,
                "temp_min": 42.8,
                "temp_max": 42.8,
                "pressure": 1014,
                "humidity": 100
            },
            "visibility": 10000,
            "wind": {
                "speed": 4.608088761632069,
                "deg": 120
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "today": 40
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                }
            ]
        }
    ]
}
```


<br>

### Cities in circle
API returns data from cities laid within definite circle
that is specified by center point (lat, lon)
and expected number of cities (count) around this point.

Example, use `WeatherAPI.current_weather_with_circle()`:
```
import json
from WeatherAPI import WeatherAPI

weather = WeatherAPI(api_key="<enter_your_api_key_here>")
circle_weather = weather.current_weather_with_circle(lat=55.5, lon=37.5, count=10)
print(json.dumps(circle_weather, indent=4))
```

Will will return a response with output:
```
{
    "message": "accurate",
    "cod": "200",
    "count": 10,
    "list": [
        {
            "id": 495260,
            "name": "Shcherbinka",
            "coord": {
                "lat": 55.4997,
                "lon": 37.5597
            },
            "main": {
                "temp": -8.86,
                "feels_like": -16.83,
                "temp_min": -9.4,
                "temp_max": -8,
                "pressure": 1017,
                "humidity": 84
            },
            "dt": 1610950151,
            "wind": {
                "speed": 2.24,
                "deg": 0
            },
            "sys": {
                "country": "RU"
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "all": 20
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ]
        },
        {
            "id": 564517,
            "name": "Dubrovitsy",
            "coord": {
                "lat": 55.4397,
                "lon": 37.4867
            },
            "main": {
                "temp": -8.88,
                "feels_like": -16.85,
                "temp_min": -9.4,
                "temp_max": -8,
                "pressure": 1017,
                "humidity": 84
            },
            "dt": 1610949926,
            "wind": {
                "speed": 2.24,
                "deg": 0
            },
            "sys": {
                "country": "RU"
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "all": 20
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ]
        },
        {
            "id": 570578,
            "name": "Butovo",
            "coord": {
                "lat": 55.5483,
                "lon": 37.5797
            },
            "main": {
                "temp": -8.88,
                "feels_like": -16.85,
                "temp_min": -9.4,
                "temp_max": -8,
                "pressure": 1017,
                "humidity": 84
            },
            "dt": 1610949926,
            "wind": {
                "speed": 2.24,
                "deg": 0
            },
            "sys": {
                "country": "RU"
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "all": 20
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ]
        },
        {
            "id": 545782,
            "name": "Kommunarka",
            "coord": {
                "lat": 55.5695,
                "lon": 37.4893
            },
            "main": {
                "temp": -8.91,
                "feels_like": -16.89,
                "temp_min": -9.4,
                "temp_max": -8,
                "pressure": 1017,
                "humidity": 84
            },
            "dt": 1610949924,
            "wind": {
                "speed": 2.24,
                "deg": 0
            },
            "sys": {
                "country": "RU"
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "all": 20
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ]
        },
        {
            "id": 6417490,
            "name": "Lesparkkhoz",
            "coord": {
                "lat": 55.5431,
                "lon": 37.6014
            },
            "main": {
                "temp": -9.08,
                "feels_like": -18.31,
                "temp_min": -11.2,
                "temp_max": -7.6,
                "pressure": 1017,
                "humidity": 84
            },
            "dt": 1610950453,
            "wind": {
                "speed": 4.47,
                "deg": 320
            },
            "sys": {
                "country": "RU"
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "all": 0
            },
            "weather": [
                {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                }
            ]
        },
        {
            "id": 526736,
            "name": "Sed\u2019moy Mikrorayon",
            "coord": {
                "lat": 55.5622,
                "lon": 37.5797
            },
            "main": {
                "temp": -8.9,
                "feels_like": -16.87,
                "temp_min": -9.4,
                "temp_max": -8,
                "pressure": 1017,
                "humidity": 84
            },
            "dt": 1610949915,
            "wind": {
                "speed": 2.24,
                "deg": 0
            },
            "sys": {
                "country": "RU"
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "all": 20
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ]
        },
        {
            "id": 473051,
            "name": "Vlas\u2019yevo",
            "coord": {
                "lat": 55.4603,
                "lon": 37.3794
            },
            "main": {
                "temp": -8.9,
                "feels_like": -16.87,
                "temp_min": -9.4,
                "temp_max": -8,
                "pressure": 1017,
                "humidity": 84
            },
            "dt": 1610949919,
            "wind": {
                "speed": 2.24,
                "deg": 0
            },
            "sys": {
                "country": "RU"
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "all": 20
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ]
        },
        {
            "id": 578680,
            "name": "Bachurino",
            "coord": {
                "lat": 55.58,
                "lon": 37.52
            },
            "main": {
                "temp": -8.91,
                "feels_like": -16.89,
                "temp_min": -9.4,
                "temp_max": -8,
                "pressure": 1017,
                "humidity": 84
            },
            "dt": 1610949927,
            "wind": {
                "speed": 2.24,
                "deg": 0
            },
            "sys": {
                "country": "RU"
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "all": 20
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ]
        },
        {
            "id": 554629,
            "name": "Shestoy Mikrorayon",
            "coord": {
                "lat": 55.5667,
                "lon": 37.5833
            },
            "main": {
                "temp": -8.9,
                "feels_like": -16.87,
                "temp_min": -9.4,
                "temp_max": -8,
                "pressure": 1017,
                "humidity": 84
            },
            "dt": 1610949925,
            "wind": {
                "speed": 2.24,
                "deg": 0
            },
            "sys": {
                "country": "RU"
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "all": 20
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ]
        },
        {
            "id": 508101,
            "name": "Podolsk",
            "coord": {
                "lat": 55.4242,
                "lon": 37.5547
            },
            "main": {
                "temp": -11.09,
                "feels_like": -19.12,
                "temp_min": -17,
                "temp_max": -8,
                "pressure": 1017,
                "humidity": 84
            },
            "dt": 1610950152,
            "wind": {
                "speed": 2.24,
                "deg": 0
            },
            "sys": {
                "country": "RU"
            },
            "rain": null,
            "snow": null,
            "clouds": {
                "all": 20
            },
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ]
        }
    ]
}
```

<br>


### Call for several city IDs
There is a possibility to get current weather data for several cities by making one API call.

Example, use `WeatherAPI.current_weather_with_circle()`:

> Please note that a single City ID counts as one API call. So, the above example is treated as a 3 API calls.

```
import json
from WeatherAPI import WeatherAPI

weather = WeatherAPI(api_key="<enter_your_api_key_here>")
data = weather.current_weather_with_several_city_ids(city_id_list=[524901,703448,2643743])
print(json.dumps(data, indent=4))
```

Will will return a response with output:

```
{
    "cnt": 3,
    "list": [
        {
            "coord": {
                "lon": 37.6156,
                "lat": 55.7522
            },
            "sys": {
                "country": "RU",
                "timezone": 10800,
                "sunrise": 1610948741,
                "sunset": 1610976829
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "main": {
                "temp": -9.49,
                "feels_like": -17.48,
                "temp_min": -11.2,
                "temp_max": -8,
                "pressure": 1016,
                "humidity": 84
            },
            "visibility": 9000,
            "wind": {
                "speed": 2.24,
                "deg": 0
            },
            "clouds": {
                "all": 72
            },
            "dt": 1610950080,
            "id": 524901,
            "name": "Moscow"
        },
        {
            "coord": {
                "lon": 30.5167,
                "lat": 50.4333
            },
            "sys": {
                "country": "UA",
                "timezone": 7200,
                "sunrise": 1610948979,
                "sunset": 1610979999
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "main": {
                "temp": -5.66,
                "feels_like": -16.06,
                "temp_min": -11.2,
                "temp_max": -2.2,
                "pressure": 1016,
                "humidity": 84
            },
            "visibility": 8000,
            "wind": {
                "speed": 6.71,
                "deg": 300
            },
            "clouds": {
                "all": 92
            },
            "dt": 1610950162,
            "id": 703448,
            "name": "Kyiv"
        },
        {
            "coord": {
                "lon": -0.1257,
                "lat": 51.5085
            },
            "sys": {
                "country": "GB",
                "timezone": 0,
                "sunrise": 1610956591,
                "sunset": 1610987099
            },
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                }
            ],
            "main": {
                "temp": 37.2,
                "feels_like": 29.98,
                "temp_min": 35.01,
                "temp_max": 39.2,
                "pressure": 1024,
                "humidity": 87
            },
            "visibility": 10000,
            "wind": {
                "speed": 6.91,
                "deg": 240
            },
            "clouds": {
                "all": 52
            },
            "dt": 1610950198,
            "id": 2643743,
            "name": "London"
        }
    ]
}
```

<hr>

# Weather fields in API Response

## JSON
Example of API response
```
                          

{
  "coord": {
    "lon": -122.08,
    "lat": 37.39
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.55,
    "feels_like": 281.86,
    "temp_min": 280.37,
    "temp_max": 284.26,
    "pressure": 1023,
    "humidity": 100
  },
  "visibility": 16093,
  "wind": {
    "speed": 1.5,
    "deg": 350
  },
  "clouds": {
    "all": 1
  },
  "dt": 1560350645,
  "sys": {
    "type": 1,
    "id": 5122,
    "message": 0.0139,
    "country": "US",
    "sunrise": 1560343627,
    "sunset": 1560396563
  },
  "timezone": -25200,
  "id": 420006353,
  "name": "Mountain View",
  "cod": 200
  }                         
```

## Fields in API response
- `coord`
  - `coord.lon`:  City geo location, longitude
  - `coord.lat`:  City geo location, latitude
- `weather` (more info Weather condition codes)
  - `weather.id`:    Weather condition id
  - `weather.main`:   Group of weather parameters (Rain, Snow, Extreme etc.)
  - `weather.description`:    Weather condition within the group. You can get the output in your language.
  - `weather.icon`:   Weather icon id
- `base`: Internal parameter
- `main`
  - `main.temp`:  Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit
  - `man.feels_like`: Temperature. This teperature paremter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit
  - `main.pressure`:  Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level). hPa
  - `main.humidity`:  Humidity %
  - `main.temp_min`:  Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit
  - `main.temp_max`:   Maximum temperature at the monent. This is maximal currently observed temperature (within large megalopolises and urban areas). Units Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
  - `main.sea_level`: Atmospheric pressure on the seal leve. hPa
  - `main.grnd_level`:    Atmospheric pressure on the ground level. hPa
- `wind`
  - `wind.speed`: Wind speed. Unit Default: meter/sec, Metic: meter/sec, Imperial: miles/hour
  - `wind.deg`: Wind direction, degrees (metorological)
  - `wind.gust`:    Wind gust. nit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
- `clouds`
  - `clouds.all`:   Cloudiness, %
- `rain`
  - `rain.1h`:  Rain volume for the last 1 hour, mm
  - `rain.3h`:  Rain volume for the last 3 hours, mm
- `snow`
  - `snow.1h`:  Snow volume for the last 1 hour, mm
  - `snow.3h`:  Snow volume for the last 3 hours, mm
- `dt`: Time fo date calculation, unix, UTC
- `sys`
  - `sys.type`: Internal parameter
  - `sys.id`:   Internal parameter
  - `sys.message`:  Internal parameter
  - `sys.country`:  Country code (GB, JP etc.)
  - `sys.sunrise`:  Sunrise time, unix, UTC
  - `sys.sunset`:   Snset time, unix, UTC
- `timezone`: Shift in seconds from UTC
- `id`:   City ID
- `name`: City Name
- `cod`:  Internal parameter

<hr>

# Hourly Forecast
**NOT WORKING**
Hourly forecast by OpenWeatherMap! 
Hourly forecast for 4 days, with 96 timestamps and higher geographic accuracy.

## Call hourly forecast data by city name
You can search weather forecast for 4 days (96 hours) with data every hour by city name. 
All weather data can be obtained in JSON and XML formats.

<hr>

# Air Polution API

## Current Air Polution Data
Example, use `WeatherAPI.current_air_pollution_data()`:
```
import json
from WeatherAPI import WeatherAPI

weather = WeatherAPI(api_key="<enter_your_api_key_here>")
current_air_pollution = weather.current_air_pollution_data(lat=29, lon=-98)
print(json.dumps(current_air_pollution, indent=4))
```

Response Output:
```
{
    "coord": {
        "lon": -98,
        "lat": 29
    },
    "list": [
        {
            "main": {
                "aqi": 1
            },
            "components": {
                "co": 223.64,
                "no": 0,
                "no2": 2.59,
                "o3": 36.12,
                "so2": 0.07,
                "pm2_5": 5.73,
                "pm10": 8.01,
                "nh3": 0.48
            },
            "dt": 1610956800
        }
    ]
}
```

<br>

## Forecast air pollution data
Example, use `WeatherAPI.forecast_air_pollution_data()`:
```
import json
from WeatherAPI import WeatherAPI

weather = WeatherAPI(api_key="<enter_your_api_key_here>")
forecast_air_pollution = weather.forecast_air_pollution_data(lat=29, lon=-98)
print(json.dumps(forecast_air_pollution, indent=4))
```

Response Output:
```
{
    "coord": {
        "lon": -98,
        "lat": 29
    },
    "list": [
        {
            "main": {
                "aqi": 1
            },
            "components": {
                "co": 226.97,
                "no": 0.07,
                "no2": 4.46,
                "o3": 79.39,
                "so2": 1.82,
                "pm2_5": 1.36,
                "pm10": 2.52,
                "nh3": 1.06
            },
            "dt": 1610755200
        },
        
        ...
        ...

        {
            "main": {
                "aqi": 1
            },
            "components": {
                "co": 250.34,
                "no": 0.1,
                "no2": 5.01,
                "o3": 24.68,
                "so2": 0.18,
                "pm2_5": 7.6,
                "pm10": 9.91,
                "nh3": 1.27
            },
            "dt": 1611360000
        }
    ]
}
```

<br>

## Historical air pollution data
Example, use `WeatherAPI.historical_air_pollution_data()`:
```
import json
from WeatherAPI import WeatherAPI

weather = WeatherAPI(api_key="<enter_your_api_key_here>")
historical_air_pollution_data = weather.historical_air_pollution_data(lat=29, lon=-98, start=1606223802, end=1606482999)
print(json.dumps(historical_air_pollution_data, indent=4))
```

Response Output:
```
{
    "coord": {
        "lon": -98,
        "lat": 29
    },
    "list": [
        {
            "main": {
                "aqi": 1
            },
            "components": {
                "co": 173.57,
                "no": 0,
                "no2": 0.74,
                "o3": 33.62,
                "so2": 0.16,
                "pm2_5": 4.24,
                "pm10": 7.43,
                "nh3": 0.19
            },
            "dt": 1606482000
        },

        ...
        ...

        {
            "main": {
                "aqi": 1
            },
            "components": {
                "co": 178.58,
                "no": 0,
                "no2": 2.31,
                "o3": 72.24,
                "so2": 1.21,
                "pm2_5": 6.19,
                "pm10": 11.21,
                "nh3": 0.07
            },
            "dt": 1606266000
        }
    ]
}

```

<hr>

## Air Pollution API Response

Response:
```
{
  "coord":[
    50,
    50
  ],
  "list":[
    {
      "dt":1605182400,
      "main":{
        "aqi":1
      },
      "components":{
        "co":201.94053649902344,
        "no":0.01877197064459324,
        "no2":0.7711350917816162,
        "o3":68.66455078125,
        "so2":0.6407499313354492,
        "pm2_5":0.5,
        "pm10":0.540438711643219,
        "nh3":0.12369127571582794
      }
    }
  ]
} 
```

## Fields in API Response
- `coord`: Coordinates from the specified locaiton (latitude longitude)
- `list`
  - `dt`:   Date and time, Unix, UTC
  - `main`:
    - `main.aqi`: Air Quality Index. Possible Values: 1, 2, 3, 4, 5.
        Where 1 = Good, 2 = Fair, 3 = Moderate, 4 = Poor, 5 = Very Poor
  - `components`
    - `components.co`:      Concetration of CO (Carbon monoxide), μg/m3
    - `components.no`:      Conentration of NO (Nitrogen monoxide) , μg/m3
    - `components.no2`:     Concentration of NO2 (Nitrogen dioxide), μg/m3
    - `components.o3`:      Сoncentration of O3 (Ozone), μg/m3
    - `components.so2`:     Сoncentration of SO2 (Sulphur dioxide), μg/m3
    - `components.pm2_5`:   Сoncentration of PM2.5 (Fine particles matter), μg/m3
    - `components.pm10`:    Сoncentration of PM10 (Coarse particulate matter), μg/m3
    - `components.nh3`:     Сoncentration of NH3 (Ammonia), μg/m3