from src.MessageGenerator import MessageGenerator


def handler(event, context) -> None:
    message = MessageGenerator().generate_message('toes')
    print(message)

    return message
