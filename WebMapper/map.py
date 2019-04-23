import folium

def main():
    nybase = folium.Map(location = [40.730610, -73.935242])
    nybase.save("nyBaseMap.html")

if __name__ == "__main__":
    main()