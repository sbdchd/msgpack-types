from __future__ import annotations

from collections.abc import Callable
from typing import Any

from typing_extensions import Protocol

from .exceptions import (
    BufferFull,
    ExtraData,
    FormatError,
    OutOfData,
    PackException,
    PackOverflowError,
    PackValueError,
    StackError,
    UnpackException,
    UnpackValueError,
)
from .ext import ExtType, Timestamp
from .fallback import Packer, Unpacker, unpackb

version: tuple[int, int, int] = ...
__version__: str = ...

class _WriteStream(Protocol):
    def write(self, b: bytes) -> int: ...

class _Stream(Protocol):
    def read(self) -> bytes: ...

class _FileLike(Protocol):
    def read(self, n: int) -> bytes: ...

def pack(
    o: Any,
    stream: _WriteStream,
    *,
    default: Callable[[Any], Any] | None = ...,
    use_single_float: bool = ...,
    autoreset: bool = ...,
    use_bin_type: bool = ...,
    strict_types: bool = ...,
    datetime: bool = ...,
    unicode_errors: str | None = ...,
) -> None: ...
def packb(
    o: Any,
    *,
    default: Callable[[Any], Any] | None = ...,
    use_single_float: bool = ...,
    autoreset: bool = ...,
    use_bin_type: bool = ...,
    strict_types: bool = ...,
    datetime: bool = ...,
    unicode_errors: str | None = ...,
) -> bytes: ...
def unpack(
    stream: _Stream,
    *,
    file_like: _FileLike | None = ...,
    read_size: int = ...,
    use_list: bool = ...,
    raw: bool = ...,
    timestamp: int = ...,
    strict_map_key: bool = ...,
    object_hook: Callable[[dict[Any, Any]], Any] | None = ...,
    object_pairs_hook: Callable[[list[tuple[Any, Any]]], Any] | None = ...,
    list_hook: Callable[[list[Any]], Any] | None = ...,
    unicode_errors: str | None = ...,
    max_buffer_size: int = ...,
    ext_hook: Callable[[int, bytes], Any] = ...,
    max_str_len: int = ...,
    max_bin_len: int = ...,
    max_array_len: int = ...,
    max_map_len: int = ...,
    max_ext_len: int = ...,
) -> Any: ...

load = unpack
loads = unpackb

dump = pack
dumps = packb

__all__ = [
    "BufferFull",
    "ExtType",
    "ExtraData",
    "FormatError",
    "OutOfData",
    "PackException",
    "PackOverflowError",
    "PackValueError",
    "Packer",
    "StackError",
    "Timestamp",
    "UnpackException",
    "UnpackValueError",
    "Unpacker",
    "__version__",
    "dump",
    "dumps",
    "load",
    "loads",
    "pack",
    "packb",
    "unpack",
    "unpackb",
    "version",
]
