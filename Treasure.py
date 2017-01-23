try:
    t=int(raw_input())
except ValueError:
    print "Not a number"



for i in range(0,t):
	try:
		matrix=int(raw_input())
	except ValueError:
		print "Not a number"
		
	mat_list = []
	for j in range(0,matrix):
		mat_list.append(raw_input().split()) 
		
	for l in range (0,matrix):
		for m in range (0,matrix):
			print (mat_list[l][m])
			
	#print (mat_list)
			
