import random
def find_number():
    random_numbers = []
    for i in range(1, 101):
        random_numbers.append(i)
    random.shuffle(random_numbers)
    random_numbers.remove(93)
    print len(random_numbers)
if __name__ == "__main__":
    find_number()