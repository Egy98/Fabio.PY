my_list = []

# Richiedi 5 numeri all'utente
for i in range(5):
    num = int(input(f'Dammi il numero {i + 1}: '))
    my_list.append(num)

# Calcolo somma e media
total = sum(my_list)
avg = total / len(my_list)

# Output
print(f'Questa è la lista: {my_list}, questa è la somma: {total}, e questa è la media {avg}')
