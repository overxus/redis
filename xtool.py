import os, sys, json


def loadScriptPath() -> str:
	with open('.xtool.config', 'r', encoding='utf-8') as reader:
		config_dict = json.load(reader)
		script_path = config_dict.get('script_path', None)
		if script_path is None:
			raise ValueError('.xtool.config doesn\'t exists key <script_path>')
	return script_path
	

def loadScriptNames(script_path: str) -> list[str]:
	script_names = []
	for filename in os.listdir(script_path):
		if filename.endswith('.py'):
			script_names.append(filename.rstrip('.py'))
	return script_names


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('usage: xtool <command> [arg1 ...]')
	script_path = loadScriptPath()
	script_names = loadScriptNames(script_path)
	if sys.argv[1] == 'ls':
		for script_name in script_names:
			print(script_name)
	elif sys.argv[1] in script_names:
		script_path = os.path.join(script_path, sys.argv[1])
		match sys.argv[1]:
			case 'update': 
				sys.argv.append(os.path.join(os.getcwd(), 'xtool.py'))
				sys.argv.append(os.getcwd())
		os.system(f'python {script_path}.py {" ".join(sys.argv[2:])}')
	else:
		print(f'error: can\'t find command {sys.argv[1]}')
