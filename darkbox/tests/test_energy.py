from darkbox import energy

from numpy.testing import assert_equal
import numpy as np

def test_square():
	y = energy.square(np.array([1,2,3]))
	assert_equal(y,14)
