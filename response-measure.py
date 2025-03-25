import argparse
import requests

from out.signal import Signal
from response.collection import ResponseCollection
from response.result import ResponseResult


def main() -> None:
    signal: Signal = Signal()
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="response-measure",
        description="Measure server response time after request to provided URL.",
    )

    parser.add_argument("url", metavar="URL", type=str)
    parser.add_argument("--attempts", "-a", metavar="ATTEMPTS", type=int, default=1)
    args = parser.parse_args()

    url: str = args.url
    attempts: int = args.attempts

    collection: ResponseCollection = ResponseCollection()
    finish_attempts = 0
    for i in range(attempts):
        try:
            response = requests.get(url)
            result = ResponseResult(
                response_time=response.elapsed.total_seconds(),
                requested_url=url,
            )

            collection.append(result)
            signal.success(f"Hit to {url}: {result.response_time}s")
            finish_attempts += 1
        except requests.exceptions.RequestException as e:
            signal.error(f"Could not connect to {url}: {e}")
            continue
        except KeyboardInterrupt:
            signal.warn("Closing connection...")
            break

    signal.success(f"\n")
    signal.success(f"Requested URI:\t\t {url}")
    signal.success(f"Number of attempts:\t {finish_attempts}")
    signal.success(f"Average response time:\t {collection.get_average_response_time()}s")


if __name__ == "__main__":
    main()
