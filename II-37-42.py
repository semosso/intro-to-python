# testing how to manipulate strings by slicing them into substrings
# [start:end:step]
letters = 'abcdefghijklmnopqrstuvwxyz'

print(letters[:]) # will print all

print(letters[-1::-1]) # will print backwards (i.e., starting at -1, go with -1 step)
print(letters[::-1]) # same as above

print(letters[-51:-50]) # ln 9 and ln 10 are the same, because an offset earlier than the beggining is treated as -1
print(letters[-1:-1]) 
print(letters[-40:2]) # for the same reason as ln 10, ln 12 and 13 are the same
print(letters[:2])

# now splitting with SPLICE and combining with JOIN
todos = 'go to play, go to movies, buy tickets, pick-up laundry'

todos.split(', ') # breaks string into smaller ones based on the separator you specify (i.e., comma + space ', ')
# if no separator specified, it defaults to white space characters

print(todos.split(', ')[2]) # this prints the position you call for, cool; how to print all split into new lines? maybe ln 29

# now how about joining them with combine (i.e., collapsing a list of strings into a single one)
crypto_list = ['Yetti', 'Bigfoot', 'Loch Ness Monster'] # this is a list, one of pythons smallest data structures
crypto_string = ', '.join(crypto_list)
# as above, you have to first specify the string that glues every other (', ') and then the list of loose strings as parameters to join()
print('This is the combined list:', crypto_string)

# tentando dar print na lista de ln 16, mas em diferentes linhas
todos = 'go to play, go to movies, buy tickets, pick-up laundry'
quebrada = todos.split(', ') # alternatively, add split at the end of todos, and change variables below
nova_linha = '\n'.join(quebrada)
print(nova_linha) # IT WORKED!