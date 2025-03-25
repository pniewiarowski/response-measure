import requests

from input.parser import Parser
from communication.signal import signal_success, signal_error, signal_warn
from response.collection import ResultCollection
from response.response import Response
from result.result import Result
from result.terminal import TerminalResult


def main() -> None:
    parser: Parser = Parser()
    collection: ResultCollection = ResultCollection(parser.url)
    result: Result = TerminalResult(collection)

    for i in range(parser.attempts):
        try:
            response = requests.get(parser.url)
            response_time = response.elapsed.total_seconds()
            response = Response(response_time)

            collection.append(response)
            signal_success(f"Hit to {parser.url}: {response_time}s")
        except requests.exceptions.RequestException as e:
            signal_error(f"Could not connect to {parser.url}: {e}")
            continue
        except KeyboardInterrupt:
            signal_warn("Closing connection...")
            break

    result.out()


if __name__ == "__main__":
    main()
