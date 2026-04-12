from abc import ABC, abstractmethod
from typing import TypeVar

from pybeli.models.signal import Signal

IndicatorT = TypeVar("IndicatorT")


class Strategy[IndicatorT](ABC):
    """Abstract base class for all trading strategies.

    Type parameter IndicatorT is the indicator value type the strategy consumes
    (e.g. RSI, MACD). Concrete subclasses narrow this to a specific indicator.
    """

    @abstractmethod
    def analyze(self, data: IndicatorT) -> Signal:
        """
        Analyze the given indicator value and return a trading signal.

        Args:
            data: The indicator value to analyze.

        Returns:
            A trading signal indicating whether to buy, sell, or wait.
        """
        ...
