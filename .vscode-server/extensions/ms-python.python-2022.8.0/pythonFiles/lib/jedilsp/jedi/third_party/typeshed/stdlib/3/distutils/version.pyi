from abc import abstractmethod
from typing import Optional, Pattern, Tuple, TypeVar, Union

_T = TypeVar("_T", bound=Version)

class Version:
    def __repr__(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self: _T, other: Union[_T, str]) -> bool: ...
    def __le__(self: _T, other: Union[_T, str]) -> bool: ...
    def __gt__(self: _T, other: Union[_T, str]) -> bool: ...
    def __ge__(self: _T, other: Union[_T, str]) -> bool: ...
    @abstractmethod
    def __init__(self, vstring: Optional[str] = ...) -> None: ...
    @abstractmethod
    def parse(self: _T, vstring: str) -> _T: ...
    @abstractmethod
    def __str__(self) -> str: ...
    @abstractmethod
    def _cmp(self: _T, other: Union[_T, str]) -> bool: ...

class StrictVersion(Version):
    version_re: Pattern[str]
    version: Tuple[int, int, int]
    prerelease: Optional[Tuple[str, int]]
    def __init__(self, vstring: Optional[str] = ...) -> None: ...
    def parse(self: _T, vstring: str) -> _T: ...
    def __str__(self) -> str: ...
    def _cmp(self: _T, other: Union[_T, str]) -> bool: ...

class LooseVersion(Version):
    component_re: Pattern[str]
    vstring: str
    version: Tuple[Union[str, int], ...]
    def __init__(self, vstring: Optional[str] = ...) -> None: ...
    def parse(self: _T, vstring: str) -> _T: ...
    def __str__(self) -> str: ...
    def _cmp(self: _T, other: Union[_T, str]) -> bool: ...