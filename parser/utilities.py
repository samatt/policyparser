from glob import glob
import json
import os

def del_empty_configs(base, policy='privacypolicy'):
	for directory in glob(os.path.join(base,"*/raw/%s/*" % policy)):
		timestamp, company, directory, raw_path, parsed_path, html = load_raw(base, directory)
		if not timestamp:
			continue

		delete_file = False
		if os.path.exists(os.path.join(directory, 'parser_config.json')):
			with open(os.path.join(directory, 'parser_config.json'), 'r') as infile:
				config = json.load(infile)
				if config['func_name'] == '':
					delete_file = True

		if delete_file:
			os.remove(os.path.join(directory, 'parser_config.json'))


def load_raw(base, directory):
		timestamp = directory.split('/')[-1]
		company = directory.split('/')[1]
		website = [d for d in os.listdir(directory) if '.DS_Store' not in d and '.json' not in d][0]
		html_file = os.listdir(os.path.join(directory, website))[0]
		raw_path = os.path.join(directory, website, html_file)
		parsed_path = os.path.join(base, company, 'txt', '%s.txt'%timestamp)
		if '.DS_Store' in raw_path:
			return (False, False, False, False, False, False)
		with open(raw_path, encoding = "ISO-8859-1") as infile:
			return (timestamp, company, directory, raw_path, parsed_path, infile.read())

def load_all_raw(base, policy='tos'):
	"""
	Load html to be parsed
	"""
	for directory in glob(os.path.join(base,"*/raw/%s/*" % policy)):
		yield load_raw(base, directory)

		