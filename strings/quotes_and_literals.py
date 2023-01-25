# string defining types
print('\n***************************\nString Defining Types\n***************************\n')

single_quote_text = 'Single Quoted Text!!!'
print(single_quote_text)

double_quote_text = "Double Quoted Text!!!"
print(double_quote_text)

s_triple_quote_text = '''Triple Single Quoted Text!!!
Triple Single Quoted Text!!!
Triple Single Quoted Text!!!'''
print(s_triple_quote_text)

d_triple_quote_text = """Triple Double Quoted Text!!!
Triple Double Quoted Text!!!
Triple Double Quoted Text!!!"""
print(d_triple_quote_text)

text_mixed_with_quotes = "6\" inch Fruit's" # Otherwise -> '6" inch Fruit\'s'
print(text_mixed_with_quotes)

# string using literals
print('\n***************************\nLiterals in String\n***************************\n')

single_quote_raw_text = r'Single\n\rQuoted\tText!!!' # prints the raw statement
print(single_quote_raw_text)

double_quote_raw_text = r"Double\n\rQuoted\tText!!!" # prints the raw statement
print(double_quote_raw_text)

double_quote_text = "Double\nQuoted\tText\r!!!" # doesn't prints the raw statement
print(double_quote_text)
