from response.result import ResponseResult


class ResponseCollection:
    def __init__(self) -> None:
        self.__responses = []

    def append(self, response: ResponseResult) -> None:
        self.__responses.append(response)

    def get_average_response_time(self) -> float:
        total: float = 0
        for response in self.__responses:
            total += response.response_time

        return total / len(self.__responses)
