from scripts.base_script import BaseScript
from src.message_generator import MessageGenerator

TEAM_NAME = "TICKLE"


class PrintVolleyballTeamFixture(BaseScript):
    description = "Print name volleyball time fixture for a team."

    def run(self):
        message = MessageGenerator().generate_message(TEAM_NAME)
        print(message)


if __name__ == "__main__":
    PrintVolleyballTeamFixture().run()
