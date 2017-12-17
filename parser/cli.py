import click
from .commands.parse import parse
from .commands.clean import clean

@click.group()
@click.option('--base', default="data", help="Path to data directory")
@click.pass_context
def cli(ctx, base):
	""""
	policy parser: extract privacy policy and terms of service text for Facebook (and others in the future)
	"""
	ctx.obj["base"] = click.format_filename(base)

cli.add_command(parse)
cli.add_command(clean)