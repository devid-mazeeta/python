str1 = 'GeeksforGeeks'

# lambda returns a function object
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))

#############################

format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))
