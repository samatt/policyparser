from logzero import logger
import os
import hashlib
import json
import inspect
class PolicyParser:

	def __init__(self, raw_dir, timestamp, output_path, html, parser, force):
		self.raw_dir = raw_dir
		self.timestamp = timestamp
		self.parser = parser
		self.output_path = output_path
		self.html = html
		self.force = force
	
	def config_exists(self, filename):
		return os.path.exists(os.path.join(self.raw_dir, filename))

	def create_config(self, filename):
		config = {'func_hash': '',
			'func_name': self.parser}
		with open(os.path.join(self.raw_dir, filename), 'w') as f:
			json.dump(config, f, ensure_ascii=False, sort_keys=True, indent=2)
		return config
	
	def set_config(self, func_name, filename='parser_config.json'):
		try:
			config = {'func_hash': self.get_function_hash(func_name),
				'func_name': func_name}
			with open(os.path.join(self.raw_dir, filename), 'w') as f:
				json.dump(config, f, ensure_ascii=False, sort_keys=True, indent=2)
			return config
		except Exception as e:
			logger.error('Couldn\'t set config')
			raise e

	def get_function_hash(self, func_name):
		func_source = inspect.getsource(getattr(self, func_name))
		hash_object = hashlib.md5(func_source.strip().encode())
		return  hash_object.hexdigest()
	
	def is_configured(self, config):
		if not config['func_name']:
			logger.error('No function assigned for %s/parser_config.json' % self.raw_dir)
			return False

		if not config['func_hash']:
			logger.warn('No hash for function %s. Assigning current hash' % config['func_name'])
			# self.set_config(func_name=config['func_name'])
			return True
		return True

	def should_parse(self, config):
		if self.force:
			logger.warn('Force flag detected. Ignoring has and parsing %s' % self.raw_dir)
			return True

		if config['func_hash'] != self.get_function_hash(config['func_name']):
			logger.warn('Function hash in %s is different, should parse' % self.raw_dir)
			self.set_config(func_name=config['func_name'])
			return True
		logger.info('Parser did not change since last run')
		return False


	def load_config(self, filename='parser_config.json'):
		if self.config_exists(filename):
			with open(os.path.join(self.raw_dir, filename), 'r') as infile:
				return json.load(infile)
		else:
			return self.create_config(filename)

	def save_parsed(self, parsed):
		with open('%s/%s.txt' % (self.output_path, self.timestamp), 'w') as outfile:
			logger.debug('saving %s/%s.txt' % (self.output_path, self.timestamp))
			outfile.write(parsed)
			return True