from typing import Any
from typing import Callable


class _Depends:
	def __init__(self, dependency: Callable[..., Any], cache: bool) -> None:
		self.dependency = dependency
		self.cache = cache


def Depends(dependency: Callable[..., Any], cache: bool = True) -> Any:
	return _Depends(dependency=dependency, cache=cache)
