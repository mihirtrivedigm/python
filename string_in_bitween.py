'''
mystring = "do you know what I mean (really not) that day Part-23.mp3"
start = mystring.find( '(' )
end = mystring.find( ')' )
if start != -1 and end != -1:
    result1 = mystring[start + 1:end]
    result2 = mystring[start:end+1]
print result1
print result2

print mystring
print mystring.replace(result2,"")
'''

def change_name(filename):
    start = filename.find('P')
    end = filename.find('.')
    if start != -1 and end != -1:
        result1 = filename[start + 1:end]
        result2 = filename[start:end + 1]
        result3 = filename[start:end]
    #print result1
    #print result2
    #print result3

    #print filename
    #print filename.replace(result2, "")
    result4 = result3 + " " + filename
    #print result4
    return result4


name1 = "I mean (really not) that day Part-23.mp3"
name2 = change_name(name1)
print name1
print name2


'''
filename = "do you know what I mean (really not) that day Part-23.mp3"
start = filename.find( 'P' )
end = filename.find( '.' )
if start != -1 and end != -1:
    result1 = filename[start + 1:end]
    result2 = filename[start:end+1]
    result3 = filename[start:end]
print result1
print result2
print result3

print filename
print filename.replace(result2,"")
result4 = result3 + " " + filename
print result4
'''