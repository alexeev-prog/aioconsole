import asyncio
from pyaioconsole.app import Application, Settings

settings = Settings(
	APP_NAME='Example App',
	BRIEF='Short brief description',
	LONG_DESC='aioconsole library example application'
)

app = Application(settings)


async def main():
	await app.help()


if __name__ == '__main__':
	asyncio.run(main())
