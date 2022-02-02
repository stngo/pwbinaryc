import os,time,sys,json
import ctypes as cty
import msvcrt as mcr
import Updater as uda

DEF_OUTPUT = 'output.txt'
DEF_WAIT_TIME = 1

pref_file = 'prefences.json'
reTitle = cty.windll.kernel32.SetConsoleTitleW
dn = "\n"

err_msg = [
	"Can't load %s properly! Restart, or reinstall program, to use it!" % pref_file,
]

# Load some Functions, because i need it kekw
def loadMsg(number):
	print(err_msg[int(number)])
	input('Press Enter, to quit!\n')
	exit()
def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux
    else:
        os.system('clear')



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
	print('Select:'+dn+dn+'[1] Text to Binary Code'+dn+'[2] Binary Code to Text'+dn+'[3] Exit'+dn)


	select_method = mcr.getch()


	# Selection Methods
	if select_method == b'3':
		runMethod = False
		break

	elif select_method == b'1':
		tobin_str = input(dn+'Paste text here: ')

		tobin_array = bytearray(tobin_str, "utf8")
		byte_list = []

		for byte in tobin_array:
			tobin_repr = bin(byte)

			byte_list.append(tobin_repr)
			lenth_byte = len(byte_list)

		FILE_NAME = 'TEXT_TO_BINARY.txt'
		with open(FILE_NAME, 'w') as fl:
			writingFile = True

			tWrite = ""
			while writingFile:
				try:
					tWrite += byte_list[lenth_byte]
				except IndexError:
					print(lenth_byte)
					writingFile = False ; break

				fl.write(tWrite)

				lenth_byte -= 1

				if lenth_byte == 0:
					print('Lenth is 0  -  %s' % lenth_byte)
					time.sleep(2)
					writingFile = False
					break
				else: continue

		print('Finished! Output is in %s' % FILE_NAME)
		print(tobin_repr)

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
		print(totext_finish+dn+dn+totext_char)

		time.sleep(DEF_WAIT_TIME)

exit()