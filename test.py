import requests
response=requests.get("http://baidu.com")
print(response.status_code)
