from enum import Enum


class LogLevel(Enum):
    INFO = 1
    ERROR = 2


class Logger:
    def __init__(self, log_level: LogLevel = LogLevel.INFO) -> None:
        self._log_level = log_level

    def set_log_level(self, log_level: LogLevel) -> None:
        self._log_level = log_level

    def info(self, *args, **kwargs) -> None:
        if self._log_level.value <= LogLevel.INFO.value:
            print(*args, **kwargs)

    def error(self, *args, **kwargs) -> None:
        if self._log_level.value <= LogLevel.ERROR.value:
            print(*args, **kwargs)


_singleton_logger = None


def get_logger() -> Logger:
    global _singleton_logger
    if _singleton_logger:
        return _singleton_logger
    else:
        _singleton_logger = Logger()
        return _singleton_logger
