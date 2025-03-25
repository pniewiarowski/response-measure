import argparse


class Parser:
    def __init__(self):
        parser: argparse.ArgumentParser = argparse.ArgumentParser(
            prog="response-measure",
            description="Measure server response time after request to provided URL.",
        )

        parser.add_argument("url", metavar="URL", type=str)
        parser.add_argument("--attempts", "-a", metavar="ATTEMPTS", type=int, default=1)

        args = parser.parse_args()

        self.__url = args.url
        self.__attempts = args.attempts

    @property
    def url(self) -> str:
        return self.__url

    @property
    def attempts(self) -> int:
        return self.__attempts
