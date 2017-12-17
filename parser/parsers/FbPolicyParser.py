from logzero import logger
from bs4 import BeautifulSoup 
from .PolicyParser import PolicyParser

class FbPolicyParser(PolicyParser):
	def __init__(self, raw_dir, timestamp, output_path, html, parser, force):
		PolicyParser.__init__(self, raw_dir, timestamp, output_path, html, parser, force)
		self.html = html

	def check_config(self):
		config = self.load_config()
		return self.is_configured(config)

	def run(self):
		config = self.load_config()
		f = getattr(self, config['func_name'])
		result = f(self.html)
		if result:
			return self.save_parsed(result)
		else:
			logger.warn('%s didn\'t work for %s' % (config['func_name'], self.raw_dir))
			return False

	def pp_parse_1(self, html):
		soup = BeautifulSoup(html, "html.parser")
		return '\n\r'.join([t.text for t in soup.select('body center table.bordertable')])

	def pp_parse_2(self, html):
		soup = BeautifulSoup(html, "html.parser")
		return soup.find('div', {'id': 'pagebody'}).text
	
	def pp_parse_3(self, html):
		soup = BeautifulSoup(html, "html.parser")
		return soup.find('div', {'id': 'page_body'}).text
	
	def pp_parse_4(self, html):
		soup = BeautifulSoup(html, "html.parser")
		return soup.find('div', {'class': 'UIStandardFrame_Content'}).text

	def pp_parse_5(self, html):
		soup = BeautifulSoup(html, "html.parser")
		return soup.find('div', {'class': 'UIFullPage_Container'}).text

	def pp_parse_6(self, html):
		soup = BeautifulSoup(html, "html.parser")
		return soup.find('div', {'id': 'contentArea'}).text
	
	def pp_parse_7(self, html):
		soup = BeautifulSoup(html, "html.parser")
		return soup.find('div', {'id': 'content'}).text
		
	def tos_parse_1(self, html):
		soup = BeautifulSoup(html, "html.parser")
		return soup.find('div', {'id': 'pagebody'}).text
	
	def tos_parse_2(self, html):
		soup = BeautifulSoup(html, "html.parser")
		return soup.find('div', {'id': 'content'}).text

	def parse_test(self, html):
		logger.info('Test parser')

