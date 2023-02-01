class PasswordSender:
    address = ""
    username = ""

    def __init__(self, address, username):
        self.address = address
        self.username = username
        pass

    def send_password(self, password):
        # response = requests.post(self.address, data={'username': self.username, 'password': password})
        print("Отправка на {0}, имя {1}, пароль {2}".format(self.address, self.username, password))
        if password == "ntpupdate":
            return True
        else:
            return False
        # if response.status_code < 300 :
        #     return True
        # else:
        #     return False
