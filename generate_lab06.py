import folium

locations = [
    {"name": "Stanley's Famous Pit Barbecue", "lat": 32.3432, "lng": -95.2943, "type": "Restaurant", "description": "A Tyler institution since 1958."},
    {"name": "Tyler Rose Garden", "lat": 32.3519, "lng": -95.3102, "type": "Cultural", "description": "The largest rose garden in the US."},
    {"name": "Caldwell Zoo", "lat": 32.3681, "lng": -95.3189, "type": "Recreation", "description": "One of the best small-city zoos in the country."},
    {"name": "Tyler State Park", "lat": 32.4617, "lng": -95.2697, "type": "Park", "description": "Thick pine forest and a spring-fed lake."},
    {"name": "True Vine Brewing Company", "lat": 32.3754, "lng": -95.3301, "type": "Restaurant", "description": "Tyler's best craft brewery."},
    {"name": "The Grove Kitchen & Gardens", "lat": 32.3198, "lng": -95.3354, "type": "Restaurant", "description": "Farm-to-table dining on a garden patio."},
    {"name": "Goodman-LeGrand House", "lat": 32.3541, "lng": -95.2972, "type": "Historical", "description": "A preserved 1859 antebellum home."},
    {"name": "University of Texas at Tyler", "lat": 32.3293, "lng": -95.2625, "type": "School", "description": "UT Tyler's wooded campus."},
    {"name": "Rose Rudman Trail", "lat": 32.3387, "lng": -95.3012, "type": "Park", "description": "A beloved trail through pine forest."},
    {"name": "Tiger Creek Wildlife Refuge", "lat": 32.4198, "lng": -95.2341, "type": "Cultural", "description": "A sanctuary for rescued big cats."},
]

color_map = {"Restaurant": "red", "Cultural": "purple", "Recreation": "orange", "Park": "green", "Historical": "darkred", "School": "blue"}

m = folium.Map(location=[32.3513, -95.3011], zoom_start=12, tiles="OpenStreetMap")

for loc in locations:
    color = color_map.get(loc["type"], "gray")
    popup_html = f"<div style='font-family:Georgia,serif;max-width:200px;'><strong style='color:#2c3e6b;'>{loc['name']}</strong><br><em style='font-size:0.8rem;color:#888;'>{loc['type']}</em><br><br><span style='font-size:0.85rem;'>{loc['description']}</span></div>"
    folium.CircleMarker(location=[loc["lat"], loc["lng"]], radius=9, color="white", weight=2, fill=True, fill_color=color, fill_opacity=0.85, popup=folium.Popup(popup_html, max_width=220), tooltip=loc["name"]).add_to(m)

m.save("hometown_map.html")
print("Done!")
