"""
Extract Privacy policies from Wayback html
"""
import click
from logzero import logger
import re
from bs4 import BeautifulSoup 
from parser.utilities import load_all_parsed

@click.command("dedup")
@click.pass_context

def dedup(ctx):
	dates = set()
	pattern = re.compile("(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, 2\d{3}")
	for policy in ['tos', 'privacypolicy']:
		for path, output_path, text in load_all_parsed(ctx.obj['base'], policy):
			match = pattern.findall(text) 
			if not match:
				logger.info('didnt find date in %s' % path)
				continue

			if match[0] not in dates:
				dates.add(match[0])
				logger.info('adding %s to dedup folder' % match[0])
				with open(output_path, 'w') as outfile:
					outfile.write(text)


