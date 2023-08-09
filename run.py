import os, sys



SCRIPTS_DIRECTORY = "scripts"


def getScriptNames(script_directory):
	script_names = []
	for file in os.listdir(script_directory):
		if file.endswith(".py"):
			script_names.append(file)
	return script_names


def help():
	print(
"usage: python run.py <command> [arg1 ...]" 
"<command>:"
"	help: get help"
"	gcc XXX.c: compile C source file"
)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		help()
	match sys.argv[1]:
		case "ls":
			for filename in getScriptNames(SCRIPT_DIRECTORY):
				print(filename)
		case "gcc":
			os.system(f"gcc {sys.argv[2]} -o {sys.argv[3]}") 
		case _:
			print(f"error: command {sys.argv[1]} isn't implemented or doesn't exist")