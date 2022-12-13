colors = ['red','green','blue']
print(colors)

new_colors = colors  # copies the list
print(new_colors)

new_colors = colors.sort()  # incorrect format
print(new_colors) # returns none

colors.sort() # correct format
print(colors) # returns sorted list
