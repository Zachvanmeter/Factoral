def Factoral(i):
	for x in [i-x for x in range(1,i)]:
		i=i*x
	return i

if __name__ == '__main__':
	i = int(input('Please enter a Natural Number (ex 1, 6, 12)\n'))
	f = Factoral(i)
	print('The Factoral of %s equals: %s'%(i,f))
	#>>> The Factoral of 6 equals: 720
