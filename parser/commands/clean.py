"""
Extract Privacy policies from Wayback html
"""
import click
from logzero import logger
from bs4 import BeautifulSoup 
from parser.utilities import del_empty_configs

@click.command("clean")
@click.pass_context
def clean(ctx):
	del_empty_configs(ctx.obj["base"])


