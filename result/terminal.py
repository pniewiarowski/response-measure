from abc import ABC

from communication.signal import signal_success, signal_error
from result.result import Result


class TerminalResult(Result, ABC):
    def out(self) -> None:
        if self._results.finish_attempts <= 0:
            signal_error("No finish attempts.")
            return

        signal_success(f"\n")
        signal_success(f"Requested URI:\t\t {self._results.url}")
        signal_success(f"Number of attempts:\t {self._results.finish_attempts}")
        signal_success(f"Average response time:\t {self._results.get_average_response_time()}s")
