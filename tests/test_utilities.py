import unittest
from parser.utilities import load_all_raw
import re

class TestUtilities(unittest.TestCase):
	def test_load_fb(self):
		base = 'data'
		timestamp_pattern = re.compile('\d{14}$')
		policies = ['tos', 'privacypolicy']
		company = 'facebook'
		test_website = 'www.%s.com' % company
		for policy in policies:
			filepath =  'terms.php' if policy == 'tos' else 'policy.php'
			for timestamp, website, directory, raw_path, parsed_path, html in load_all_raw(base, policy):
				self.assertTrue(website, test_website)
				self.assertTrue(timestamp_pattern.match(timestamp))
				print(directory)
				self.assertEqual(raw_path, '%s/%s/raw/%s/%s/%s/%s' % (base, company, policy, timestamp, website, filepath))
				self.assertEqual(directory, '%s/%s/raw/%s/%s' % (base, company, policy, timestamp))
				self.assertEqual(parsed_path, '%s/%s/txt/%s.txt' % (base, company, timestamp))
				self.assertTrue(isinstance(html, str))
				length = len(html) > 0
				self.assertTrue(length)

if __name__ == '__main__':
	unittest.main()

