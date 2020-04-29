from digital_assistant.voice_commands import \
    VoiceCommandEnglish, VoiceCommandItalian, VoiceCommandChinese, VoiceCommandSpanish
from api.routes.movement import MoveForward, MoveBackward, MoveLeftward, MoveRightward
from .music_player import play_music


class ActionManager(object):

    speaker = None
    command_list = None

    def __init__(self, speaker, language='en_EN'):
        self.speaker = speaker
        if language == 'en_EN':
            self.command_list = VoiceCommandEnglish
        if language == 'it_IT':
            self.command_list = VoiceCommandItalian
        if language == 'es_ES':
            self.command_list = VoiceCommandSpanish
        if language == 'zh-cn':
            self.command_list = VoiceCommandChinese

    def handle_decision(self, data):
        data = data.lower()

        if any(x in data for x in self.command_list.how_are_you_cmd):
            self.speaker.talk('I\'m fine, and you?')
            return

        if any(x in data for x in self.command_list.hello_cmd):
            self.speaker.talk("Hello")
            return

        if any(x in data for x in self.command_list.follow_cmd):
            self.speaker.talk("Let's go")
            MoveForward().get()
            return

        if any(x in data for x in self.command_list.turn_right_cmd):
            self.speaker.talk("Turn right")
            MoveRightward().get()
            return

        if any(x in data for x in self.command_list.turn_left_cmd):
            self.speaker.talk("Turn left")
            MoveLeftward().get()
            return

        if any(x in data for x in self.command_list.back_cmd):
            self.speaker.talk("Ok I'll go backward")
            MoveBackward().get()
            return

        if any(x in data for x in self.command_list.stop_cmd):
            self.speaker.talk("Of course!")
            return

        if any(x in data for x in self.command_list.play_cmd):
            play_music()
            return

        if any(x in data for x in self.command_list.fitness_data):
            self.speaker.talk("Your fitness data are:")
            return

