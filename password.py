password_c = 'a123456'
time = 3
while True:	
	password_t = input('Enter your password: ')
	if password_t == password_c:
		print('Successfully log in !!!')
		break
	else:
		time = time - 1
		print('Please try again,and you have',time,'times.')
		if time == 0:
			print('Goodbye !!!')
			break