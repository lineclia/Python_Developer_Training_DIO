'''
Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja  modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão desse sistema devemos implementar apenas 3 operações: depósito, saque e extrato. 

Operação de DEPÓSITO:
	Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, portanto não precisamos nos preocupar com a identificação e número da agência bancária e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato. 

Operação de SAQUE:
	O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato. 

Operação de EXTRATO:
	Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. 
	Os valores devem ser exibidos utilizando o formato R$ XXX.XX, p.e.:
1500.45 = R$1500.45

'''



menu = '''  

[d] Deposit
[s] Withdraw
[e] Extract
[q] Exit

=> '''

balance = 0
limit = 500
transactions = []
number_of_withdraws = 0
WITHDRAW_LIMIT  = 3

while True:
	option = input(menu)

	if  option == 'd':
		print('Deposit')
		value = float(input("Value of deposit: "))
		if value <= 0:
			print ("Invalid value. Value must be positive.")
		else:
			balance += value 
			transactions.append(value)
			print (f"-------- Success deposit ! Balance: {balance:.2f} --------")

	elif option == 's':
		print('Withdraw')
		if number_of_withdraws >= WITHDRAW_LIMIT:
			print ("--------You already used your 3 withdraws per day.--------")
			continue
		value = float(input("Value of withdraw: "))
		if  value > balance:
			print(f"-------- Insuficient balance in you account. Balance: {balance}")
		else:
			balance -= value
			number_of_withdraws += 1
			transactions.append(-value)
			print (f"-------- Withdraw successful ! Balance: {balance:.2f}")
		


	elif option == 'e':
		print ('Extract')
		if not transactions: 
			print("No transactions to display yet.")
		else:
			for transaction in transactions:
				print (transaction)
			print(f"Current balance: R${balance:.2f}")
	
	elif option == 'q':
		break

	else: 
		print ('Invalid option, please select the desired operation again.')

	
print("Thank you for using our bank !")
