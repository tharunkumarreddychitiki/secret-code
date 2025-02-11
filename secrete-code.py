import string
import random
def encoding(message) :
	for i in words :
		if len(i) >= 3 :
			front = ''.join(random.choices(string.ascii_letters,k=3))
			back = ''.join(random.choices(string.ascii_letters,k=3))
			new_word = front + i[1:] + i[0] + back
			coded_msg.append(new_word)
		else :
			coded_msg.append(i[::-1])
	print(" ".join(coded_msg))

def decoding(message) :
	for i in words :
		if len(i) >= 3 :
			a = i[3:-3]
			new_word = a[-1] + a[:-1]
			coded_msg.append(new_word)
		else :
			coded_msg.append(i[::-1])
	print(" ".join(coded_msg))


choice = int(input("1. Encoding\n2. Decoding\nEnter your choice : "))
if choice in [1,2] :
	message = input("Enter the message : ")
	words = message.split(" ")
	coded_msg = []
	if choice == 1 :
		encoding(message)
	elif choice == 2 :
		decoding(message)