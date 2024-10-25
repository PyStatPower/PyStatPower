from math import ceil

import pytest

from pystatpower.models import one_proportion


class TestSolveForSampleSize:
    test_data = [
        # (alpha, power, nullproportion, proportion, alternative, test_type, expected_result)
        ((0.05, 0.80, 0.80, 0.95, "TWO_SIDED", "EXACT_TEST"), 42),
        ((0.05, 0.80, 0.80, 0.95, "ONE_SIDED", "EXACT_TEST"), 32),
        ((0.05, 0.80, 0.80, 0.95, "TWO_SIDED", "Z_TEST_USING_S_P0"), 42),
        ((0.05, 0.80, 0.80, 0.95, "TWO_SIDED", "Z_TEST_USING_S_P0_CC"), 49),
        ((0.05, 0.80, 0.80, 0.95, "TWO_SIDED", "Z_TEST_USING_S_PHAT"), 17),
        ((0.05, 0.80, 0.80, 0.95, "TWO_SIDED", "Z_TEST_USING_S_PHAT_CC"), 23),
    ]

    test_data_raise_error = [
        # (alpha, power, nullproportion, proportion, alternative, test_type, expected_error)
        ((0.05, 0.80, 0.80, 0.80, "TWO_SIDED", "EXACT_TEST"), ValueError),
    ]

    @pytest.mark.parametrize(("params", "result"), test_data)
    def test_solve(self, params, result):
        result = one_proportion.solve_for_sample_size(*params)
        assert ceil(result) == result

    @pytest.mark.parametrize(("params", "expected_error"), test_data_raise_error)
    def test_solve_raise_error(self, params, expected_error):
        with pytest.raises(expected_error):
            one_proportion.solve_for_sample_size(*params)

    def test_solve_full_output(self):
        result = one_proportion.solve_for_sample_size(
            0.05, 0.80, 0.80, 0.95, "TWO_SIDED", "EXACT_TEST", full_output=True
        )
        assert isinstance(result, one_proportion.OneProportion.ForSize)


class TestSolveForAlpha:
    params_list = [
        # (expected_result, size, power, nullproportion, proportion, alternative, test_type)
        (0.05, 42, 0.80, 0.80, 0.95, "TWO_SIDED", "EXACT_TEST"),
    ]

    def test_solve(self):
        for (
            expected_result,
            size,
            power,
            nullproportion,
            proportion,
            alternative,
            test_type,
        ) in TestSolveForAlpha.params_list:
            result = one_proportion.solve_for_alpha(
                size=size,
                power=power,
                nullproportion=nullproportion,
                proportion=proportion,
                alternative=alternative,
                test_type=test_type,
            )
            assert round(result, 2) == expected_result

    def test_solve_full_output(self):
        result = one_proportion.solve_for_alpha(70, 0.80, 0.80, 0.95, "TWO_SIDED", "EXACT_TEST", full_output=True)
        assert isinstance(result, one_proportion.OneProportion.ForAlpha)


class TestSolveForPower:
    params_list = [
        # (expected_result, size, alpha, nullproportion, proportion, alternative, test_type)
        (0.80598, 42, 0.05, 0.80, 0.95, "TWO_SIDED", "EXACT_TEST"),
        (0.92528, 42, 0.05, 0.80, 0.95, "ONE_SIDED", "EXACT_TEST"),
        (0.80598, 42, 0.05, 0.80, 0.95, "TWO_SIDED", "Z_TEST_USING_S_P0"),
        (0.69469, 42, 0.05, 0.80, 0.95, "TWO_SIDED", "Z_TEST_USING_S_P0_CC"),
        (0.99380, 42, 0.05, 0.80, 0.95, "TWO_SIDED", "Z_TEST_USING_S_PHAT"),
        (0.98408, 42, 0.05, 0.80, 0.95, "TWO_SIDED", "Z_TEST_USING_S_PHAT_CC"),
    ]

    def test_solve(self):
        for (
            expected_result,
            size,
            alpha,
            nullproportion,
            proportion,
            alternative,
            test_type,
        ) in TestSolveForPower.params_list:
            result = one_proportion.solve_for_power(
                size=size,
                alpha=alpha,
                nullproportion=nullproportion,
                proportion=proportion,
                alternative=alternative,
                test_type=test_type,
            )
            assert round(result, 5) == expected_result

    def test_solve_full_output(self):
        result = one_proportion.solve_for_power(70, 0.05, 0.80, 0.95, "TWO_SIDED", "EXACT_TEST", full_output=True)
        assert isinstance(result, one_proportion.OneProportion.ForPower)


class TestSolveForNullProportion:
    params_list = [
        # (expected_result, size, alpha, power, proportion, alternative, test_type, search_direction)
        (0.80, 42, 0.05, 0.80, 0.95, "TWO_SIDED", "EXACT_TEST", "LESS"),
        (1.00, 42, 0.05, 0.80, 0.95, "TWO_SIDED", "EXACT_TEST", "GREATER"),
    ]

    params_raise_error_list = [
        # (expected_error, size, alpha, power, proportion, alternative, test_type, search_direction)
        (ValueError, 42, 0.05, 0.80, 0.05, "TWO_SIDED", "Z_TEST_USING_S_PHAT_CC", "LESS"),
        (ValueError, 42, 0.05, 0.80, 0.95, "TWO_SIDED", "Z_TEST_USING_S_PHAT_CC", "GREATER"),
    ]

    def test_solve(self):
        for (
            expected_result,
            size,
            alpha,
            power,
            proportion,
            alternative,
            test_type,
            search_direction,
        ) in TestSolveForNullProportion.params_list:
            result = one_proportion.solve_for_nullproportion(
                size=size,
                alpha=alpha,
                power=power,
                proportion=proportion,
                alternative=alternative,
                test_type=test_type,
                search_direction=search_direction,
            )
            assert round(result, 2) == expected_result

        for (
            expected_error,
            size,
            alpha,
            power,
            proportion,
            alternative,
            test_type,
            search_direction,
        ) in TestSolveForNullProportion.params_raise_error_list:
            with pytest.raises(expected_error):
                one_proportion.solve_for_nullproportion(
                    size=size,
                    alpha=alpha,
                    power=power,
                    proportion=proportion,
                    alternative=alternative,
                    test_type=test_type,
                    search_direction=search_direction,
                )

    def test_solve_full_output(self):
        result = one_proportion.solve_for_nullproportion(
            70, 0.05, 0.80, 0.95, "TWO_SIDED", "EXACT_TEST", "LESS", full_output=True
        )
        assert isinstance(result, one_proportion.OneProportion.ForNullProportion)


class TestSolveForProportion:
    params_list = [
        # (expected_result, size, alpha, power, nullproportion, alternative, test_type, search_direction)
        (0.6237, 42, 0.05, 0.80, 0.80, "ONE_SIDED", "Z_TEST_USING_S_P0_CC", "LESS"),
        (0.9434, 42, 0.05, 0.80, 0.80, "ONE_SIDED", "Z_TEST_USING_S_P0_CC", "GREATER"),
    ]

    params_raise_error_list = [
        # (expected_error, size, alpha, power, nullproportion, alternative, test_type, search_direction)
        (ValueError, 4, 0.05, 0.80, 0.00001, "TWO_SIDED", "Z_TEST_USING_S_PHAT_CC", "LESS"),
        (ValueError, 4, 0.05, 0.80, 0.99999, "TWO_SIDED", "Z_TEST_USING_S_PHAT_CC", "GREATER"),
    ]

    def test_solve(self):
        for (
            expected_result,
            size,
            alpha,
            power,
            nullproportion,
            alternative,
            test_type,
            search_direction,
        ) in TestSolveForProportion.params_list:
            result = one_proportion.solve_for_proportion(
                size=size,
                alpha=alpha,
                power=power,
                nullproportion=nullproportion,
                alternative=alternative,
                test_type=test_type,
                search_direction=search_direction,
            )
            assert round(result, 4) == expected_result

        for (
            expected_error,
            size,
            alpha,
            power,
            nullproportion,
            alternative,
            test_type,
            search_direction,
        ) in TestSolveForProportion.params_raise_error_list:
            with pytest.raises(expected_error):
                one_proportion.solve_for_proportion(
                    size=size,
                    alpha=alpha,
                    power=power,
                    nullproportion=nullproportion,
                    alternative=alternative,
                    test_type=test_type,
                    search_direction=search_direction,
                )

    def test_solve_full_output(self):
        result = one_proportion.solve_for_proportion(
            70, 0.05, 0.80, 0.95, "TWO_SIDED", "EXACT_TEST", "LESS", full_output=True
        )
        assert isinstance(result, one_proportion.OneProportion.ForProportion)
