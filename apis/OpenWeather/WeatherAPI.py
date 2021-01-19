import datetime
import json
import requests
from json.decoder import JSONDecodeError

class WeatherAPI:
    def __init__(self, api_key:str):
        self.api_key = api_key
        self.logger = None
        self.base_url = "https://api.openweathermap.org/data/2.5"


    def send_request(self, request_url:str):
        print ("sending request to:\t{url}".format(url=request_url))
        try:
            response = requests.get(url=request_url, timeout=30)
            return response.json()
        except JSONDecodeError as err:
            print ("JSON response error, returning raw text.")
            return response.text
        except TypeError as err:
            return response.text


    ################################################
    # Current Weather Data
    # source: https://openweathermap.org/current
    ################################################

    def current_weather_by_city_name(self, city_name:str, state_code:str=None, country_code:str=None, units:str="imperial"):
        """
        Returns current weather (JSON) from the location of the given city name.

        INPUT:
            - city_name (string - REQUIRED):        City Name
            - state_code (string - OPTIONAL):       State Code
            - country_code (string - OPTIONAL):     Country Code
            - units   (strings - OPTIONAL):         Units of measurement (defaults to "imperial"). 
                - standard, metric, imperial
        """
        if state_code and country_code:
            url = "{base_url}/weather?q={city},{state},{country}&units={units}&appid={api_key}".format(base_url=self.base_url, city=city_name, state=state_code, country=country_code, units=units, api_key=self.api_key)
        elif state_code:
            url = "{base_url}/weather?q={city},{state}&units={units}&appid={api_key}".format(base_url=self.base_url, city=city_name, state=state_code, units=units, api_key=self.api_key)
        else:
            url = "{base_url}/weather?q={city}&units={units}&appid={api_key}".format(base_url=self.base_url, city=city_name, units=units, api_key=self.api_key)
        return self.send_request(request_url=url)


    def current_weather_by_city_id(self, city_id:int, units:str="imperial"):
        """
        Returns current weather (JSON) from the location of the given city id.
        The City ID can be found from a list within the "city.list.json" file.

        INPUT:
            - city_id (integer - REQUIRED): City ID number
            - units   (strings - OPTIONAL): Units of measurement (defaults to "imperial"). 
                - standard, metric, imperial
        """
        url = "{base_url}/weather?id={city_id}&units={units}&appid={api_key}".format(base_url=self.base_url, city_id=city_id, units=units, api_key=self.api_key)
        return self.send_request(request_url=url)


    def current_weather_by_geo_coordinates(self, lat:int, lon:int, units:str="imperial"):
        """
        Returns current weather (JSON) from the location of the given geographic coordinates.

        INPUT:
            - lat (string - REQUIRED): latitude
            - lon (string - REQUIRED): longitude
            - units (strings - OPTIONAL): Units of measurement. Defaults to "imperial".
                - standard, metric, imperial
        """
        url = "{base_url}/weather?lat={lat}&lon={lon}&units={units}&appid={api_key}".format(base_url=self.base_url, lat=lat, lon=lon, units=units, api_key=self.api_key)
        return self.send_request(request_url=url)


    def current_weather_by_zip_code(self, zip_code:int, country_code:str=None, units:str="imperial"):
        """
        Returns current weather (JSON) from the location of the given the ZIP code.

        INPUT:
            - zip_code (integer - REQUIRED): ZIP code of location
            - country_code (string - OPTIONAL): Country Code
            - units (strings - OPTIONAL): Units of measurement. Defaults to "imperial".
                - standard, metric, imperial
        """
        url = "{base_url}/weather?zip={zip_code}&units={units}&appid={api_key}".format(base_url=self.base_url, zip_code=zip_code, units=units, api_key=self.api_key)
        if country_code:
            url = "{base_url}/weather?zip={zip_code},{country_code}&units={units}&appid={api_key}".format(base_url=self.base_url, zip_code=zip_code, country_code=country_code, units=units, api_key=self.api_key)
        return self.send_request(request_url=url)


    def current_weather_with_bound_box(self, lon_left:int, lat_bottom:int, lon_right:int, lat_top:int, zoom:int=10, units:str="imperial"):
        """
        API returns the data from cities within the defined rectangle specified by the geographic coordinates.

        INPUT:
            - lon_left (integer - REQIURED):    longitude left
            - lat_bottom (integer - REQIURED):  latitude bottom
            - long_right (integer - REQIURED):  longitude right
            - lat_top (integer - REQIURED):     latitude top
            - zoom (integer - REQIURED):        defaults to 10
            - units (strings - OPTIONAL):       Units of measurement. Defaults to "imperial".
                - standard, metric, imperial

        EXAMPLE:    api.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&appid={API key}
        """
        bbox = [lon_left, lat_bottom, lon_right, lat_top, zoom]
        url = "{base_url}/box/city?bbox={bbox}&units={units}&appid={api_key}".format(base_url=self.base_url, bbox=','.join(map(str, bbox)), units=units, api_key=self.api_key)
        return self.send_request(request_url=url)


    def current_weather_with_circle(self, lat:int, lon:int, count:int, units:str="imperial"):
        """
        API returns data from cities laid within definite circle that is specified by center point (lat, lon)
        and expected number of cities (count) around this point.

        INPUT:
            - lat (integer - REQUIRED): latitude
            - lon (integer - REQUIRED): longitude
            - cont (integer - REQUIRED): number of cities around (lat, lon) point
            - units (strings - OPTIONAL): Units of measurement. Defaults to "imperial".
                - standard, metric, imperial

        EXAMPLE: api.openweathermap.org/data/2.5/find?lat=55.5&lon=37.5&cnt=10&appid={API key}
        """
        url = "{base_url}/find?lat={lat}&lon={lon}&cnt={cnt}&units={units}&appid={api_key}".format(base_url=self.base_url, lat=lat, lon=lon, cnt=count, units=units, api_key=self.api_key)
        return self.send_request(request_url=url)

    
    def current_weather_with_several_city_ids(self, city_id_list:list, units:str="imperial"):
        """
        There is a possibility to get current weather data for several cities by making one API call.
        
        INPUT:
            - city_id_list (list of integers - REQUIRED): City ID. List of city ID (use city.lsit.json file for list of city IDs).
                - The limit of locations is 20.

            - units (strings - OPTIONAL): Units of measurement. Defaults to "imperial".
                - standard, metric, imperial
        EXAMPLE: api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&appid={API key}
        """
        url = "{base_url}/group?id={city_ids}&units={units}&appid={api_key}".format(base_url=self.base_url, city_ids=','.join(map(str, city_id_list)), units=units, api_key=self.api_key)
        return self.send_request(request_url=url)

    ################################################
    # End Current Weather Data
    ################################################



    ################################################
    # Hourly forecast
    # source: https://openweathermap.org/api/hourly-forecast
    ################################################
    def get_hourly_forecast_by_city_name(self, city_name:str, units:str="imperial"):
        """
        NOT WORKING -- RETURNING 401 INVALID API KEY
        You can search weather forecast for 4 days (96 hours) with data every hour by city name. 

        INPUT:


        """
        url = "https://pro.openweathermap.org/data/2.5/forecast/hourly?q={city_name}&appid={api_key}".format(city_name=city_name, api_key=self.api_key)
        return self.send_request(request_url=url)
    

    def get_hourly_forecast_by_zip_code(self, zip_code:int, country_code:str=None, units:str="imperial"):
        """
        NOT WORKING -- RETURNING 401 INVALID API KEY
        """
        url = "https://pro.openweathermap.org/data/2.5/forecast/hourly?zip={zip_code}&appid={api_key}".format(zip_code=zip_code, api_key=self.api_key)
        if country_code:
            url = "https://pro.openweathermap.org/data/2.5/forecast/hourly?zip={zip_code},{country_code}&appid={api_key}".format(zip_code=zip_code, country_code=country_code, api_key=self.api_key)
        return self.send_request(request_url=url)


    ################################################
    # Daily Forecast 16 Days
    # source: https://openweathermap.org/forecast16
    ################################################
    def daily_forecast_data_by_city_name(self, city_name:str=None, state_code:str=None, contry_code:str=None, cnt:int=10, units:str="imperial"):
        """
        NOT WORKING -- 401 Invalid API key
        You can search 16 day weather forecast with daily average parameters by city name.
        
        INPUT:
            - city_name (string - REQUIRED):        City Name
            - state_code (string - OPTIONAL):       State Code
            - country_code (string - OPTIONAL):     Country Code
            - units   (strings - OPTIONAL):         Units of measurement (defaults to "imperial"). 
                - standard, metric, imperial
        Example: api.openweathermap.org/data/2.5/forecast/daily?q=London&mode=xml&units=metric&cnt=7&appid={API key}
        """
        if state_code and country_code:
            url = "{base_url}/forecast/daily?q={city_name},{state_code},{country_code}&cnt={cnt}&units={units}appid={api_key}".format(base_url=self.base_url, city_name=city_name, state_code=state_code, country_code=country_code, cnt=cnt, units=units, api_key=self.api_key)
        elif state_code:
            url = "{base_url}/forecast/daily?q={city_name},{state_code}&cnt={cnt}&units={units}&appid={api_key}".format(base_url=self.base_url, city_name=city_name, state=state_code, cnt=cnt, units=units, api_key=self.api_key)
        else:
            url = "{base_url}/forecast/daily?q={city_name}&cnt={cnt}&units={units}&appid={api_key}".format(base_url=self.base_url, city_name=city_name, cnt=cnt, units=units, api_key=self.api_key)
        return self.send_request(request_url=url)

            
    ################################################
    # AIR POLLUTION
    # source: https://openweathermap.org/api/air-pollution
    ################################################

    def current_air_pollution_data(self, lat:int, lon:int):
        """
        INPUT:
            - lat (integer - REQUIRED): Geographical coordinates (latitude)
            - lon (integer - REQUIRED): Geographical coordinates (longitude)
        EXAMPLE: http://api.openweathermap.org/data/2.5/air_pollution?lat=50&lon=50&appid={API key}
        """
        url = "{base_url}/air_pollution?lat={lat}&lon={lon}&appid={api_key}".format(base_url=self.base_url, lat=lat, lon=lon, api_key=self.api_key)
        return self.send_request(request_url=url)

    def forecast_air_pollution_data(self, lat:int, lon:int):
        """
        INPUT:
            - lat (integer - REQUIRED): Geographical coordinates (latitude)
            - lon (integer - REQUIRED): Geographical coordinates (longitude)
        EXAMPLE: http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat=50&lon=50&appid={API key}
        """
        url = "{base_url}/air_pollution/forecast?lat={lat}&lon={lon}&appid={api_key}".format(base_url=self.base_url, lat=lat, lon=lon, api_key=self.api_key)
        return self.send_request(request_url=url)


    def historical_air_pollution_data(self, lat:int, lon:int, start:int, end:int):
        """
        INPUT:
            - lat (integer - REQUIRED):     Geographical coordinates (latitude)
            - lon (integer - REQUIRED):     Geographical coordinates (longitude)
            - start (integer - REQUIRED):   Start date (unix time, UTC time zone), e.g. start=1606488670
            - end (integer - REQUIRED):     End date (unix time, UTC time zone), e.g. start=1606747870
        EXAMPLE: http://api.openweathermap.org/data/2.5/air_pollution/history?lat=508&lon=50&start=1606223802&end=1606482999&appid={API key}
        """
        url = "{base_url}/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={api_key}".format(base_url=self.base_url, lat=lat, lon=lon, start=start, end=end, api_key=self.api_key)
        return self.send_request(request_url=url)

if __name__ == '__main__':

    data = {}
    weather = WeatherAPI(api_key="<enter_api_key_here>")

    # Test Get Current Weather:
    #phx_weather = weather.current_weather_by_city_id(city_id=5308655)
    #phx_weather = weather.current_weather_by_geo_coordinates(lat=33.4484, lon=-112.074)
    #sa_weather = weather.current_weather_by_zip_code(zip_code=78232)
    #sa_weather = weather.current_weather_by_zip_code(zip_code=78205, country_code="US")
    #data = weather.current_weather_with_bound_box(lon_left=12, lat_bottom=32, lon_right=15, lat_top=37, zoom=10)
    #data = weather.current_weather_with_circle(lat=55.5, lon=37.5, count=10)
    #data = weather.current_weather_with_several_city_ids(city_id_list=[524901,703448,2643743])

    # Test Get Hourly Forecast
    # TODO: THESE ARE NOT WORKING -- RETURNING 401 INVALID API KEY
    #data = weather.get_hourly_forecast_by_city_name(city_name="Tucson")
    #data = weather.get_hourly_forecast_by_zip_code(zip_code=78232)
    

    # Get Forecast 16 day
    # TODO: THESE ARE NOT WORKING -- RETURNING 401 INVALID API KEY
    #data = weather.daily_forecast_data_by_city_name(city_name="Houston", cnt=10)

    # Test Air Pollution Forecast
    #data = weather.current_air_pollution_data(lat=29, lon=-98)
    #data = weather.forecast_air_pollution_data(lat=29, lon=-98)
    #data = weather.historical_air_pollution_data(lat=29, lon=-98, start=1606223802, end=1606482999)

    print(json.dumps(data, indent=4))
    
    