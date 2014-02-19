def sort_arr_by_using_dict(list):
    order = {}
    counter = 0
    for item in list:
        if len(item) in order.keys():
            key = str(len(item))+'.'+str(counter)
            key = float(key)
            order[key] = item
        else:
            order[len(item)] = item
        counter = counter +1
    for value in sorted(order.keys()):
        print order[value]
#     print list
def brute_force(list):
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if len(list[i]) < len(list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    print list
if __name__ == "__main__":
    arr = ['absnd', 'b', 'a','jhgfjhsd', 'ad', 'kjasdfhkjsdfh']
#     sort_arr_by_using_dict(arr)
    brute_force(arr)
    