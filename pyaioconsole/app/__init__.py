import argparse
import sys
from typing import Any
from typing import Awaitable
from typing import Callable
from typing import Coroutine
from typing import Dict
from typing import List
from typing import NamedTuple
from typing import Optional
from typing import Type

from rich.console import Console

from pyaioconsole.app.config import Settings
from pyaioconsole.app.config import load_from_env
from pyaioconsole.commands import Argument
from pyaioconsole.commands import Command
from pyaioconsole.commands import Option

console = Console()


class Application:
	_show_support: bool = True

	def __init__(self, settings: Settings, show_support: bool = True):
		self.settings = settings
		self.options = {
			"-h, --help": "show this message and exit",
			"-v, --version": "show program's version number and exit",
		}
		self.commands = {}

		self._show_support = show_support

		self._commands = {}
		self._options = []
		self._arguments = []

		self.options = {}
		self.arguments = {}

		self.parser = argparse.ArgumentParser(description=self.settings.BRIEF)
		self.subparsers = self.parser.add_subparsers(dest="command")

	def _new_command_parser(self, command_name, command):
		command_parser = self.subparsers.add_parser(command_name, help=command.help)

		for argument in self.arguments[command_name]:
			command_parser.add_argument(argument.name, help=argument.help)

		for option in self.options[command_name]:
			if option.is_flag:
				command_parser.add_argument(
					option.name,
					help=option.help,
					default=option.default,
					required=option.required,
					action="store_true",
				)
			else:
				command_parser.add_argument(
					option.name,
					help=option.help,
					default=option.default,
					required=option.required,
				)

	async def run(self):
		self._prework_commands()

		if len(sys.argv) > 0:
			if sys.argv[1] == "help":
				await self.help()
				return

		for command_name, command in self._commands.items():
			self._new_command_parser(command_name, command)

		await self.execute()

	async def execute(self):
		args = self.parser.parse_args()
		command_name = args.command

		vars_args = vars(args)
		del vars_args["command"]

		await self._commands[command_name].handler(**vars_args)

	def _prework_commands(self):
		for command_name, command in self._commands.items():
			options = [option for option in self._options if option.handler_name == command_name]
			arguments = [argument for argument in self._arguments if argument.handler_name == command_name]

			self.commands[command_name] = command.help
			self.options[command_name] = options
			self.arguments[command_name] = arguments

	def _add_command(self, command: Command):
		self._commands[command.name] = command

	def command(self, help: Optional[str] = None):
		def decorator(handler: Awaitable):
			self._add_command(Command(name=str(handler.__name__), help=help, handler=handler))
			return handler

		return decorator

	def argument(self, name: str, help: Optional[str] = None):
		def decorator(handler: Awaitable):
			self._arguments.append(Argument(handler_name=handler.__name__, name=name, help=help))
			return handler

		return decorator

	def option(
		self,
		name: str,
		help: Optional[str] = None,
		default: Optional[Any] = None,
		is_flag: Optional[bool] = False,
		required: Optional[bool] = False,
	):
		def decorator(handler: Awaitable):
			self._options.append(
				Option(
					handler_name=handler.__name__,
					name=name,
					help=help,
					default=default,
					is_flag=is_flag,
					required=required,
				)
			)
			return handler

		return decorator

	def _get_commands(self):
		result = []

		max_length = max([len(option) for option in self.commands.keys()]) * 2

		for option, desc in self.commands.items():
			adjusted_option = option.ljust(max_length)
			result.append(f"  [green]{adjusted_option}[/green]{desc}")

		return "\n".join(result)

	async def help(self):
		self._prework_commands()
		console.print(
			f"""[yellow]Usage[/yellow]: {self.settings.APP_NAME} [OPTIONS] COMMAND [ARGS]...

  {self.settings.BRIEF}
  {self.settings.LONG_DESC}

[bold blue]Available commands:[/bold blue]
{self._get_commands()}
		"""
		)
		if self._show_support:
			console.print("[italic dim]Powered by aioconsole: https://github.com/alexeev-prog/aioconsole[/italic dim]")


all = [load_from_env, Settings, Application]
