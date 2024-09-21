from __future__ import annotations

from collections.abc import Callable
from typing import Any

from typing_extensions import Protocol, Buffer

class _FileLike(Protocol):
    def read(self, n: int) -> bytes: ...

def unpackb(
    packed: Buffer,
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

class Unpacker:
    def __init__(
        self,
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
    ): ...
    def feed(self, next_bytes: Buffer) -> None: ...
    def read_bytes(self, n: int) -> bytearray: ...
    def __iter__(self) -> Unpacker: ...
    def __next__(self) -> Any: ...
    def next(self) -> Any: ...
    def skip(self) -> None: ...
    def unpack(self) -> Any: ...
    def read_array_header(self) -> Any: ...
    def read_map_header(self) -> Any: ...
    def tell(self) -> int: ...

class Packer:
    def __init__(
        self,
        default: Callable[[Any], Any] | None = ...,
        use_single_float: bool = ...,
        autoreset: bool = ...,
        use_bin_type: bool = ...,
        strict_types: bool = ...,
        datetime: bool = ...,
        unicode_errors: str | None = ...,
    ): ...
    def pack(self, obj: Any) -> bytes: ...
    def pack_map_pairs(self, pairs: Any) -> bytes: ...
    def pack_array_header(self, n: int) -> bytes: ...
    def pack_map_header(self, n: int) -> bytes: ...
    def pack_ext_type(self, typecode: int, data: bytes) -> None: ...
    def bytes(self) -> bytes: ...
    def reset(self) -> None: ...
    def getbuffer(self) -> memoryview: ...
