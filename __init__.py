from mycroft import MycroftSkill, intent_file_handler


class Alimentos(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('alimentos.intent')
    def handle_alimentos(self, message):
        self.speak_dialog('alimentos')


def create_skill():
    return Alimentos()

