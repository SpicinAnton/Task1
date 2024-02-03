import sys
from geocoder import get_ll_span
from mapapi_PG import show_map

toponym_to_find = " ".join(sys.argv[1:])

if toponym_to_find:
    ll, spn = get_ll_span(toponym_to_find)
    add_params = f"pt={ll}"
    ll_span = f'll={ll}&spn={spn}'
    show_map(ll_spn=ll_span, map_type="map")

else:
    print('No toponym')