# Import countryinfo module.
from countryinfo import CountryInfo
country = CountryInfo("Bulgaria")

# How many name this country is known for.
print(country.alt_spellings())

# Capital of the country.
print(country.capital())

# Currency used in the country.
print(country.currencies())

# Languages used in the country.
print(country.languages())

# Countries that share the country border.
print(country.borders())

# See all information about the country.
data = country.info()
for i, j in data.items():
    print(f"{i}:>>{j}")