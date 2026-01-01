#creating an virtual atm
accounts = {'62433570421' : {'name':'Alex','balance': 1000,'pin':1234},
            '62433570422' : {'name':'Bob','balance': 10000,'pin':9999},
            '62433570423' : {'name':'Charles','balance': 5000,'pin':1357},
            '62433570424' : {'name':'David','balance': 2000,'pin':3535}
            }
acc_no = input('Enter your account no:')
if acc_no in accounts:
    crct_pin = accounts[acc_no]['pin']
    nxt_attempt = True
    a = 1
    session = False
    while a<4 and nxt_attempt:
         pin = int(input('Enter the pin:'))
         remaining = 3-a
         a+= 1
         if pin == crct_pin:
             print('proceed')
             session = True
             nxt_attempt = False
         else:
             if remaining ==0:
                 print('Account locked.Please visit after 24 hrs')
             else:
                 print(f'{remaining} attempts left.please try again later')
    transaction_history = []
    while session:
        print('please choose your option')
        print('1.Deposit')
        print('2.Withdraw')
        print('3.Balance Enquiry')
        print('4.Mini Statement')
        print('5.Pin Change')
        print('6.Exit')
        ch =int(input('Please enter your choice:'))
        if ch == 1:
            amount = int(input('Please enter the amount to deposit:'))
            accounts[acc_no]['balance'] += amount
            transaction_history.append(f'{amount} Deposited successfully')
            print(f'{amount} deposited successfully')
        elif ch == 2:
            amount = int(input('Please enter the amount for withdraw:'))
            if amount <= accounts[acc_no]['balance']:
                accounts[acc_no]['balance'] -= amount
                transaction_history.append(f'{amount} withdrawen successfully')
                print(f'{amount} withdrawen successfully')
                print(f"current bal: {accounts[acc_no]['balance']}")
            else:
                print('Insufficient funds')
                print(f"current bal: {accounts[acc_no]['balance']}")
        elif ch == 3:
            print(f"current bal: {accounts[acc_no]['balance']}")
        elif ch == 4:
            n = len(transaction_history)
            i = n-1
            count = 0
            while i >= 0 and count < 3:
                print(transaction_history[i])
                i -= 1
                count += 1
        elif ch == 5:
            cur_pin = int(input('Please enter your current pin:'))
            if cur_pin == accounts[acc_no]['pin']:
                new_pin = int(input('Please enter new pin:'))
                confirm_pin = int(input('please confirm your new pin:'))
                if new_pin == confirm_pin:
                    accounts[acc_no]['pin'] = new_pin
                    print('Pin updated successfully')
                else:
                    print('Confirmation failed')
            else:
                print('Invalid pin')
        elif ch == 6:
            print('Thank you. Visit Again....')
            break
        else:
            print('Invalid choice')
else:
    print('Invalid account number')

































