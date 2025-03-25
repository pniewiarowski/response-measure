import requests

from input.parser import Parser
from output.signal import Signal
from response.collection import ResponseCollection
from response.result import ResponseResult


def main() -> None:
    signal: Signal = Signal()
    parser: Parser = Parser()
    collection: ResponseCollection = ResponseCollection()

    finish_attempts = 0
    for i in range(parser.attempts):
        try:
            response = requests.get(parser.url)
            total_seconds = response.elapsed.total_seconds()

            result = ResponseResult(total_seconds, parser.url)

            collection.append(result)
            signal.success(f"Hit to {parser.url}: {result.response_time}s")
            finish_attempts += 1
        except requests.exceptions.RequestException as e:
            signal.error(f"Could not connect to {parser.url}: {e}")
            continue
        except KeyboardInterrupt:
            signal.warn("Closing connection...")
            break

    signal.success(f"\n")
    signal.success(f"Requested URI:\t\t {parser.url}")
    signal.success(f"Number of attempts:\t {finish_attempts}")
    signal.success(f"Average response time:\t {collection.get_average_response_time()}s")


if __name__ == "__main__":
    main()
