#         N1 
# inf = input("string: ")
# letter = 0
# number = 0
# symbol = 0
# for i in inf:
#     if i.isalpha():
#         letter+=1
#     elif i.isdigit():
#         number+=1
#     elif i==' ':
#         symbol=symbol
#     else:
#         symbol+=1
# print(f"digits: {number}, letters: {letter}, symbols: {symbol}")

#              N2
# sent1 = input('first sentence: ')
# sent2 = input('second sentence: ')
# new = ''
# ind1 = 0
# ind2 = -1
# a = 0
# while len(new)<=len(sent1)+len(sent2)-1:
#     if a%2==0:
#         if ind1<len(sent1):
#             new+=sent1[ind1]
#             ind1+=1
#         else:
#             break
#     else:
#         if abs(ind2)<=len(sent2):
#             new+=sent2[ind2]
#             ind2=ind2-1
#     a+=1
# print(new)

#               N3
# sent1 = input('first sentence: ')
# sent2 = input('second sentence: ')
# i=0
# while i<len(sent1):
#     if sent1[i] != sent2[i]:
#         print('Strings are not balanced!')
#         break
#     i+=1
# else:
#     print('Strings are balanced!')