import tensorflow as tf
import numpy      as np
import scipy.linalg as la

from qfast import hilbert_schmidt_distance
from qfast import FixedGate, get_pauli_n_qubit_projection
from qfast import pauli_dot_product, reset_tensor_cache


class TestFixedgateGetLocation ( tf.test.TestCase ):

    def test_fixedgate_get_location ( self ):
        reset_tensor_cache()
        fg = FixedGate( "Test", 4, 2, (0, 1) )
        self.assertTrue( np.array_equal( fg.get_location(), (0, 1) ) )


if __name__ == '__main__':
    tf.test.main()
