import time


class Notification:
    def __init__(self, message):
        self.message = message
        self.notification()

    def notification(self):
        print("Notification yuborishin boshladi...")
        for x in range(6):
            time.sleep(2)
            print(f" {self.message}")

    def close_notification(self):
        print("Closing notification")

    def __del__(self):
        self.close_notification()
        print(f"message:  {self.message} o'chirilmoqda")


objects = Notification("salom")

del objects
