"""
Extract Privacy policies from Wayback html
"""
import click
from logzero import logger
from bs4 import BeautifulSoup 
from parser.utilities import load_all_raw
from parser.parsers.FbPolicyParser import FbPolicyParser

@click.command("parse", )
@click.option('--parser', default="", help="optional <parser function name>")
@click.option('--force', is_flag=True, help="ignore hash and force parse")
@click.pass_context

def parse(ctx, parser, force):
	policies = ['privacypolicy', 'tos']
	# policies = ['tos']
	for policy in policies:
		for timestamp, company, directory, raw_path, parsed_path, html in load_all_raw(ctx.obj["base"], policy):
			if not timestamp:
				continue
			p = FbPolicyParser(directory, timestamp, '%s/%s/parsed/%s'%(ctx.obj["base"], company, policy), html, parser, force)
			if p.check_config():
				if p.should_parse(p.load_config()):
					successful = p.run()
					if not successful:
						break
			else:
				break
				logger.error('Config missing for %s. You need to add it.'% directory)

