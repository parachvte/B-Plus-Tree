import random


def gen():
	num = 100
	ch_list = [chr(i) for i in range(ord('a'), ord('z') + 1)] 
	length = 10
	with open("data/small-data.txt", "w") as F:
		for i in range(num):
			key = random.randint(0, 1000)
			F.write(str(key))
			F.write(" " + "".join([random.choice(ch_list) for i in range(length)]) + "\n")

def test():
	d = {}
	with open("data/ex-data.txt", "r") as F:
		cnt = 0
		valid = 0
		while True:
			line = F.readline()
			if line.strip() == "":
				break
			key_s, value = line.split()
			key = int(key_s)
			cnt += 1
			if d.get(key) is None:
				d[key] = 1
				valid += 1
			if cnt % 10000 == 0:
				print "cnt = ", cnt
		print "cnt =", cnt
		print "valid = ", valid

#gen()
