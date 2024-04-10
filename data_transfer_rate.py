def convert_data_size(size, from_unit, to_unit):
    units = {
        'b': 1,
        'kb': 1024,
        'mb': 1024 ** 2,
        'gb': 1024 ** 3,
        'tb': 1024 ** 4
    }

    if from_unit.lower() not in units or to_unit.lower() not in units:
        return "Invalid units"

    return size * units[from_unit.lower()] / units[to_unit.lower()]

# Example usage:
size = 100  # Size in megabytes
from_unit = input()
to_unit = input()
converted_size = convert_data_size(size, from_unit, to_unit)
print(f"{size} {from_unit.upper()} is equal to {converted_size:.2f} {to_unit.upper()}")
