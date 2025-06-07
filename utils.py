import datetime


class Time_Tool:
    def __init__(self):
        self.reset()

    def reset(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
        self.point_time = None
        self.flowing_time = None
        self.is_running = False

    def start(self):
        self.start_time = datetime.datetime.now()
        self.point_time = self.start_time
        self.is_running = True

    def showing_time(self):
        while 1:
            if self.is_running:
                self.flowing_time = datetime.datetime.now() - self.point_time
                print(self.flowing_time)
            else:
                break

    def mark_time(self):
        if self.is_running:
            self.point_time = datetime.datetime.now()
            print(self.point_time)

    def stop_time(self):
        if self.is_running:
            self.end_time = datetime.datetime.now()
            self.is_running = False
        else:
            return False

Timer = Time_Tool()
Timer.start()
# Timer.showing_time()
for i in range(10000):
    if i % 100 == 0:
        Timer.mark_time()
Timer.stop_time()
