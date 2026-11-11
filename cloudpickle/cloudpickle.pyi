import abc as abc
import builtins as builtins
import copyreg as copyreg
import dataclasses as dataclasses
import dis as dis
import io as io
import itertools as itertools
import logging as logging
import opcode as opcode
import pickle as pickle
import platform as platform
import struct as struct
import sys as sys
import threading as threading
import types as types
import typing as typing
import uuid as uuid
import warnings as warnings
import weakref as weakref
from _typeshed import SupportsWrite
from collections import ChainMap as ChainMap, OrderedDict as OrderedDict
from enum import Enum as Enum
from pickle import PickleBuffer, load as load, loads as loads
from types import CellType as CellType, ModuleType, NotImplementedType
from typing import Callable, Iterator, Mapping, TypeVar

_T = TypeVar("_T")
_BufferCallback = Callable[[PickleBuffer], object]
_Reduction = (
    str
    | tuple[Callable[..., object], tuple[object, ...]]
    | tuple[Callable[..., object], tuple[object, ...], object]
    | tuple[Callable[..., object], tuple[object, ...], object, Iterator[object] | None]
    | tuple[
        Callable[..., object],
        tuple[object, ...],
        object,
        Iterator[object] | None,
        Iterator[object] | None,
    ]
    | tuple[
        Callable[..., object],
        tuple[object, ...],
        object,
        Iterator[object] | None,
        Iterator[object] | None,
        Callable[[object, object], object] | None,
    ]
)
_DispatchTable = Mapping[type[object], Callable[[object], _Reduction]]

DEFAULT_PROTOCOL: int
PYPY: bool
builtin_code_type: type[object] | None
STORE_GLOBAL: int
DELETE_GLOBAL: int
LOAD_GLOBAL: int
GLOBAL_OPS: tuple[int, int, int]
HAVE_ARGUMENT: int
EXTENDED_ARG: int
k: str
v: object

def register_pickle_by_value(module: ModuleType) -> None: ...
def unregister_pickle_by_value(module: ModuleType) -> None: ...
def list_registry_pickle_by_value() -> set[str]: ...
def is_tornado_coroutine(func: object) -> bool: ...
def subimport(name: str) -> ModuleType: ...
def dynamic_subimport(name: str, vars: Mapping[str, object]) -> ModuleType: ...
def instance(cls: type[_T]) -> _T: ...

class Pickler(pickle.Pickler):
    dispatch: _DispatchTable
    globals_ref: dict[int, dict[str, object]]
    proto: int
    def __init__(
        self,
        file: SupportsWrite[bytes],
        protocol: int | None = None,
        buffer_callback: _BufferCallback | None = None,
    ) -> None: ...
    def dump(self, obj: object) -> None: ...
    def reducer_override(self, obj: object) -> _Reduction | NotImplementedType: ...

CloudPickler = Pickler

def dump(
    obj: object,
    file: SupportsWrite[bytes],
    protocol: int | None = None,
    buffer_callback: _BufferCallback | None = None,
) -> None: ...
def dumps(
    obj: object,
    protocol: int | None = None,
    buffer_callback: _BufferCallback | None = None,
) -> bytes: ...
