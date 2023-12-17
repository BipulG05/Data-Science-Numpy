class S:
	# @param A : integer
	# @param B : list of strings
	# @return an integer
	def solve(self, A, b):
	    sum2 = 0
	   # member = 0
	    for group in b:
                sum1 = 0
                member = len(group)
                if len(group) > A: 
                    continue
            # member += len(group)
                print(group)
                for i in range(len(group)):
                    if group[i] == 'c':   sum1 += 4
                    elif group[i] == 'w': sum1 += 3
                    elif group[i] == 'm': sum1 += 2
                    elif group[i] == 'o': sum1 += 1
                sum2 += sum1 * member
	    return sum2

a = S()
print(a.solve(5,['mmo','oo','cmw','cc','c']))