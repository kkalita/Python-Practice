import folium
import pandas

def colorCat(n):
    if n < 1000: 
        return 'green'
    elif n < 2000: 
        return 'orange'
    else:
        return 'red'

def main():
    mapdata = pandas.read_csv("Volcanoes.txt")
    lat = list(mapdata["LAT"])
    lon = list(mapdata["LON"])
    elev = list(mapdata["ELEV"])

    nybase = folium.Map(location = [40.730610, -73.935242], zoom_start = 5, tiles = "Mapbox Bright")
    fgv = folium.FeatureGroup(name = "Volcano")

    for lt, ln, el in zip(lat, lon, elev):
        fgv.add_child(folium.CircleMarker(location = [lt, ln], radius = 7, popup = str(el) + " m",
        fill_color = colorCat(el), color = 'grey', fill_opacity = 0.7)) 

    fgp = folium.FeatureGroup(name = "Country Population")


    fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), 
    style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'yellow'
    if x['properties']['POP2005'] < 50000000 else 'orange' }))

    nybase.add_child(fgv)
    nybase.add_child(fgp)
    nybase.add_child(folium.LayerControl())


    nybase.save("nyBaseMap.html")

if __name__ == "__main__":
    main()