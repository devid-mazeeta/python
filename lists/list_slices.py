# list slicing
prog_langs = ['java', 'python', 'sql', 'perl']

print(prog_langs[1:-1]) # ['python', 'sql']
prog_langs[0:2] = 'a' # replace ['java', 'python'] with ['a']
print(prog_langs) # ['a','sql', 'perl']
print(prog_langs[0:2]) # ['a','sql']
