from pygal_maps_world.maps import COUNTRIES


def get_country_code(country_name):
    # Check for specific countries in the COUNTRIES dictionary
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    return None
