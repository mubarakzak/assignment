#!/usr/bin/python
import getpass
import string
import os

# creatinga lists of users, their PINs and bank statements
users = ['user', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0
# while loop checks existance of the enterd username
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		else:
			n = 2
		break
	else:
		print('----------------')
		print('****************')
		print('INVALID USERNAME')
		print('****************')
		print('----------------')

# comparing pin
while count < 3:
	print('------------------')
	print('******************')
	pin = str(input('PLEASE ENTER PIN: '))
	print('******************')
	print('------------------')
	if pin.isdigit():
		if user == 'user1':
			if pin == pins[0]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()

		if user == 'user2':
			if pin == pins[1]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
				
		if user == 'user3':
			if pin == pins[2]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
	else:
		print('------------------------')
		print('************************')
		print('PIN CONSISTS OF 4 DIGITS')
		print('************************')
		print('------------------------')
		count += 1
	

print('-------------------------')
print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')	
print(str.capitalize(users[n]), 'welcome to ZAKS ATM')
print('**************************')
print('----------ATM SYSTEM-----------')
# Main menu
while True:
	#os.system('clear')
	print('-------------------------------')
	print('*******************************')
	response = input('SELECT FROM FOLLOWING OPTIONS: \nbalance__(S) \nWithdraw___(W) \ndeposit__(L)   \nQuit_______(Q) \n: ').lower()
	print('*******************************')
	print('-------------------------------')
	valid_responses = ['s', 'w', 'l', 'q']
	response = response.lower()
	if response == 's':
		print('---------------------------------------------')
		print('*********************************************')
		print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'cedis ON YOUR ACCOUNT.')
		print('*********************************************')
		print('---------------------------------------------')
		
	elif response == 'w':
		print('---------------------------------------------')
		print('*********************************************')
		cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
		print('*********************************************')
		print('---------------------------------------------')
		if cash_out%10 != 0:
			print('------------------------------------------------------')
			print('******************************************************')
			print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 cedis NOTES')
			print('******************************************************')
			print('------------------------------------------------------')
		elif cash_out > amounts[n]:
			print('-----------------------------')
			print('*****************************')
			print('YOU HAVE INSUFFICIENT BALANCE')
			print('*****************************')
			print('-----------------------------')
		else:
			amounts[n] = amounts[n] - cash_out
			print('-----------------------------------')
			print('***********************************')
			print('YOUR NEW BALANCE IS: ', amounts[n], 'cedis')
			print('***********************************')
			print('-----------------------------------')
			
	elif response == 'l':
		print()
		print('---------------------------------------------')
		print('*********************************************')
		cash_in = int(input('ENTER AMOUNT YOU WANT TO deposit: '))
		print('*********************************************')
		print('---------------------------------------------')
		print()
		if cash_in%10 != 0:
			print('----------------------------------------------------')
			print('****************************************************')
			print('AMOUNT YOU WANT TO deposit MUST TO MATCH 10 cedis NOTES')
			print('****************************************************')
			print('----------------------------------------------------')
		else:
			amounts[n] = amounts[n] + cash_in
			print('----------------------------------------')
			print('****************************************')
			print('YOUR NEW BALANCE IS: ', amounts[n], 'cedis')
			print('****************************************')
			print('----------------------------------------')
	
		
	elif response == 'q':
		exit()
	else:
		print('------------------')
		print('******************')
		print('RESPONSE NOT VALID')
		print('******************')
		print('------------------')