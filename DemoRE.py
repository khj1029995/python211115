# DemoRE.py
#정규표현식 모듈
import re

#print(dir(re))

result = re.match("[0-9]*th", "35th")
print(result)
# 검색 결과를 문자열로 리턴(group)
print(result.group())

# match vs search
print(bool(re.match("[0-9]*th", " 35th")))      # 패턴이 정확히 일치해야 True
print(bool(re.search("[0-9]*th", " 35th")))     # 문자열 내에 패턴이 포함되면 True

# 연도 찾기
print(bool(re.search("\d{4}", "올해는 2021년입니다.")))  # 문자열 안에 숫자 4개 있으면 True
result = re.search("\d{4}", "올해는 2021년입니다.")
print(result.group())

