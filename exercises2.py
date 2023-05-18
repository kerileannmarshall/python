# Keri Marshall
# Exercise set 2 of learning Python

# learning to make a list
books = ['The Giver', 'On The Come Up', 'Throne of Fire', 'Forged By Fire']
print(books)
print()

# pulling data from a list
print('\t' + books[0])

# putting data from list in a message
print('\tMy favorite book is ' + books[0] + '.')
print('\n\t' + books[2].upper())
message = f"\n\tMy favorite book is {books[0].title()}."
print(message)

# changing item in list
books[2] = 'The Hate U Give'
print(books)

# adding an item to a list
books.append('Python Crash Course')
print(books)

# building a list with append
colors = []
colors.append('blue')
colors.append('red')
colors.append('pink')
colors.append('orange')
colors.append('teal')
colors.append('green')
print(colors)

# inserting an item to a list at a certain position
colors.insert(0, 'grey')
print(colors)

# deleting an item from a list at a certain position
del colors[1]
print(colors)

# Popping items from a list
last_color = colors.pop()
print(f"My least favorite color to use in a kitchen remodel is {last_color}.")
print(colors)
bad_color = colors.pop(1)
print(f"But my least favorite home decor color is {bad_color}.")

# using the remove to remove from a list
books.remove('Forged By Fire')
print(books)

# sorting list values
colors.sort()
print(colors)
books.sort()
print(books)

# reversing list sort
colors.sort(reverse=True)
print(colors)

# finding the length of a list
print(len(colors))
print(len(books))
