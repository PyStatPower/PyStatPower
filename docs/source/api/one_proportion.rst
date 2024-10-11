one_proportion
==============

.. py:function:: solve_for_sample_size(alpha, power, nullproportion, proportion, alternative, test_type, dropout_rate=0, full_output=True)

    Return sample size for one proportion test

    :param float alpha: The significance level of the test
    :param float power: The power of the test
    :param float nullproportion: The proportion under the null hypothesis
    :param float proportion: The proportion under the alternative hypothesis
    :param str alternative: The alternative hypothesis
    :param str test_type: The type of test
    :param optional[float] dropout_rate: The drop-out rate
    :param optional[bool] full_output: if set to True, return the full output

    :return: The sample size
    :rtype: float