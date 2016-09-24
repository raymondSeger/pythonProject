print( 'spam eggs' ) # single quotes
print( 'doesn\'t' )

print('C:\some\name')  # here \n means newline!

print(r'C:\some\name')  # note the r before the quote

#string literal keeps the empty spaces and tab
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#strings can be used with + and x
# only works with two literals though. DOES NOT WORK on strings stored in variables
print( 3 * 'un' + 'ium' )

# you can combine strings without using +
print( 'Put several strings within parentheses '
'to have them joined together.' )
print('a' 'b')

word = 'Python'
print(word[0])
print(word[5])
print( word[0:2] )
print( word[:] )