from rich.console import Console
from pyaioconsole.app.config import Settings, load_from_env

console = Console()


class Application:
	_show_support: bool = True

	def __init__(self, settings: Settings, show_support: bool = True):
		self.settings = settings
		self.options = {
			'-h, --help': 'show this message and exit',
			'-v, --version': 'show program\'s version number and exit'
		}
		self.commands = {
			'help': 'Show this message and exit'
		}

		self.show_support = show_support

	def _get_options(self):
		result = []

		max_length = max([len(option) for option in self.options.keys()]) + 2

		for option, desc in self.options.items():
			adjusted_option = option.ljust(max_length)
			result.append(f'  {adjusted_option}{desc}')

		return "\n".join(result)

	def _get_commands(self):
		result = []

		max_length = max([len(option) for option in self.commands.keys()]) * 2

		for option, desc in self.commands.items():
			adjusted_option = option.ljust(max_length)
			result.append(f'  [green]{adjusted_option}[/green]{desc}')

		return "\n".join(result)

	async def help(self):
		console.print(f'''[yellow]Usage[/yellow]: {self.settings.APP_NAME} [OPTIONS] COMMAND [ARGS]...

  {self.settings.BRIEF}
  {self.settings.LONG_DESC}

[bold blue]Available commands:[/bold blue]
{self._get_commands()}

[bold blue]Options:[/bold blue]
{self._get_options()}
		''')
		if self._show_support:
			console.print('[italic dim]Powered by aioconsole: https://github.com/alexeev-prog/aioconsole[/italic dim]')


all = [load_from_env, Settings, Application]
