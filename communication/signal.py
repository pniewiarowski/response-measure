from rich.console import Console


def signal_error(message: str) -> None:
    console = Console()
    console.print(message, style="bold red")


def signal_success(message: str) -> None:
    console = Console()
    console.print(message, style="bold green")


def signal_warn(message: str) -> None:
    console = Console()
    console.print(message, style="bold yellow")


def signal_out(message: str) -> None:
    console = Console()
    console.print(message, style="bold cyan")
