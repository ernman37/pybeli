from abc import ABC, abstractmethod
from typing import TypeVar

from pybeli.models.candle import Candle

IndicatorValueT = TypeVar("IndicatorValueT")


class Indicator[IndicatorValueT](ABC):
    """Abstract base class for all technical indicators.

    Type parameter IndicatorValueT is the model the indicator produces
    (e.g. RSI, MACD). Concrete subclasses narrow this to a specific output type.
    """

    @staticmethod
    @abstractmethod
    def calculate(candles: list[Candle]) -> list[IndicatorValueT]:
        """
        Calculate the indicator values for a list of candles.

        Args:
            candles: The ordered list of Candle objects to calculate over.

        Returns:
            An ordered list of indicator value objects aligned with the candles.
        """
        ...
