while(1):
	num_list = []
	a, b, c = map(int, input().split())
	if a + b + c == 0:
		break
	num_list.append(a)
	num_list.append(b)
	num_list.append(c)
	num_list.sort()
	if num_list[2] ** 2 == num_list[0] ** 2 + num_list[1] ** 	2:
		print("right")
	else:
		print("wrong")