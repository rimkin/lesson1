import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, p_object):
        x = super(LoggableList, self).append(p_object)
        return self.log(p_object)



a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)
