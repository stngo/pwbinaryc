import requests as req
import json
import webbrowser

pref_file = 'prefences.json'

with open(pref_file, 'r') as prefFile:
	pref_data = prefFile.read()
	pref_json = json.loads(pref_data)

UPDATE_CHECK_LINK = req.get(pref_json["UpdateManager"]["redirect"])
resp = UPDATE_CHECK_LINK.json()

if __name__ == "__main__":
	currentver = pref_json["CurrentVerion"])
	newestver = resp["newestVersion"])

	print(f'Connection to API from %s (made by {pref_json["UpdateManager"]["madeHost"]}):\n' % pref_json["UpdateManager"]["host"])
	print('Name: %s' % resp["name"])
	print('\nVersion: %s' % newestver
	print('Current Version: %s' % currentver

	if currentver <= newestver:
		print('Update available! Download it from the official repository on github!')
		input('Press a key, to redirect to the page') ; webbrowser.open('http://example.com')  # Go to example.com