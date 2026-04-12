from pybeli.indicators.rsi import RSI
from pybeli.models.signal import Signal
from pybeli.strategies.rsistrategy import RSIStrategy
from tests.models.utils import create_datetime


def test_analyze_buy_signal() -> None:
    strategy = RSIStrategy(buy_threshold=30, sell_threshold=70)
    datetime = create_datetime(minute=0)
    ticker = "TEST"
    rsi = RSI(value=25, timestamp=datetime, ticker=ticker, interval="1d", window=14)
    signal = strategy.analyze(rsi)
    assert signal == Signal.BUY
    rsi = RSI(value=75, timestamp=datetime, ticker=ticker, interval="1d", window=14)
    signal = strategy.analyze(rsi)
    assert signal == Signal.SELL
    rsi = RSI(value=50, timestamp=datetime, ticker=ticker, interval="1d", window=14)
    signal = strategy.analyze(rsi)
    assert signal == Signal.WAIT
