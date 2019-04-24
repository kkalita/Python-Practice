import folium
import pandas

def main():

    mapdata = pandas.read_csv("Volcanoes.txt")
    lat = list(mapdata["LAT"])
    lon = list(mapdata["LON"])
    elev = list(mapdata["ELEV"])

    nybase = folium.Map(location = [40.730610, -73.935242], zoom_start = 5, tiles = "Mapbox Bright")
    fg = folium.FeatureGroup(name = "demoMap")

    for lt, ln, el in zip(lat, lon, elev):
        fg.add_child(folium.Marker(location = [lt, ln], popup = str(el) + " m"))
    
    nybase.add_child(fg)


    nybase.save("nyBaseMap.html")

if __name__ == "__main__":
    main()