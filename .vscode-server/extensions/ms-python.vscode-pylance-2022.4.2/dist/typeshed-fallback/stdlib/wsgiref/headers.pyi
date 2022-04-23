from typing import Pattern, overload
from typing_extensions import TypeAlias

_HeaderList: TypeAlias = list[tuple[str, str]]

tspecials: Pattern[str]  # undocumented

class Headers:
    def __init__(self, headers: _HeaderList | None = ...) -> None: ...
    def __len__(self) -> int: ...
    def __setitem__(self, name: str, val: str) -> None: ...
    def __delitem__(self, name: str) -> None: ...
    def __getitem__(self, name: str) -> str | None: ...
    def __contains__(self, name: str) -> bool: ...
    def get_all(self, name: str) -> list[str]: ...
    @overload
    def get(self, name: str, default: str) -> str: ...
    @overload
    def get(self, name: str, default: str | None = ...) -> str | None: ...
    def keys(self) -> list[str]: ...
    def values(self) -> list[str]: ...
    def items(self) -> _HeaderList: ...
    def __bytes__(self) -> bytes: ...
    def setdefault(self, name: str, value: str) -> str: ...
    def add_header(self, _name: str, _value: str | None, **_params: str | None) -> None: ...
