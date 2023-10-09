from argparse import ArgumentParser, BooleanOptionalAction

from MessageGenerator import MessageGenerator
from utils.logger import get_logger, LogLevel

logger = get_logger()


def print_volleyball_team_fixture(team_name: str) -> None:
    message = MessageGenerator().generate_message(team_name)
    print(message)


if __name__ == "__main__":
    parser = ArgumentParser(
        prog=__file__,
        description="Print name volleyball time fixture for a team."
    )
    parser.add_argument('-v', '--verbose', action=BooleanOptionalAction, default=False)
    args = parser.parse_args()

    if args.verbose:
        logger.set_log_level(LogLevel.INFO)
    else:
        logger.set_log_level(LogLevel.ERROR)

    team_name = "TICKLE"
    print_volleyball_team_fixture(team_name)
