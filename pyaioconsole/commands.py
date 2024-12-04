from dataclasses import dataclass
from dataclasses import field
from typing import Awaitable
from typing import List


@dataclass
class Argument:
	handler_name: str
	name: str
	help: str


@dataclass
class Option:
	handler_name: str
	name: str
	help: str
	default: str = None
	is_flag: bool = False
	required: bool = False


@dataclass
class Command:
	name: str
	help: str
	handler: Awaitable
	arguments: List[Argument] = field(default_factory=list)
	options: List[Option] = field(default_factory=list)
