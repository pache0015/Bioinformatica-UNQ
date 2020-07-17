#Mapa - Modelo
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="TP FINAL Bioinformatica")
import folium
from folium.plugins import MiniMap
from folium.plugins import MousePosition
import PySimpleGUI as sg
import io
from PIL import Image
from geopy.geocoders import Nominatim
import Bio.SeqIO as SeqIO

class UbicacionNotFound(Exception):
    def __init__(self, nombre_ubicacion):
        super().__init__(f"La ubicación {nombre_ubicacion} no es válida")

class NotUbicacion(Exception):
    def __init__(self, nombre_ubicacion):
        super().__init__("En el archivo cargado no hay ubicaciones")

class Mapa:
    def __init__(self):
        self.points = []
        self.my_map = folium.Map(
            zoom_start = 12,
            control_scale=True,
            world_copy_jump=False,
            no_wrap=False
        )
        
       
    def armar_mapa(self, ubicaciones):
        n = 1
        if not ubicaciones:
            raise NotUbicacion
        for nombre_ubicacion in ubicaciones:
            geolocator = Nominatim(user_agent="TP FINAL Bioinformatica")
            ubicacion = geolocator.geocode(nombre_ubicacion)
            if ubicacion == None:
                raise UbicacionNotFound(nombre_ubicacion)
            point = (ubicacion.latitude, ubicacion.longitude)
            self.points.append(point)
            folium.Marker(
                location = [point[0], point[1]],
                icon = folium.Icon(color='red', icon='cloud'),
                popup= f'Ubicacion: {nombre_ubicacion}',
                tooltip = n
            ).add_to(self.my_map)
            n = n + 1
        return self

    def guardar_mapa(self):
        self.my_map.save("Mapa final")

    def render_mapa(self):
        MousePosition().add_to(self.my_map)
        folium.PolyLine(self.points).add_to(self.my_map)
        minimap = MiniMap()
        self.my_map.add_child(minimap)
        self.guardar_mapa()
        display(self.my_map)
        return self.my_map
