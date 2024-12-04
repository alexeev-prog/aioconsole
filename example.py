import asyncio

from pyaioconsole.app import Application
from pyaioconsole.app import Settings

settings = Settings(
	APP_NAME="Example App",
	BRIEF="Short brief description",
	LONG_DESC="aioconsole library example application",
)

app = Application(settings)


@app.command(help="Say hello")
@app.argument("name", help="name")
async def hello(name: str):
	print(f"Hello, {name}!")


@app.command(help="Say bye")
@app.argument("name", help="name")
async def bye(name: str):
	print(f"Bye, {name}!")


async def main():
	await app.run()


if __name__ == "__main__":
	asyncio.run(main())
