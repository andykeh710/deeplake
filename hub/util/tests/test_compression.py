import numpy as np
import pytest
from hub.util.compress import compress_array, decompress_array


parametrize_compressions = pytest.mark.parametrize("compression", ["jpeg", "png"])


@parametrize_compressions
def test_file(compression):
    # TODO
    pass


@parametrize_compressions
def test_array(compression):
    array = np.zeros((100, 100, 3), dtype="uint8")  # TODO: handle non-uint8
    compressed_buffer = compress_array(array, compression)

    assert len(compressed_buffer) < len(
        array.tobytes()
    ), "Compressed buffer should be smaller than uncompressed buffer."

    decompressed_array = decompress_array(compressed_buffer)
    np.testing.assert_array_equal(array, decompressed_array)
