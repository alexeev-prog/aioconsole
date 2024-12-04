# aioconsole

<a id="readme-top"></a> 

<div align="center">  
  <p align="center">
    Simple python library for creating async CLI applications
    <br />
    <a href="./docs/en/index.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#getting-started">Getting Started</a>
    ·
    <a href="#usage-examples">Basic Usage</a>
    ·
    <a href="https://github.com/alexeev-prog/aioconsole/blob/main/LICENSE">License</a>
  </p>
</div>
<br>
<p align="center">
    <img src="https://img.shields.io/github/languages/top/alexeev-prog/aioconsole?style=for-the-badge">
    <img src="https://img.shields.io/github/languages/count/alexeev-prog/aioconsole?style=for-the-badge">
    <img src="https://img.shields.io/github/license/alexeev-prog/aioconsole?style=for-the-badge">
    <img src="https://img.shields.io/github/stars/alexeev-prog/aioconsole?style=for-the-badge">
    <img src="https://img.shields.io/github/issues/alexeev-prog/aioconsole?style=for-the-badge">
    <img src="https://img.shields.io/github/last-commit/alexeev-prog/aioconsole?style=for-the-badge">
</p>

## Getting Started
aioconsole is available on [PyPI](https://pypi.org/project/aioconsole). Simply install the package into your project environment with PIP:

```bash
pip install pyaioconsole
```

## Usage Examples

```python
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
```
