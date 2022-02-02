import requests as req
import json
import webbrowser

pref_file = 'prefences.json'

with open(pref_file, 'r') as prefFile:
	pref_data = prefFile.read()  # Read the Prefences file
	pref_json = json.loads(pref_data)  # Load it as Json

UPDATE_CHECK_LINK = req.get(pref_json["UpdateManager"]["redirect"])
resp = UPDATE_CHECK_LINK.json()

currentver = pref_json["CurrentVersion"]  # Get Current Version
newestver = resp["newestVersion"]

def check():
	if currentver == newestver:  # If curver and newver are the same
		print('No Update available!')
	elif currentver <= newestver:  # If curver is older than newver
		print('Update available! Download it from the official repository on github!')
		input('Press Enter, to redirect to the page') ; webbrowser.open('https://github.com/stngo/pwbinaryc/releases')  # Go to my releases
	elif currentver >= newestver:  # If newver is older(?) than curver
		print('You have a newer version as possible??? Are you a dev?')
		input('wow... enter enter...\n\n') ; exit()

if __name__ == "__main__":  # If its started (not imported!)
	print(f'Connection to API from %s (made by {pref_json["UpdateManager"]["madeHost"]}):\n' % pref_json["UpdateManager"]["host"])
	print('Name: %s' % resp["name"])
	print('\nVersion: %s' % newestver)
	print('Current Version: %s\n' % currentver)

	# Checking, if a update is available
	if currentver == newestver:  # If curver and newver are the same
		print('No Update available!')
		input('Press Enter, to exit') ; exit()
	elif currentver <= newestver:  # If curver is older than newver
		print('Update available! Download it from the official repository on github!')
		input('Press Enter, to redirect to the page') ; webbrowser.open('https://github.com/stngo/pwbinaryc/releases')  # Go to my releases
	elif currentver >= newestver:  # If newver is older(?) than curver
		print('You have a newer version as possible??? Are you a dev?')
		input('wow...') ; exit()