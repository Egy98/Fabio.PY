animals = ('Elefante', 'Capra', 'Topo', 'Ermellino', 'leone')
animals = list(animals)
animals.append('Lontra')
animals.insert(0, 'Gatto')
animals.remove('Elefante')
animals.sort()
animals = tuple(animals)

print (animals)
