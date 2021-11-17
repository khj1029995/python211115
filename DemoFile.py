# DemoFile.py

# 파일 쓰기
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째라인\n두번째\n세번째\n")
f.close()

print(f.closed)

# 파일 읽기
f = open("c:\\work\\demo.txt", "rt", encoding="utf-8")

print("---read()---")
print(f.read())

print("---readline()---")
print(f.tell())
# 이때 파일 포인터는 EOF(read() 하고 나서 파일 맨 끝에 포인터 위치)
# EOF 위치가 39바이트라서 39 출력

# 파일 포인터를 맨 위로 리셋
f.seek(0)
# 그리고 한줄씩 읽어옴
print(f.readline())
print(f.readline())

print("---readlines()---")
# 파일 포인터 다시 리셋
f.seek(0)
print(f.readlines())

