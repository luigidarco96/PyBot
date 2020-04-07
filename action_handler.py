class ActionHandler(object):

    speaker = None

    def __init__(self, speaker):
        self.speaker = speaker

    def handle_decision(self, data):

        if 'hello' in data:
            self.speaker("Hello")

        if 'follow' and 'me' in data:
            self.speaker("Let's go")

        if 'turn' and 'right' in data:
            self.speaker("Turn right")

        if 'turn' and 'left' in data:
            self.speaker("Turn left")



