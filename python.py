"""
I am using python file
"""
print(" ........................ program 1.......................")
list1 = [('third', 9, 5), ('first', 4, 6), ('second', 8, 12)]
list1.sort(key=lambda a: a[0])
print(list1)

print("......................... program 2 .......................")
list2 = [1, 1, 1, 3, 3, 4, 5, 7]
list3 = []
for i in list2:
    if i not in list3:
        list3.append(i)
if len(list3) == len(set(list2)):
    print("No Duplicate")
else:
    print("There duplicate is  available")

print("...................... program 3 ...........................")
string1 = 'I love python programming'
string2 = string1.split()


def reverse_string(Str):
    new_string = []
    for char in Str[::-1]:
        new_string.append(char)
    output = " ".join(new_string)
    return output


print(reverse_string(string2))

print("............................. program 4 ..........................")


def deco(func):
    print('print before main function')
    func()
    print('print after main function ')


@deco
def main():
    print('main function')


print("..................... program 5.................")


def add(a):
    return a + a


out = list(map(add, (1, 2, 3)))
# map function return map object
print(out)

print("................... i am using new branch ............................")