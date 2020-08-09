
def main():
	rec(10)


def rec(num):

	if int(num) > 0:
		rec(num - 1)
		print(num)
		
		


main()