import sys
from io import BytesIO
from geocoder import *
import requests
from PIL import Image

toponym_to_find = " ".join(sys.argv[1:])
if toponym_to_find:
    ll,spn=get_ll_span(toponym_to_find)
    map_params = {
        "ll": ll,
        "spn": spn,
        "l": "map",
        'pt': ll
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    Image.open(BytesIO(
        response.content)).show()