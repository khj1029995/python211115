# DemoError.py

def divide(a,b) :
    return a/b

try :
    result = divide(5,2)
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError :
    print("숫자여야 합니다.")
else :
    print("result: {0}".format(result))
finally: 
    print("한번 더 체크")

print("end")