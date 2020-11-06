owners = ['Eric', 'Jack', 'Jamie', 'Lauren']

car_data_dictionary = {
    'make': 'Tesla',
    'model': '3',
    'year': 2019,
    'owners': owners
}

# 3 methods for getting the object back in different ways
# .values(), .keys(), .items()

print("Printing .values()")
for i in car_data_dictionary.values():
    print(i)

print("\nAnd now .keys()")
for i in car_data_dictionary.keys():
    print(i)

print("\nAnd now .items")
for i in car_data_dictionary.items():
    print(i)

print("\nAnd iterating with no method call")
for i in car_data_dictionary:
    print(i)

if 'make' in car_data_dictionary:
    print('\nMake included in data')

if 'mileage' in car_data_dictionary:
    print('\nMileage included in data')

if 'Tesla' in car_data_dictionary.values():
    print('\nMake is:')
    print(car_data_dictionary['make'])

print('\nOwners are:')
print(car_data_dictionary.get('owners'))

car_data_dictionary['itself'] = car_data_dictionary

print(car_data_dictionary)
print(car_data_dictionary['itself'])
print(car_data_dictionary['itself']['itself'])
print(car_data_dictionary['itself']['itself']['itself'])
