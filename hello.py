print("hello")

array = []
array.append("hi")
print(array)
array.append(["hello", "안녕"])
print(array)
array.extend(["bye", "chao"])
print(array)

person = {"name": "Lee", "age": 7}
people = [{"name": "Kim", "age": 38}]

people.append(person)
print(people)

print(people[0]["age"])


def hello(name):
    print(name)
    if (True):
        print("")


def sum(a, b):
    return a + b


def minus(a, b):
    return a - b


def mul(a, b):
    return a * b


print(mul(sum(1, 2), minus(10, 15)))


def even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(even(3))
print(even(2))

print("짝수")


def zeroToN(n):
    accum = 0
    for i in range(n+1):
        accum+=i
    return accum


print(zeroToN(10))

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

def get_age(name):
    for p in people:
        if p["name"] == name:
            return p["age"]
    return -1


print(get_age("bob"))
print("이름 없습니다" if get_age("kim") == -1 else get_age("kim"))


