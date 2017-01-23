try:
	a,b= raw_input("Enter two numbers here: ").split()
except ValueError:
	print "Not a number"

print "a = ",a
print "b = ",b


number_sets = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
print(number_sets[1])
number_sets[1].append(20)
print(number_sets[1])

number_sets.append([100,200])
print(number_sets[3])

number_sets = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
print(number_sets[0][1])
number_sets[0][1] = 50
print(number_sets[0][1])

number_sets.append(raw_input().split()) 
print(number_sets)