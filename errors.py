class ProfessorNotExist(Exception):
    def init(self, message):
        self.message = message

class NoActivityRegistered(Exception):
    def init(self, message):
        self.message = message