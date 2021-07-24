from __future__ import annotations
from typing import NamedTuple
import datetime

class _ExtType(NamedTuple):
    code: int
    data: bytes

class ExtType(_ExtType): ...

class TimeStamp:
    def __init__(self, seconds: int, nanoseconds: int = ...) -> None: ...
    def __eq__(self, o: object) -> bool: ...
    def __ne__(self, o: object) -> bool: ...
    @staticmethod
    def from_bytes(b: bytes) -> TimeStamp: ...
    @staticmethod
    def to_bytes(self) -> bytes: ...
    @staticmethod
    def from_unix(self, unix_sec: float) -> TimeStamp: ...
    def to_unix(self) -> float: ...
    @staticmethod
    def from_unix_nano(unix_ns: int) -> TimeStamp: ...
    @staticmethod
    def to_unix_nano(self) -> int: ...
    def to_datetime(self) -> datetime.datetime: ...
    @staticmethod
    def from_datetime(dt: datetime.datetime) -> TimeStamp: ...

