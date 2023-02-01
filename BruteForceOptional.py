class BruteForceOptional:
    currentPassword = [0]
    characters = []
    length = 0

    def __get_string_password(self):
        result = ""
        for i in range(len(self.currentPassword)):
            result += self.characters[self.currentPassword[i]]
        return result

    def __increase_password(self, index):
        if self.currentPassword[index] == len(self.characters) - 1:
            if index == 0:
                return False
            else:
                self.currentPassword[index] = 0
                return self.__increase_password(index - 1)
        else:
            self.currentPassword[index] = self.currentPassword[index] + 1
            return True

    def get_password(self):
        result = self.__get_string_password()
        if not self.__increase_password(len(self.currentPassword) - 1):
            result = ""
        return result

    def __init__(self, characters, length):
        self.characters = list(set(list(characters)))
        self.currentPassword = [0] * length
        self.length = length
        pass
