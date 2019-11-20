f = open("./new_file.txt", "w")
for i in range(1, 11):
	data = "%d lines\n" %i
	f.write(data)
f.close()