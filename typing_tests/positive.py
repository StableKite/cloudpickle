import io
import math
from collections.abc import Callable
from pickle import PickleBuffer
from typing import assert_type

import cloudpickle
from cloudpickle import cloudpickle as implementation
from cloudpickle import cloudpickle_fast as compatibility


def make_adder(offset: int) -> Callable[[int], int]:
    def add(value: int) -> int:
        return value + offset

    return add


buffers: list[PickleBuffer] = []
payload = cloudpickle.dumps(make_adder(7))
assert_type(payload, bytes)
restored: object = cloudpickle.loads(payload)
assert callable(restored) and restored(5) == 12

stream = io.BytesIO()
assert_type(cloudpickle.dump({"count": 3}, stream), None)
stream.seek(0)
assert cloudpickle.load(stream) == {"count": 3}

buffer_data = cloudpickle.dumps(PickleBuffer(b"buffer-data"), 5, buffers.append)
assert (
    buffers and bytes(cloudpickle.loads(buffer_data, buffers=buffers)) == b"buffer-data"
)
assert_type(cloudpickle.Pickler(io.BytesIO(), 5, buffers.append), cloudpickle.Pickler)
assert_type(cloudpickle.CloudPickler(io.BytesIO()), cloudpickle.Pickler)
assert_type(implementation.dumps(3), bytes)
assert_type(compatibility.dumps(3), bytes)

cloudpickle.register_pickle_by_value(math)
assert_type(implementation.list_registry_pickle_by_value(), set[str])
assert "math" in implementation.list_registry_pickle_by_value()
cloudpickle.unregister_pickle_by_value(math)
assert "math" not in implementation.list_registry_pickle_by_value()


class Constructed:
    value: int = 8


assert_type(implementation.instance(Constructed), Constructed)
assert implementation.instance(Constructed).value == 8
assert implementation.subimport("math") is math
assert implementation.dynamic_subimport("generated", {"number": 9}).number == 9
