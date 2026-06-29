import folium

a = folium.Map(location=(55.169438, 23.881275), zoom_start= 12, control_scale = True)

folium.Marker(location =(56.1667, 24.2108), tooltip='Cidade', popup='Vaškai', icon=folium.Icon(icon="cloud")).add_to(a)
folium.Marker(location =(56.06251, 24.39965), tooltip='Cidade', popup='Pasvalys', icon=folium.Icon(color="green")).add_to(a)
a.save("index.html")

a