################################################################################
# © Copyright 2021-2022 Zapata Computing Inc.
################################################################################
"""Types commonly encountered in orquestra repositories."""
from numbers import Number
from os import PathLike
from typing import Any, Dict, Protocol, Sequence, Union, runtime_checkable

import numpy as np
import sympy


@runtime_checkable
class Readable(Protocol):
    def read(self, size: int = 0) -> str:
        pass

    def writable(self) -> bool:
        pass


@runtime_checkable
class Writeable(Protocol):
    def write(self, content: str):
        pass

    def writable(self) -> bool:
        pass


AnyPath = Union[str, bytes, PathLike]

LoadSource = Union[Readable, AnyPath]

DumpTarget = Union[Writeable, AnyPath]

Specs = Union[str, Dict]

MATRIX_TYPES = Union[np.ndarray, sympy.Matrix]


Parameter = Union[sympy.Symbol, Number]
ParameterizedVector = Union[Sequence[Parameter], np.ndarray]


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool:
        """Return result of comparison self < other."""
