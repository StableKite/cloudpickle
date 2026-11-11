import io
from pickle import PickleBuffer

import cloudpickle


def wrong_buffer_callback(value: str) -> None:
    pass


cloudpickle.dumps(3, protocol="5")
cloudpickle.dump(3, io.StringIO())
cloudpickle.dumps(3, buffer_callback=wrong_buffer_callback)
cloudpickle.Pickler(io.StringIO())
cloudpickle.Pickler(io.BytesIO(), buffer_callback=lambda left, right: None)
cloudpickle.register_pickle_by_value("math")
cloudpickle.unregister_pickle_by_value(3)
cloudpickle.loads("not a bytes buffer")
cloudpickle.dumps(3, fix_imports=True)
payload: str = cloudpickle.dumps(PickleBuffer(b"data"))
