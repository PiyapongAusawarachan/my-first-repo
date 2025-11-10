import csv, os
from pathlib import Path

class DataLoader:
    """Handles loading CSV data files."""
    
    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files.
        """
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)
    
    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries.
        """
        filepath = self.base_path / filename
        data = []
        
        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))
        
        return data
    
class Table:
    def __init__(self, name, dict_list):
        self.name = name
        self.dict_list = dict_list  

    def filter(self, condition_func):
        filtered_data = [row for row in self.dict_list if condition_func(row)]
        return Table(self.name, filtered_data)

    def aggregate(self, agg_func, column_name):
        vals = [row[column_name] for row in self.dict_list if column_name in row]
        return agg_func(vals)

    def _numeric_series(self, column_name):
        nums = []
        for item in self.dict_list:
            if column_name in item and item[column_name] not in (None, ""):
                try:
                    nums.append(float(item[column_name]))
                except (ValueError, TypeError):
                    pass
        if not nums:
            raise ValueError(f"No numeric data found in column '{column_name}'")
        return nums

    def mean(self, column_name):
        xs = self._numeric_series(column_name)
        return sum(xs) / len(xs)

    def max_num(self, column_name):
        xs = self._numeric_series(column_name)
        return max(xs)

    def unique_count(self, column_name):
        return len({row[column_name] for row in self.dict_list if column_name in row})


loader = DataLoader()
cities = loader.load_csv('Cities.csv')
my_table1 = Table('cities', cities)

my_value = my_table1.mean('temperature')
print(my_value)
print()

my_cities = my_table1.filter(lambda x: x['country'] == 'Germany')
cities_list = [[city['city'], city['country']] for city in my_cities.dict_list]
print("All the cities in Germany:")
for city in cities_list:
    print(city)
print()

my_cities = my_table1.filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12.0)
cities_list = [[city['city'], city['country'], city['temperature']] for city in my_cities.dict_list]
print("All the cities in Spain with temperature above 12°C:")
for city in cities_list:
    print(city)
print()

my_countries = my_table1.unique_count('country')
print("The number of unique countries is:")
print(my_countries)
print()

my_value = my_table1.filter(lambda x: x['country'] == 'Germany').mean('temperature')
print("The average temperature of all the cities in Germany:")
print(my_value)
print()

my_value = my_table1.filter(lambda x: x['country'] == 'Italy').max_num('temperature')
print("The max temperature of all the cities in Italy:")
print(my_value)
print()
