import urllib.request
from lab.database.database.DatabaseExt import DatabaseExt
from lab.database.gui.AwesomeEffects import AwesomeEffects
import re
import urllib2


class Exercise6:
    def __init__(self):
        self.path = "http://mmajchr.kis.p.lodz.pl/pwjs/"
        self.response = urllib.request.urlopen(self.path).read().decode('utf-8')
        self.files = ["imiona.txt", "nazwiska.txt"]
        self.awesome_effects = AwesomeEffects()
        self.db = DatabaseExt()

    @staticmethod
    def load_from_url(url, file_name):
        return urllib.request.urlopen(url + file_name).read().decode('utf-8').split('\n')

    def exercise6a(self):
        for file in self.files:
            self.awesome_effects.success("\n" + file)
            data = self.load_from_url(self.path, file)
            for i in sorted(data):
                self.awesome_effects.success(i)
            self.awesome_effects.success(data.__len__())

    def exercise6b(self, ):
        names = self.load_from_url(self.path, self.files[0])
        surnames = self.load_from_url(self.path, self.files[1])
        for i in range(0, surnames.__len__() - 1):
            self.awesome_effects.success(str(i + 1) + ", " + names[i % names.__len__()] + ", " + surnames[i])

    def exercise6c(self, ):
        names = self.load_from_url(self.path, self.files[0])
        surnames = self.load_from_url(self.path, self.files[1])
        for i in range(0, surnames.__len__() - 1):
            self.db.add_record(names[i % names.__len__()], surnames[i])

    def save_data_from_exercise_6c(self):
        self.exercise6c()
        self.db.save_ext()

    def upload_data_from_exercise_6c(self):
        names = self.load_from_url(self.path, self.files[0])
        surnames = self.load_from_url(self.path, self.files[1])
        output = ""
        for i in range(0, surnames.__len__() - 1):
            output += (str(i + 1) + ", " + names[i % names.__len__()] + ", " + surnames[i])
        self.send("208323", output)

    # todo: refactoring
    @staticmethod
    def send(file_name, file_text):
        data = ("Content-Disposition: form-data; name=\"file\"; filename=\"{0}\"\r\n"
                "Content-Type: text/plain\r\n"
                "{1}\r\n") \
            .format(file_name, file_text)
        return urllib2.urlopen(urllib2.Request("http://mmajchr.kis.p.lodz.pl/pwjs/odpowiedz.php", data,
                                               {'Content-Type': 'text/xml'})).read()

    def exercise6d(self):
        response = urllib.request.urlopen(self.path).read().decode('utf-8')
        self.awesome_effects.success(re.findall("(?:[^a-zA-Z]|^)komputer(?:[^a-zA-Z]|$)", response).__len__())
        self.awesome_effects.success(re.findall("komputer", response).__len__())

    def exercise6e(self):
        response = urllib.request.urlopen(self.path).read().decode('utf-8')
        self.awesome_effects.success(re.findall(r"((?:p[piouaue]+ )+p[piouaue])", response))
