from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from pybeli.models.signal import Signal


class Trade(BaseModel):
    """Represents a trade executed in the market."""

    ticker: str = Field(..., description="The ticker symbol for the asset")
    quantity: float = Field(..., description="The quantity of the asset traded")
    price: float = Field(..., description="The price at which the trade was executed")
    timestamp: datetime = Field(..., description="The timestamp of the trade execution")
    trade_type: Signal = Field(..., description="The type of trade (buy or sell)")

    @property
    def amount(self) -> float:
        """
        Calculate the total amount of the trade

        Returns:
            The total amount of the trade (quantity * price).
        """
        return self.quantity * self.price

    @field_validator("trade_type")
    def validate_trade_type(cls, value: Signal) -> Signal:
        if value not in (Signal.BUY, Signal.SELL):
            raise ValueError("Invalid trade type")
        return value
