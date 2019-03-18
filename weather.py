import requests

#DarkSky api requires an API key. Please get your own. :)
req = requests.get('https://api.darksky.net/forecast/1ca512d2c3996c9c4b83c2688d094162/40.7608,-111.8910')
result = req.json()

summary = result['currently']['summary']
temperature = result['currently']['temperature']
print(summary," ",temperature,"°F",sep='')

#Can use FontAwesome fonts for pretty icons
#https://fontawesome.com/how-to-use/on-the-web/setup/hosting-font-awesome-yourself
#if summary == 'Clear':
#	print(summary,"  ",temperature,"°F",sep='')
#else:
#	print("whoDat?")
