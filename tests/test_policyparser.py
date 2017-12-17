import unittest
from parser.parsers.PolicyParser import PolicyParser
from parser.parsers.FbPolicyParser import FbPolicyParser
from parser.utilities import load_raw
import re
import inspect

class TestPolicyParser(unittest.TestCase):
	def test_set_config_fb_privacy_policy(self):
		html = "<h1> SOME TEST HTML </h1>"
		p = FbPolicyParser('tests/test_data', '20050809235134', 'tests/test_data/out', html)
		config = p.set_config('parse_test', 'config_test.json')
		self.assertTrue(config['func_name'] == 'parse_test')
		self.assertTrue(config['func_hash'] == 'e8e5dc331aabb47b8e22d6e4e9f502ea')
		

	def test_load_config(self):
		html = "<h1> SOME TEST HTML </h1>"
		p = PolicyParser('tests/test_data', '20050809235134', 'tests/test_data/out', html)
		config = p.load_config('config_test.json')
		self.assertTrue(set(config.keys()) == set(['func_name', 'func_hash']))

	def test_should_parse(self):
		html = "<h1> SOME TEST HTML </h1>"
		p = FbPolicyParser('tests/test_data', '20050809235134', 'tests/test_data/out', html)
		config = p.load_config('config_test.json')
		if p.is_configured(config) :
			self.assertTrue(p.should_parse(config))

	# def test_parse_fb_privacy_policy(self):
	# 	timestamp, website, directory, raw_path, parsed_path, html = load_raw('data', 'data/facebook/raw/privacypolicy/20050809235134')
	# 	p = FbPolicyParser(directory	, 'data/facebook/parsed', html)
	# 	p.run()

if __name__ == '__main__':
	unittest.main()

