class ResponseResult:
    def __init__(self, response_time: float, requested_url: str) -> None:
        self.__response_time = response_time
        self.__requested_url = requested_url

    @property
    def response_time(self) -> float:
        return self.__response_time

    @property
    def requested_url(self) -> str:
        return self.__requested_url
