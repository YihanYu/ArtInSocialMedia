import urllib2


url='https://drawcrowd.com/users/suntea30259'


headers = {'User-agent': 'Yihan'}
request = urllib2.Request(url, headers=headers)
html = urllib2.urlopen(request).read()
print html

