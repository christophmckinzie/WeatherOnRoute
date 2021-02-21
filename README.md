# WeatherOnRoute

This project uses a custom Python3 class with Google Maps API and OpenWeatherMaps API to find weather on your route. I created it because I thought it would be helpful for determining if it would be safe to travel to my parents house which is over a moutain pass. 

The GUI is built using PyQt5 which is a set of Python bindings for v5 of the Qt application framework from The Qt Company.

As it stands the programs takes a parameter 'number of checks' which divides the route evenly between that number and checks those locations for the specified weather. This obviously isnt the best way to do it as you would want a database to check against your route or something. The other issue I am having is that the folium maps pop ups hyperlinks are not working. 

![alt text](https://github.com/christophmckinzie/WeatherOnRoute/blob/main/weatherapp.png)
