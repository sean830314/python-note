from Mediator import Mediator
from Colleague_abs import Colleague_abs


class OptionColleague(Colleague_abs):
    """選擇權評分模型"""
    
    _mediator = None

    def __init__(self):
        self.prod = "期貨/選擇權"

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, val=Mediator):
        self._mediator = val

    def score(self):
        # Implement the real score model here.
        return 10