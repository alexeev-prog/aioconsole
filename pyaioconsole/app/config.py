import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Settings:
	APP_NAME: str
	BRIEF: str
	LONG_DESC: str


async def load_from_env(env_file: str = ".env") -> Settings:
	"""
	Loads settings a from environment.

	:param		env_file:  The environment file
	:type		env_file:  str

	:returns:	settings dataclass
	:rtype:		Settings
	"""
	load_dotenv(env_file)

	app_name = os.getenv("APP_NAME", "App")
	brief = os.getenv("BRIEF", "Short brief description")
	long_desc = os.getenv("LONG_DESC", "Long description")

	return Settings(APP_NAME=app_name, BRIEF=brief, LONG_DESC=long_desc)
