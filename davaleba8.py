#              N1
# lst = [1, 2, 3, 4, 5]
# mult = 2
# result = list(map(lambda x: x * mult, lst))
# print(result)

#               N2
# lst = ['Apple', 'dog', 'Blue', 'happy', 'Red']
# reslt = list(filter(lambda x: x[0].isupper(), lst))
# print(len(reslt))

#               N3
# lst = [1,4,-6,-2,-8,4,6]
# num_pos = list(filter(lambda x: x>0, lst))
# num_neg = list(filter(lambda x: x<0, lst ))
# pos_sum = sum(num_pos)
# neg_sum = sum(num_neg)
# print('sum of positives: ',pos_sum)
# print('sum of negatives: ',neg_sum)

#               N4
# customers = []
# def sign_up():
#     while True:
#         customer_info = []
#         name = input('Enter your name: ')
#         password = input('Enter your password: ')
        
#         if name != '' and len(password) >= 8:
#             print('Account registered')
#             customer_info.append(name)
#             customer_info.append(password)
#             print(f'name: {name}\nPassword: {password}')
#             break 
#         elif name != '':
#             print('Password must be at least 8 characters long')
#         elif len(password) >= 8:
#             print("Name can't be empty")
#         else:
#             print("Name can't be empty, and password must be at least 8 characters long")
# sign_up()

# def balance():
#     bal = 0
#     print(f'Balance: {bal}')
#     add_mon = input('how much money to deposit: ')
#     bal+= int(add_mon)
#     print(f'Balance: {bal}$')
# balance()
# lg = input('Do you want to log in your account? (y/n): ')

# if lg.lower()=='y' or lg.lower()=='yes':
#     def log_in():
#         global customers
#         while True:
#             name_log = input('enter name: ')
#             password_log = input('enter password: ')
#             try:
#                 customer = next(cust for cust in customers if cust[0] == name_log)
#                 if customer[1] == password_log:
#                     print('Login successful')
#                     break
#                 else:
#                     print('Incorrect password')
#             except StopIteration:
#                 print('Customer not found')
#     log_in()
