from Mediator import Mediator
from Colleague_abs import Colleague_abs


class CreditColleague(Colleague_abs):
    """信貸評分模型"""
    
    _mediator = None

    def __init__(self):
        self.prod = "信貸"

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, val=Mediator):
        self._mediator = val

    def score(self):
        # Implement the real score model here.
        return 20