# 1 შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას, თუმცა უნიკალური ელემენტებით (გამოიყენე set მონაცემთა ტიპი).
# lst1 = [1,1,2,2,3,3]
# def unique_list(li):
#     list_set = set(li)
#     unique_lst = list(list_set)
#     return unique_lst
# print(unique_list(lst1))

#
#
# 2 შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე set ტიპის მონაცემს უნიკალური ელემენტებით, რომლის შეცვლაც შეუძლებელი იქნება (გამოიყენე frozenset).
# def immutable_set(li):
#     frzn_set= frozenset(li)
#     return frozenset
# print(immutable_set(lst1))
#
#
# 3 შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს tuple ტიპის მონაცემად და დააბრუნებს შედეგს.
# st1 = {1,2,3,4,5}
# st2 = {6,7,8,9,10}
# def set_to_tuple(a,b):
#     st_un = a.union(b)
#     tup_un = tuple(st_un)
#     return tup_un
# print(set_to_tuple(st1,st2))


#
# 4 შექმენი ფუნქცია რომელიც მიიღებს მომხმარებლის სახელს და პაროლს, ასევე სიის სახელს. პაროლს გაუკეთებს ჰეშირებას და მონაცემს შეინახავს tuple ტიპის
# მონაცემად გადაცემულ სიაში. შედეგი უნდა დააბრუნოს [("user1", "pass1")]
def user_info():
    user1 = input('name: ')
    pass1 = input('password: ')
    set_name = input('name of list: ')

    return ...


