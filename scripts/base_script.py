from argparse import ArgumentParser, BooleanOptionalAction
from typing import Protocol

from src.utils.logger import get_logger, LogLevel


class Script(Protocol):
    description: str

    def run(self) -> None:
        pass


class BaseScript:
    def __init__(self) -> None:
        # Set Singleton logger
        self._logger = get_logger()
        self._parser = ArgumentParser(prog=__file__, description=self.description)
        self._setup_parser()
        self._args = self._parser.parse_args()
        self._set_log_level()

    def _setup_parser(self) -> None:
        self._parser.add_argument(
            "-v", "--verbose", action=BooleanOptionalAction, default=False
        )
        self._extend_parser()

    def _extend_parser(self) -> None:
        """Child class to override if required"""
        pass

    def _set_log_level(self):
        if self._args.verbose:
            self._logger.set_log_level(LogLevel.INFO)
        else:
            self._logger.set_log_level(LogLevel.ERROR)
