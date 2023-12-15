from argparse import ArgumentParser, BooleanOptionalAction

from src.MessageGenerator import MessageGenerator
from src.utils.logger import get_logger, LogLevel, Logger

logger = get_logger()


def print_volleyball_team_fixture(team_name: str) -> None:
    message = MessageGenerator().generate_message(team_name)
    print(message)


def set_log_level(is_verbose: bool, logger: Logger) -> None:
    if is_verbose:
        logger.set_log_level(LogLevel.INFO)
    else:
        logger.set_log_level(LogLevel.ERROR)


TEAM_NAME = "TICKLE"

if __name__ == "__main__":
    parser = ArgumentParser(
        prog=__file__,
        description="Print name volleyball time fixture for a team."
    )
    parser.add_argument('-v', '--verbose', action=BooleanOptionalAction, default=False)
    args = parser.parse_args()

    set_log_level(args.verbose, logger)

    print_volleyball_team_fixture(TEAM_NAME)
