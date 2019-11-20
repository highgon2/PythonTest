while 1:
	data = input()
	if not data:
		# print("data[%d] = [%s]"%(len(data),data))
		print("data[{:02X}] = [{}]".format(len(data), data))
		break

	print("data[0x{:02X}] = {}".format(len(data), data))