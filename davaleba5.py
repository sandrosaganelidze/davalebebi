#         N1
# costumers=[]
# i = 0
# while i<=2:
#     costumer_info = []
#     name = input('name: ')
#     lstname = input('lastname: ')
#     age = input('age: ')
#     costumer_info.append(name)
#     costumer_info.append(lstname)
#     costumer_info.append(age)
#     costumers.append(costumer_info)
#     i+=1
# cost = input('enter costumer number: ')
# print()
# print(f'Name: {costumers[int(cost)][0]}\nLastname: {costumers[int(cost)][1]}\nAge: {costumers[int(cost)][2]}')


costumers = []
i=0
while i<1:
    costumer_info=[]
    name = input('enter your name: ')
    pasw = input('enter your passsword: ')
    if name!='' and len(pasw)>=8:
        print('account registered')
        i+=1
        costumer_info.append(name)
        costumer_info.append(pasw)
        costumers.append(costumer_info)
    elif name!='' and len(pasw)<8:
        print('password must be at least 8 characters long')
    elif name=='' and len(pasw)>=8:
        print("name can't be empty")
    else:
        print("name can't be empty and password must be at least 8 characters long")
nam_log = input('name: ')
pas_log = input('password: ')
if nam_log==name and pas_log==pasw:
    print('you have loged in')
else:
    print('name or pasword are incorrect')

#           N3
# actors = [['Ryan','Gosling','42'],['margot','Robbie','33'],['Chris','Hemsworth','40'],['Scarlett','Johansson','38']]
# actr = input('enter name or lastname: ').lower()
# if actr==actors[0][0].lower() or actr==actors[0][1].lower():
#     print(f"Name: {actors[0][0]}\nLastname: {actors[0][1]}\nAge: {actors[0][2]}")
# elif actr==actors[1][0].lower() or actr==actors[1][1].lower():
#     print(f"Name: {actors[1][0]}\nLastname: {actors[1][1]}\nAge: {actors[1][2]}")
# elif actr==actors[2][0].lower() or actr==actors[2][1].lower():
#     print(f"Name: {actors[2][0]}\nLastname: {actors[2][1]}\nAge: {actors[2][2]}")
# elif actr==actors[3][0].lower() or actr==actors[3][0].lower():
#     print(f"Name: {actors[3][0]}\nLastname: {actors[3][1]}\nAge: {actors[3][2]}")
# else:
#     print('No actors were found')