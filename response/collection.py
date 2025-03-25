from response.response import Response


class ResultCollection:
    def __init__(self, url: str, attempts: int) -> None:
        self.__results = []
        self.__url = url
        self.__finish_attempts = 0
        self.__attempts = attempts

    @property
    def url(self) -> str:
        return self.__url

    @property
    def finish_attempts(self) -> int:
        return self.__finish_attempts

    def increase_finish_attempts(self) -> None:
        self.__finish_attempts += 1

    def append(self, response: Response) -> None:
        self.__results.append(response)

    def get_average_response_time(self) -> float:
        total: float = 0
        for response in self.__results:
            total += response.response_time

        return total / len(self.__results)
