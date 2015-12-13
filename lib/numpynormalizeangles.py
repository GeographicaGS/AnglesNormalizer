# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2015.
#
#  __computeAngles method is based on a function developed
#  by Prasanth Nair (https://github.com/phn/angles)
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#



import numpy as np
from math import floor, ceil



class NumpyNormalizeAngles(object):

    def __init__(self, usenumpy=True, vect=True):
        """
        If usenumpy=True Numpy is used (default)

        vect=False is only for testing purposes. You must use vect=True.

        """

        self.__usenumpy = usenumpy
        self.__vect = vect


    def getValues(self, angles, lower=0, upper=360):
        """
        Normalize angles

        """

        if self.__usenumpy:

            if not isinstance(angles, np.ndarray):
                raise ValueError("---Error: angles is not a numpy array\n\tTry with usenumpy=False")

            if self.__vect:
                norm_angles = self.__computeAnglesVect(angles, lower, upper)
            else:
                vect_norm = np.vectorize(self.__computeAnglesNoVect)
                norm_angles = vect_norm(angles, lower, upper)


        else:
            if isinstance(angles, np.ndarray):
                raise ValueError("---Error: angles is a numpy array\n\tTry with usenumpy=True (default option)")

            norm_angles = self.__computeAnglesNoVect(angles, lower, upper)

        return norm_angles

    def __computeAnglesVect(self, num, lower, upper):
        """
        Normalize angle to range (lower, upper).
        Vectorized computation (with Numpy).

        This method is based on a function developed by Prasanth Nair
        https://github.com/phn/angles

        """

        # abs(num + upper) and abs(num - lower) are needed, instead of
        # abs(num), since the lower and upper limits need not be 0. We need
        # to add half size of the range, so that the final result is lower +
        # <value> or upper - <value>, respectively.

        res = num.copy()

        if lower >= upper:
            raise ValueError("Invalid lower and upper limits: (%s, %s)" % (lower, upper))

        res[(num > upper) | (num == lower)] =  lower + np.abs(res[(num > upper) | (num == lower)] + upper) % (abs(lower) + abs(upper))

        res[(num < lower) | (num == upper)] = upper - np.abs(res[(num < lower) | (num == upper)] - lower) % (abs(lower) + abs(upper))

        res[res == upper] = lower

        return res


    def __computeAnglesNoVect(self, num, lower, upper):
        """
        Normalize angle to range (lower, upper).
        Non vectorized computation.

        This method is based on a function developed by Prasanth Nair
        https://github.com/phn/angles

        """

        # abs(num + upper) and abs(num - lower) are needed, instead of
        # abs(num), since the lower and upper limits need not be 0. We need
        # to add half size of the range, so that the final result is lower +
        # <value> or upper - <value>, respectively.
        res = num

        if lower >= upper:
            raise ValueError("Invalid lower and upper limits: (%s, %s)" % (lower, upper))

        if num > upper or num == lower:
            num = lower + abs(num + upper) % (abs(lower) + abs(upper))

        if num < lower or num == upper:
            num = upper - abs(num - lower) % (abs(lower) + abs(upper))

        res = lower if num == upper else num

        res *= 1.0  # Make all numbers float, to be consistent

        return res
