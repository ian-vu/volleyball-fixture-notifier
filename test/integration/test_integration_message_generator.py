from src.message_generator import MessageGenerator


def test_message_generator_message():
    """Test message is not empty when generating a message from making a HTTP request"""
    message = MessageGenerator().generate_message(team_name="TICKLE")
    assert len(message) > 0
