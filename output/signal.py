from rich.console import Console


class Signal:
    def __init__(self) -> None:
        self.console = Console()

    def error(self, message: str) -> None:
        self.console.print(message, style="bold red")

    def success(self, message: str) -> None:
        self.console.print(message, style="bold green")

    def warn(self, message: str) -> None:
        self.console.print(message, style="bold yellow")
