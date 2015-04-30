__author__ = 'alexmcneill'
import threading
import urllib2
import json


class WeatherProcess(threading.Thread):

    _metservice_base = 'http://metservice.com/publicData/'
    _daily_forecast = 'climateDataDailyTown_{0}_32'

    def __init__(self, city_name):
        threading.Thread.__init__(self)
        self.city_name = city_name
        self.weather = None
        self.url = self._metservice_base + self._daily_forecast.format(city_name)

    def get_response(self, url):
        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError:
            return None
        return json.loads(response.read())

    def run(self):
        self.weather = self.get_response(self.url)

if __name__ == "__main__":
    weather_processes = []

    for i in range(3):
        city_name = raw_input("Please enter a city: ")
        current = WeatherProcess(city_name)
        weather_processes.append(current)
        current.start()

    for process in weather_processes:
        process.join()
        print(process.weather)