result = urllib.request.urlopen(url)
response=urllib.request.urlopen("http://www.fishc.com")
html=response.read()
print(html)
