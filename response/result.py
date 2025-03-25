class ResponseResult:
    def __init__(self, response_time: float) -> None:
        self.__response_time = response_time

    @property
    def response_time(self) -> float:
        return self.__response_time
