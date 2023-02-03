# urllib 패키지 불러오기
from urllib.request import Request, urlopen

req = Request('https://www.naver.com') # http 보안 강화 http's' = security     , request 요청 
res = urlopen(req)                     #                                       , respone 응답, url로 하면 브라우저 아니면 컴퓨터로 통함
print(res.status)
