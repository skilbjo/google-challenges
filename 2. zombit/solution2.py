def answer(intervals):
	time = []
	for interval in intervals:
		hours = []
		hours.extend(range(interval[0],interval[1]+1))
		for hour in hours:
			if hour not in time:
				time.append(hour)
	time.sort()
	return time[len(time)-1] - time[0]