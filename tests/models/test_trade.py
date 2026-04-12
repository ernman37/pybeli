from datetime import datetime

from pybeli.models.signal import Signal
from pybeli.models.trade import Trade


def test_trade_model() -> None:
    trade = Trade(
        ticker="AAPL",
        quantity=10,
        price=150.0,
        timestamp=datetime.now(),
        trade_type=Signal.BUY,
    )
    assert trade.amount == 1500.0


def test_trade_model_throws_invalid_trade_type() -> None:
    try:
        Trade(
            ticker="AAPL",
            quantity=10,
            price=150.0,
            timestamp=datetime.now(),
            trade_type=Signal.WAIT,
        )
        raise AssertionError()
    except ValueError:
        assert True
