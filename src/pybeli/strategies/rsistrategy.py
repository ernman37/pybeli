from pydantic import BaseModel, Field

from pybeli.indicators.rsi import RSI
from pybeli.models.signal import Signal
from pybeli.strategies.strategy import Strategy


class RSIStrategy(BaseModel, Strategy[RSI]):
    """
    A strategy for trading based on the Relative Strength Index (RSI) indicator.

    Attributes:
        buy_threshold: The RSI value below which to buy.
        sell_threshold: The RSI value above which to sell.
    """

    buy_threshold: float = Field(..., description="The RSI value below which to buy")
    sell_threshold: float = Field(..., description="The RSI value above which to sell")

    def analyze(self, rsi: RSI) -> Signal:
        """
        Analyze the RSI value and return a trading signal.

        Args:
            rsi: The RSI value to analyze.

        Returns:
            A trading signal indicating whether to buy, sell, or hold.
        """
        if rsi.value < self.buy_threshold:
            return Signal.BUY
        elif rsi.value > self.sell_threshold:
            return Signal.SELL
        return Signal.WAIT
