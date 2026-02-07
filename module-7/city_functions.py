## Modified function to include population & language
def city_country(city, country, population=None, language=None): 
    """Return a string like 'Santiago, Chile - population 5000000'."""
    output = f"{city.title()}, {country.title()}"
    if population:
        output += f" - population {population}"
    if language:
        output += f" - language {language}"
    return output

## Calling the function three times
print(city_country('santiago', 'chile'))
print(city_country('santiago', 'chile', population=5_000_000))
print(city_country('santiago', 'chile', population=5_000_000, language='spanish'))