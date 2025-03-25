from abc import ABC, abstractmethod

from response.collection import ResultCollection


class Result(ABC):
    def __init__(self, results: ResultCollection):
        self._results = results

    @abstractmethod
    def out(self):
        pass
