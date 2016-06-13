
def answer(intervals):
	time_arr = []
	for interval in intervals:
		start = interval[0]
		end = interval[1]
		hours = [hour for hour in range(start,end+1)]

		for hour in hours:
			if hour not in time_arr:
				time_arr.append(hour)

	time_arr.sort()

	return time_arr[len(time_arr) - 1] - time_arr[0]

def test(fn,input,output):
	if (fn(input) == output):
		print 'You passed!'
	else:
		print 'Keep trying'

def main():
	test(answer,[[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]],16)
	test(answer,[[1, 3], [3, 6]],5)

if __name__ == '__main__':
	main()