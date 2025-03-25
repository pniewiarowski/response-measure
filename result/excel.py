from abc import ABC

from result.result import Result


class ExcelResult(Result, ABC):
    def out(self) -> None:
        pass
