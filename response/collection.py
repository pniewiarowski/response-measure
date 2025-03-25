from response.response import Response


class ResultCollection:
    def __init__(self, url: str) -> None:
        self.__results = []
        self.__url = url

    @property
    def url(self) -> str:
        return self.__url

    @property
    def finish_attempts(self) -> int:
        return len(self.__results)

    def append(self, response: Response) -> None:
        self.__results.append(response)

    def get_average_response_time(self) -> float:
        total: float = 0
        for response in self.__results:
            total += response.response_time

        return total / len(self.__results)
