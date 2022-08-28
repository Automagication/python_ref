"""
CSV
"""
# An example of csv.DictWriter
import csv

with open('companies.csv', 'w') as csvfile:
  fieldnames = ['name', 'type']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({'name': 'Codecademy', 'type': 'Learning'})
  writer.writerow({'name': 'Google', 'type': 'Search'})

"""
After running the above code, companies.csv will contain the following information:

name,type
Codecademy,Learning
Google,Search
"""