def add(x,y):
	return x + y

def solve(sequence):
	sequence = list(str(sequence))

	if len(sequence) == 1:
		return int(sequence[0])
	else: 
		sequence = map(int,sequence)
		sum = reduce(add, sequence)
		return solve(sum)

def answer(x):
	return solve(x)

def test(fn,input,output):
	if (fn(input) == output):
		print 'You passed!'
	else:
		print 'Keep trying'

def main():
	test(answer,1235,2)
	test(answer,13,4)
	# answer(7)

if __name__ == '__main__':
	main()