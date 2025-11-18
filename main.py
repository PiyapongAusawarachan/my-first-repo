# # import csv, os
# # from pathlib import Path

# # class DataLoader:
# #     """Handles loading CSV data files."""
    
# #     def __init__(self, base_path=None):
# #         """Initialize the DataLoader with a base path for data files.
# #         """
# #         if base_path is None:
# #             self.base_path = Path(__file__).parent.resolve()
# #         else:
# #             self.base_path = Path(base_path)
    
# #     def load_csv(self, filename):
# #         """Load a CSV file and return its contents as a list of dictionaries.
# #         """
# #         filepath = self.base_path / filename
# #         data = []
        
# #         with filepath.open() as f:
# #             rows = csv.DictReader(f)
# #             for row in rows:
# #                 data.append(dict(row))
        
# #         return data
    
# # class Table:
# #     def __init__(self, name, dict_list):
# #         self.name = name
# #         self.dict_list = dict_list  

# #     def filter(self, condition_func):
# #         filtered_data = [row for row in self.dict_list if condition_func(row)]
# #         return Table(self.name, filtered_data)

# #     def aggregate(self, agg_func, column_name):
# #         vals = [row[column_name] for row in self.dict_list if column_name in row]
# #         return agg_func(vals)

# #     def _numeric_series(self, column_name):
# #         nums = []
# #         for item in self.dict_list:
# #             if column_name in item and item[column_name] not in (None, ""):
# #                 try:
# #                     nums.append(float(item[column_name]))
# #                 except (ValueError, TypeError):
# #                     pass
# #         if not nums:
# #             raise ValueError(f"No numeric data found in column '{column_name}'")
# #         return nums

# #     def mean(self, column_name):
# #         xs = self._numeric_series(column_name)
# #         return sum(xs) / len(xs)

# #     def max_num(self, column_name):
# #         xs = self._numeric_series(column_name)
# #         return max(xs)

# #     def unique_count(self, column_name):
# #         return len({row[column_name] for row in self.dict_list if column_name in row})


# # loader = DataLoader()
# # cities = loader.load_csv('Cities.csv')
# # my_table1 = Table('cities', cities)

# # my_value = my_table1.mean('temperature')
# # print(my_value)
# # print()

# # my_cities = my_table1.filter(lambda x: x['country'] == 'Germany')
# # cities_list = [[city['city'], city['country']] for city in my_cities.dict_list]
# # print("All the cities in Germany:")
# # for city in cities_list:
# #     print(city)
# # print()

# # my_cities = my_table1.filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12.0)
# # cities_list = [[city['city'], city['country'], city['temperature']] for city in my_cities.dict_list]
# # print("All the cities in Spain with temperature above 12°C:")
# # for city in cities_list:
# #     print(city)
# # print()

# # my_countries = my_table1.unique_count('country')
# # print("The number of unique countries is:")
# # print(my_countries)
# # print()

# # my_value = my_table1.filter(lambda x: x['country'] == 'Germany').mean('temperature')
# # print("The average temperature of all the cities in Germany:")
# # print(my_value)
# # print()

# # my_value = my_table1.filter(lambda x: x['country'] == 'Italy').max_num('temperature')
# # print("The max temperature of all the cities in Italy:")
# # print(my_value)
# # print()


# import csv, os
# from pathlib import Path

# class DataLoader:
#     """Handles loading CSV data files."""
    
#     def __init__(self, base_path=None):
#         """Initialize the DataLoader with a base path for data files.
#         """
#         if base_path is None:
#             self.base_path = Path(__file__).parent.resolve()
#         else:
#             self.base_path = Path(base_path)
    
#     def load_csv(self, filename):
#         """Load a CSV file and return its contents as a list of dictionaries.
#         """
#         filepath = self.base_path / filename
#         data = []
        
#         with filepath.open() as f:
#             rows = csv.DictReader(f)
#             for row in rows:
#                 data.append(dict(row))
        
#         return data

# class DB:
#     """Your code here"""
    
# class Table:
#     """Your code here"""

#     def __str__(self):
#         return self.table_name + ':' + str(self.table)

# loader = DataLoader()
# cities = loader.load_csv('Cities.csv')
# table1 = Table('cities', cities)
# countries = loader.load_csv('Countries.csv')
# table2 = Table('countries', countries)

# my_DB = DB()
# my_DB.insert(table1)
# my_DB.insert(table2)

# my_table1 = my_DB.search('cities')
# print("List all cities in Italy:") 
# my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
# print(my_table1_filtered)
# print()

# print("Average temperature for all cities in Italy:")
# print(my_table1_filtered.aggregate(lambda x: sum(x)/len(x), 'temperature'))
# print()

# my_table2 = my_DB.search('countries')
# print("List all non-EU countries:") 
# my_table2_filtered = my_table2.filter(lambda x: x['EU'] == 'no')
# print(my_table2_filtered)
# print()

# print("Number of countries that have coastline:")
# print(my_table2.filter(lambda x: x['coastline'] == 'yes').aggregate(lambda x: len(x), 'coastline'))
# print()

# my_table3 = my_table1.join(my_table2, 'country')
# print("First 5 entries of the joined table (cities and countries):")
# for item in my_table3.table[:5]:
#     print(item)
# print()

# print("Cities whose temperatures are below 5.0 in non-EU countries:")
# my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
# print(my_table3_filtered.table)
# print()

# print("The min and max temperatures for cities in EU countries that do not have coastlines")
# my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
# print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), 'temperature'))
# print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), 'temperature'))
# print()

import csv, os
from pathlib import Path

class DataLoader:
    """Handles loading CSV data files."""
    
    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files.
        """
        self.base_path = Path(base_path) if base_path else Path(__file__).parent.resolve()
    
    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries.
        """
        filepath = self.base_path / filename
        with filepath.open() as f:
            return [dict(row) for row in csv.DictReader(f)]


class DB:
    def __init__(self):
        self.tables = {}

    def insert(self, table):
        self.tables[table.name] = table

    def search(self, name):
        return self.tables.get(name, None)


class Table:
    def __init__(self, table_name, table):
        self.name = table_name
        self.rows = table

    def __str__(self):
        return f"{self.name}:" + str(self.rows)

    def filter(self, func):
        filtered = [row for row in self.rows if func(row)]
        return Table(self.name + "_filtered", filtered)

    def aggregate(self, func, column):
        values = [row[column] for row in self.rows]

        # Try convert to numeric
        try:
            nums = list(map(float, values))
            return func(nums)
        except ValueError:
            return func(values)

    def join(self, other_table, key):
        lookup = {}
        for o in other_table.rows:
            lookup.setdefault(o[key], []).append(o)

        joined = []
        for r in self.rows:
            val = r.get(key)
            if val in lookup:
                for o in lookup[val]:
                    joined.append({**r, **o})

        return Table(self.name + "_joined_" + other_table.name, joined)


# -------------------------------
# ด้านล่างคือโค้ดทดสอบเหมือนเดิม
# -------------------------------

loader = DataLoader() 
cities = loader.load_csv('Cities.csv')
table1 = Table('cities', cities)
countries = loader.load_csv('Countries.csv')
table2 = Table('countries', countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

my_table1 = my_DB.search('cities')
print("List all cities in Italy:") 
my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
print(my_table1_filtered)
print()

print("Average temperature for all cities in Italy:")
print(my_table1_filtered.aggregate(lambda x: sum(x)/len(x), 'temperature'))
print()

my_table2 = my_DB.search('countries')
print("List all non-EU countries:") 
my_table2_filtered = my_table2.filter(lambda x: x['EU'] == 'no')
print(my_table2_filtered)
print()

print("Number of countries that have coastline:")
print(my_table2.filter(lambda x: x['coastline'] == 'yes').aggregate(lambda x: len(x), 'coastline'))
print()

my_table3 = my_table1.join(my_table2, 'country')
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.rows[:5]:
    print(item)
print()

print("Cities whose temperatures are below 5.0 in non-EU countries:")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
print(my_table3_filtered.rows)
print()

print("The min and max temperatures for cities in EU countries that do not have coastlines")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), 'temperature'))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), 'temperature'))
print()
