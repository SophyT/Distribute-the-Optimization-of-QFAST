import tensorflow as tf
import numpy      as np
import scipy.linalg as la

from qfast import LocationModel
from qfast import hilbert_schmidt_distance
from qfast import GenericGate, get_pauli_n_qubit_projection
from qfast import pauli_dot_product, reset_tensor_cache


class TestGenericgateGetFunVals ( tf.test.TestCase ):

    def test_genericgate_get_fun_vals ( self ):
        reset_tensor_cache()
        lm = LocationModel( 4, 2 )
        gg = GenericGate( "Test", 4, 2, lm, loc_vals = [ 1, 0, 0, 0, 0, 0 ] )

        with tf.Session() as sess:
            sess.run( tf.global_variables_initializer() )
            fun_vals = gg.get_fun_vals( sess )

        self.assertTrue( np.array_equal( fun_vals, [ 0.25 ] * 16 ) )


if __name__ == '__main__':
    tf.test.main()
