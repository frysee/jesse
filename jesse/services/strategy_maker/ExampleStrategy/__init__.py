from jesse.strategies import Strategy, cached


class ExampleStrategy(Strategy):
    def should_long(self) -> bool:
        return False

    def should_short(self) -> bool:
        return False

    def should_cancel(self) -> bool:
        return True

    def go_long(self):
        pass

    def go_short(self):
        pass
