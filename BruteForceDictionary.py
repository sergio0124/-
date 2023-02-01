

class BruteForceDictionary:

    filename = 'dictionary.txt'
    file = open(filename)
    currentPassword = file.readline()

    def get_password(self):
        result = self.currentPassword
        self.currentPassword = self.file.readline()
        return result.rstrip()

    def __init__(self):
        pass
