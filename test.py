a = 'spartacodingclub@gmail.com'

"".split("@")

print(a.split("@")[1].split(".")[0])

print(a.find("기"))
print(a.find("@"))


# 채워야하는 함수
def check_mail(s):
    return (s.find("@") > -1) and (s.find(".") > -1)


def get_mail(s):
    return s.split("@")[1].split(".")[0]


# 결과값
print(check_mail(a))
print(get_mail(a))

# 입력값
a = ['사과', '감', '감', '배', '포도', '포도', '딸기', '포도', '감', '수박', '딸기']

s = {}

# 채워야하는 함수
def count_list(a_list):
    r = {}
    for f in a_list:
        if r.get(f) == None:
            r[f] = 1
        else:
            r[f] += 1
    return r


# 결과값
print(count_list(a))

# 아래와 같이 출력됩니다
{'사과': 1, '감': 3, '배': 1, '포도': 3, '딸기': 2, '수박': 1}

# 아래와 같이 출력됩니다
# True
