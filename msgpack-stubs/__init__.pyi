from __future__ import annotations

from collections.abc import Callable
from typing import Any, Dict, List, Optional, Tuple

from msgpack import _version, exceptions, ext
from msgpack._version import version
from msgpack.exceptions import (
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
from msgpack.ext import ExtType, Timestamp
from msgpack.fallback import Packer, Unpacker, unpackb
from typing_extensions import Protocol


class _Stream(Protocol):
    def read(self) -> bytes: ...


class _FileLike(Protocol):
    def read(n: int) -> bytes: ...


def pack(
    o: Any,
    stream: _Stream,
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
    "_version",
    "dump",
    "dumps",
    "exceptions",
    "ext",
    "load",
    "loads",
    "pack",
    "packb",
    "unpack",
    "unpackb",
    "version",
]
