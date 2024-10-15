from dataclasses import dataclass
from math import isclose

MIN_FLOAT: float = 1e-10
MAX_FLOAT: float = 1e10


@dataclass(frozen=True)
class Interval:
    """Dataclass of interval, single point (eg. [1, 1]) is not supported.

    Parameters
    ----------
        lower : float
            The lower bound of the interval.
        upper : float
            The upper bound of the interval.
        lower_inclusive : bool, default=False
            Wether the interval includes the lower bound.
        upper_inclusive : bool, default=False
            Whether the interval includes the upper bound.

    Examples
    --------
    >>> itv= Interval(0, 1, lower_inclusive=True, upper_inclusive=False)
    >>> itv
    [0, 1)
    >>> 0.5 in itv
    True
    >>> 1 in itv
    False
    >>> 0 in itv
    False
    >>> itv.pseudo_bound()
    (0, 0.9999999999)
    """

    lower: int | float
    upper: int | float
    lower_inclusive: bool = False
    upper_inclusive: bool = False

    def __contains__(self, value: int | float) -> bool:
        if isinstance(value, (int, float)):
            if self.lower_inclusive:
                if self.upper_inclusive:
                    return self.lower <= value <= self.upper
                else:
                    return self.lower <= value < self.upper
            else:
                if self.upper_inclusive:
                    return self.lower < value <= self.upper
                else:
                    return self.lower < value < self.upper

        raise TypeError(f"Interval.__contains__ only supports real numbers, but you passed in a {type(value)}.")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Interval):
            return (
                isclose(self.lower, other.lower)
                and isclose(self.upper, other.upper)
                and self.lower_inclusive == other.lower_inclusive
                and self.upper_inclusive == other.upper_inclusive
            )

        raise TypeError(f"Interval.__eq__ only supports Interval, but you passed in a {type(other)}.")

    def __repr__(self) -> str:
        if self.lower_inclusive:
            if self.upper_inclusive:
                return f"[{self.lower}, {self.upper}]"
            else:
                return f"[{self.lower}, {self.upper})"
        else:
            if self.upper_inclusive:
                return f"({self.lower}, {self.upper}]"
            else:
                return f"({self.lower}, {self.upper})"

    def pseudo_lbound(self, eps: float = MIN_FLOAT) -> float:
        """Return the pseudo lower bound of the interval for numerical calculation.

        Parameters
        ----------
        eps : float
            The epsilon used to calculate the pseudo bound.

        Returns
        -------
        float
            The pseudo lower bound of the interval.
        """

        if self.lower_inclusive:
            return self.lower
        else:
            return self.lower + eps

    def pseudo_ubound(self, eps: float = MIN_FLOAT) -> float:
        """Return the pseudo upper bound of the interval for numerical calculation.

        Parameters
        ----------
        eps : float
            The epsilon used to calculate the pseudo bound.

        Returns
        -------
        float
            The pseudo upper bound of the interval.
        """

        if self.upper_inclusive:
            return self.upper
        else:
            return self.upper - eps

    def pseudo_bound(self, eps: float = MIN_FLOAT) -> tuple[float, float]:
        """Return the pseudo interval for numerical calculation.

        Parameters
        ----------
        eps : float
            The epsilon used to calculate the pseudo bound.

        Returns
        -------
        tuple[float, float]
            The pseudo interval for numerical calculation.
        """

        return (self.pseudo_lbound(eps), self.pseudo_ubound(eps))


class PowerAnalysisFloat(float):
    """自定义功效分析数值类型"""

    domain = Interval(-MAX_FLOAT, MAX_FLOAT, lower_inclusive=True, upper_inclusive=True)

    def __new__(cls, obj):
        if isinstance(obj, (int, float)):
            if obj not in cls.domain:
                raise ValueError(f"{obj} is not in {cls.domain}.")
            return super().__new__(cls, obj)
        elif obj is None:
            return None
        else:
            raise TypeError(f"{obj} must be either an int, float, or None.")

    @classmethod
    def pseudo_bound(cls) -> tuple[float, float]:
        """伪区间，用于数值计算。"""

        return cls.domain.pseudo_bound()


class Alpha(PowerAnalysisFloat):
    """显著性水平"""

    domain = Interval(0, 1)


class Power(PowerAnalysisFloat):
    """检验效能"""

    domain = Interval(0, 1)


class Mean(PowerAnalysisFloat):
    """均值"""

    domain = Interval(-MAX_FLOAT, MAX_FLOAT)


class STD(PowerAnalysisFloat):
    """标准差"""

    domain = Interval(0, MAX_FLOAT)


class Proportion(PowerAnalysisFloat):
    """率"""

    domain = Interval(0, 1)


class Percent(PowerAnalysisFloat):
    """百分比"""

    domain = Interval(0, 1)


class Ratio(PowerAnalysisFloat):
    """比例"""

    domain = Interval(0, MAX_FLOAT)


class Size(PowerAnalysisFloat):
    """样本量"""

    domain = Interval(0, MAX_FLOAT)


class DropOutRate(PowerAnalysisFloat):
    """脱落率"""

    domain = Interval(0, 1, lower_inclusive=True)


class DropOutSize(PowerAnalysisFloat):
    """脱落样本量"""

    domain = Interval(0, MAX_FLOAT, lower_inclusive=True)
