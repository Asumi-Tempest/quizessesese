def single_array():
    fruits = ['apple','mango','orange','melon']
    listoffruits = []

    for G in fruits:
        listoffruits.append(fruits)
    return listoffruits [:]

def two_array():
    places = [
            ['gingoog','cagayan'],
            ['japan','tokyo'],
            ['gicc','gcc']
        ]
    listofplaces = []

    for T in places:
        listofplaces.append(places)
    return listofplaces [:]

inter = input('which array, single or two: ')

if inter == 'single':
    print(single_array())

elif inter == 'two':
    print(two_array())
else:
    print('error')





