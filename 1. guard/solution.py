
def answer(x):
	return x

def test(fn,input,output):
	if (fn(input) == output):
		print 'You passed!'
	else:
		print 'Keep trying'

def main():
	test(answer,7,4)
	# answer(7)

if __name__ == '__main__':
	main()