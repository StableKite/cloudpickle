from cloudpickle import Pickler, loads
from io import BytesIO
from types import NotImplementedType
from typing import Callable


class Payload:
    def __init__(self, value: int = 0) -> None:
        self.value = value


def make() -> Payload:
    return Payload()


def restore(value: Payload, state: int) -> None:
    value.value = state


Reduction = tuple[
    Callable[..., object],
    tuple[object, ...],
    int,
    None,
    None,
    Callable[[Payload, int], None],
]


class Concrete(Pickler):
    def reducer_override(self, obj: object) -> Reduction | NotImplementedType:
        if isinstance(obj, Payload):
            return make, (), obj.value, None, None, restore
        return NotImplemented


def check() -> None:
    stream = BytesIO()
    Concrete(stream).dump(Payload(23))
    result: object = loads(stream.getvalue())
    assert isinstance(result, Payload) and result.value == 23


if __name__ == "__main__":
    check()
