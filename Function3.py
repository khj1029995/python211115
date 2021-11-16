# Function3.py

x = 1
def func(a) :
    return a+x

# 호출
print(func(1))

def func2(a):
    x=2
    return a+x

#호출
print(func2(1))

#기본값 세팅
def times(a=10, b=20):
    return a*b

# 호출
print(times())
print(times(3))
print(times(3,4))

# 키워드 인자
def connectURI(server, port) :
    strURL = "http://" + server + ":" + port
    return strURL

# 호출
print(connectURI("naver.com", "80"))
print(connectURI(port="80", server="naver.com"))

# 가변인자
def union(*ar) :
    result = []
    for item in ar :
        for x in item :
            if x not in result :
                result.append(x)
    return result

# 호출
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))

