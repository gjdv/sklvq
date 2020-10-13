from . import ActivationBaseClass
import numpy as np


class Identity(ActivationBaseClass):
    """ Identity function

    Class that holds the identity function and gradient.

    See also
    --------
    Sigmoid, SoftPlus, Swish
    """
    __slots__ = ()

    def __call__(self, x: np.ndarray) -> np.ndarray:
        """ Implementation of the identity function:
            .. math::

                f(\\vec{x}) = \\vec{x}

        Parameters
        ----------
        x : ndarray of any shape

        Returns
        -------
        x : ndarray
            Elementwise evaluation of the identity function.
        """
        return x

    def gradient(self, x: np.ndarray) -> np.ndarray:
        """ The identity functions's gradient:
            .. math::

                \\frac{\\partial f}{\\partial \\vec{x}} = \\vec{1}

        Parameters
        ----------
        x : ndarray

        Returns
        -------
        ndarray of shape (x.shape)
            Elementwise evaluation of the identity function's gradient.
        """
        return np.ones_like(x)