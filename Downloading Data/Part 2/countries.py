from pygal_maps_world.maps import COUNTRIES

for country_code in sorted(COUNTRIES):
    print(country_code, COUNTRIES[country_code])
