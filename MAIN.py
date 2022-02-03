import os,time,sys,json
import ctypes as cty
import msvcrt as mcr
import Updater as uda


Black = "\u001b[30m"
Red = "\u001b[31m"
Green = "\u001b[32m"
Yellow = "\u001b[33m"
Blue = "\u001b[34m"
Magenta = "\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"

Reset = "\u001b[0m"


SC_ = "stngo_11.19"

DEF_OUTPUT = 'output.txt'
DEF_WAIT_TIME = 1

pref_file = 'prefences.json'
reTitle = cty.windll.kernel32.SetConsoleTitleW
dn = "\n"

err_msg = [
	f"{Red}Can't load {pref_file} properly! Restart, or reinstall program, to use it!"
]

# Load some Functions, because i need it kekw
def loadMsg(number):
	print(err_msg[int(number)])
	input('Press Enter, to quit!\n') ; print(Reset)
	exit()
def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux
    else:
        os.system('clear')


clear()
# Loading Prefences File
with open(pref_file, 'r') as pref_o: # Open File
	pref_data = pref_o.read() # Read pref and save it as var
	pref_data = json.loads(pref_data) # Loading as json

try:
	titl = pref_data['window']['title']
	reTitle(titl + 'Loading resources...') # Set as window-title
	logo_string=pref_data['window']['logo']
except:
	loadMsg(0)

if pref_data['DebugCode'] == SC_:  # I know, you can copy my debug code and paste it into prefences... i know, its useless xD
	CONFIG_DEBUG = True
else: CONFIG_DEBUG = False

# Convert Logo binary to real text, to use it at the top
logo_string_values = logo_string.split()
main_logo = ""

for binary_value in logo_string_values:
	aint = int(binary_value, 2)

	ascii_char = chr(aint)

	main_logo += ascii_char



i_onetime = True
runMethod = True

while runMethod:
	# Begin selection

	# Check For Updates, One Time
	while i_onetime:
		print(main_logo + dn)
		reTitle(titl + 'Checking for updates...')
		uda.check()
		time.sleep(DEF_WAIT_TIME)
		
		i_onetime = False
	clear()

	print(main_logo + dn)

	reTitle(titl + 'Selecting a Method')
	print(f'{Cyan}Select:'+dn+dn+f'{Green}[1] Text to Binary Code'+dn+'[2] Binary Code to Text'+dn+f'{Red}[3] Exit'+dn+f'{Yellow}[4] Check for Updates{Reset}'+dn)


	select_method = mcr.getch()


	# Selection Methods
	if select_method == b'3':
		runMethod = False
		break
	elif select_method == b'4':
		clear()
		print(main_logo +dn+ '\nCheck for Updates...'+dn+dn)
		time.sleep(0.5)
		uda.check()
		time.sleep(DEF_WAIT_TIME)

	elif select_method == b'1':
		tobin_str = input(dn+'Paste text here: ')

		tobin_array = bytearray(tobin_str, "utf-8")
		byte_list = []

		for byte in tobin_array:
			tobin_repr = bin(byte)

			byte_list.append(tobin_repr)
			#lenth_byte = len(byte_list)

		FILE_NAME = 'TEXT_TO_BINARY.txt'
		with open(FILE_NAME, 'w') as fl:
			writingFile = True

			tWrite = ""
			while writingFile:
				tWrite = ' '.join(map(str, byte_list))

				fl.write(tWrite)

				writingFile=False
				break

		print('Finished! Output is in %s' % FILE_NAME)

		if CONFIG_DEBUG:
			print('\n[DEBUG] ' + str(byte_list))

		time.sleep(DEF_WAIT_TIME)

	elif select_method == b'2':
		totext_int = input(dn+'Paste Binary Code here: ')
		totext_values = totext_int.split()

		totext_finish = ""
		for binary_value in totext_values:
			totext_aint = int(binary_value, 2)
			totext_char = chr(totext_aint)

			totext_finish += totext_char

		FILE_NAME = 'BINARY_TO_TEXT.txt'
		with open(FILE_NAME, 'w') as flg:
			flg.write(totext_finish)

		print('Finished! Output is in %s' % FILE_NAME)
		if CONFIG_DEBUG:
			print(totext_finish+dn+dn+totext_char+dn+str(totext_aint))

		time.sleep(DEF_WAIT_TIME)

exit()