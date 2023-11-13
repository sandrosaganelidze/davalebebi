from random import randint

def list_generator(length):
    generated_list=[]
    for _ in range(0,length):
        generated_list.append(randint(1,11))
    return generated_list
my_list = list_generator(15)

def merge_sort(arr):
    length = len(arr)
    if len(arr) <= 1:
        return arr
    else:
    # ეს მაასივი გავყოთ ორად
        mid_point = len(arr)//2
        sub_arr1 = arr[:mid_point]
        sub_arr2 = arr[mid_point:]
    # იგივე დალაგების ფუნქციას ვიყენებთ ორივე ქვედონეზე
        merge_sort(sub_arr1)
        merge_sort(sub_arr2)
    # 
        i = k = j = 0
    # სანამ დასაწყისს ან ბოლოს არ მივაღწევთ ვირჩევთ უფრო დიდ რიცხვს
    # ელემენტებს ვსვამთ სწორ ადგილას დალაგებულ მასივში
        while i < len(sub_arr1) and j < len(sub_arr2):
            if sub_arr1[i] < sub_arr2[j]:
                arr[k] = sub_arr1[i]
                i += 1
            else:
                arr[k] = sub_arr2[j]
                j += 1
            k += 1
    # როცა ყველა ელემენტი დალაგებულია ან arr1–ში ან arr2–ში, ვიღებთ ელემენტებს და ჩავსვსამთ დალაგებულ მასივში
        while i < len(sub_arr1):
            arr[k] = sub_arr1[i]
            i += 1
            k += 1
        while j < len(sub_arr2):
            arr[k] = sub_arr2[j]
            j += 1
            k += 1
merge_sort(my_list)
print(my_list)