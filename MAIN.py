import os,time,json
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

ResetColor = "\u001b[0m"


SC_ = "stngo_11.19"

DEF_WAIT_TIME = 2
DEF_INSTALLER_FOLDER = 'stngo\\'
DEF_FINISH_FOLDER = os.path.expanduser('~\\Documents\\'+DEF_INSTALLER_FOLDER)
DEF_OUTPUT_BINTEXT = 'BINARY_TO_TEXT.txt'
DEF_OUTPUT_TEXTBIN = 'TEXT_TO_BINARY.txt'

# Set Methods (easy to change for beginner-coders)
DEF_METHODS_PREFIX = []  # don't override it!
DEF_METHODS = []  # don't override it!

	# Adding Methods!
DEF_METHODS_PREFIX += ['%s[1]' % ResetColor]
DEF_METHODS += ['%s Text to Binary Code' % Green]

DEF_METHODS_PREFIX += ['%s[2]' % ResetColor]
DEF_METHODS += ['%s Binary Code to Text' % Green]

DEF_METHODS_PREFIX += ['%s[3]' % ResetColor]
DEF_METHODS += ['%s Exit' % Red]

DEF_METHODS_PREFIX += ['%s[4]' % ResetColor]
DEF_METHODS += ['%s Check for Updates' % Yellow]

DEF_METHODS_PREFIX += ['%s[5]' % ResetColor]
DEF_METHODS += ['%s Delete temporary files' % White]


pref_file = 'prefences.json'
reTitle = cty.windll.kernel32.SetConsoleTitleW
dn = "\n"

err_msg = [
	f"{Red}Can't load {pref_file} properly! Restart, or reinstall program, to use it!"
]

# Load some Functions, because i need it kekw
def loadMsg(number):
	print(err_msg[int(number)])
	input('Press Enter, to quit!\n') ; print(ResetColor)
	exit()
def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux
    else:
        os.system('clear')  # Support, but no build for it... Nice!


clear()
# Loading Prefences File
with open(pref_file, 'r') as pref_o: # Open File
	pref_data = pref_o.read() # Read pref and save it as var
	pref_data = json.loads(pref_data) # Loading as json

try:
	titl = pref_data['window']['title'] + pref_data['window']['title.prefix']
	reTitle(titl + 'Loading resources...') # Set as window-title
	logo_string=pref_data['window']['logo']
except:
	loadMsg(0)

if pref_data['DebugCode'] == SC_:  # I know, you can copy my debug code and paste it into prefences... i know, its useless xD
	CONFIG_DEBUG = True
else: CONFIG_DEBUG = False

if pref_data['InstallerBuild'] == '1':
	INSTALLERBUILD = True
else: INSTALLERBUILD = False


# Convert Logo binary to real text, to use it at the top
logo_string_values = logo_string.split()
main_logo = ""

for binary_value in logo_string_values:
	aint = int(binary_value, 2)

	ascii_char = chr(aint)

	main_logo += ascii_char

if INSTALLERBUILD:  # SET (IF INSTALLER) PATH
	if os.path.exists(DEF_FINISH_FOLDER):
		pass
	else: os.mkdir(DEF_FINISH_FOLDER)

	DEF_OUTPUT_BINTEXT = os.path.expanduser('~\\Documents\\'+DEF_INSTALLER_FOLDER+DEF_OUTPUT_BINTEXT)
	DEF_OUTPUT_TEXTBIN = os.path.expanduser('~\\Documents\\'+DEF_INSTALLER_FOLDER+DEF_OUTPUT_TEXTBIN)


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

	clear() # Beginn Methods

	print(main_logo + dn)

	reTitle(titl + 'Selecting a Method')
	print(
		f'{ResetColor}Select a method:' +dn+dn,
		DEF_METHODS_PREFIX[0] + DEF_METHODS[0] +dn,
		DEF_METHODS_PREFIX[1] + DEF_METHODS[1] +dn,
		DEF_METHODS_PREFIX[2] + DEF_METHODS[2] +dn,
		DEF_METHODS_PREFIX[3] + DEF_METHODS[3] +dn,
		DEF_METHODS_PREFIX[4] + DEF_METHODS[4] +dn
	)


	select_method = mcr.getch()


	# Selection Methods
	if select_method == b'3':
		runMethod = False
		break
	elif select_method == b'4':
		reTitle(titl + 'Checking for Updates')
		clear()
		print(main_logo +dn+ '\nCheck for Updates...'+dn+dn)
		time.sleep(0.5)
		uda.check()
		time.sleep(DEF_WAIT_TIME)
	elif select_method == b'5':
		reTitle(titl + 'Delete temporary files')
		try:
			os.remove(DEF_OUTPUT_BINTEXT)
		except: pass
		try:
			os.remove(DEF_OUTPUT_TEXTBIN)
		except: pass

		print('%sTemporary files deleted!' % ResetColor)
		time.sleep(DEF_WAIT_TIME)

	elif select_method == b'1':
		reTitle(titl + 'Encode text to binary code')

		tobin_str = input(dn+'Paste text here: ')

		tobin_array = bytearray(tobin_str, "utf-8")
		byte_list = []

		for byte in tobin_array:
			tobin_repr = bin(byte)

			byte_list.append(tobin_repr)
			#lenth_byte = len(byte_list)

		FILE_NAME = DEF_OUTPUT_TEXTBIN
		with open(FILE_NAME, 'w') as fl:
			writingFile = True

			tWrite = ""
			while writingFile:
				tWrite = ' '.join(map(str, byte_list))

				fl.write(tWrite)

				writingFile=False
				break

		print(f'{Green}Finished! Output is in %s{ResetColor}' % FILE_NAME)

		if CONFIG_DEBUG:
			print('\n[DEBUG] ' + str(byte_list))

		time.sleep(DEF_WAIT_TIME)
		os.startfile(DEF_FINISH_FOLDER)  # Open directory

	elif select_method == b'2':
		reTitle(titl + 'Decode binary code to text')
		totext_int = input(dn+'Paste Binary Code here: ')
		totext_values = totext_int.split()

		totext_finish = ""
		for binary_value in totext_values:
			totext_aint = int(binary_value, 2)
			totext_char = chr(totext_aint)

			totext_finish += totext_char

		FILE_NAME = DEF_OUTPUT_BINTEXT
		with open(FILE_NAME, 'w') as flg:
			flg.write(totext_finish)

		print(f'{Green}Finished! Output is in{dn}%s{ResetColor}' % FILE_NAME)
		if CONFIG_DEBUG:
			print(totext_finish+dn+dn+totext_char+dn+str(totext_aint))

		time.sleep(DEF_WAIT_TIME)
		os.startfile(DEF_FINISH_FOLDER)  # Open directory

	elif select_method == b'8':
		clear()
		print(f'Name: {pref_data["window"]["title"]}\nVersion: {pref_data["CurrentVersion"]}\n\n')  #NAME_VERSION
		print(
			'Methods:' +dn,
			str(DEF_METHODS) +dn,
			str(len(DEF_METHODS)) +dn+dn,
			str(DEF_METHODS_PREFIX) +dn,
			str(len(DEF_METHODS_PREFIX)) +dn,
		)
		print(DEF_OUTPUT_BINTEXT+ dn +DEF_OUTPUT_TEXTBIN)  #PATH

		input()

exit()