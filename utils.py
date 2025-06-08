import datetime
import time


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
while True:
    print("1——开始计时")
    print("2——打点计时")
    print("3——停止计时")
    tag = input("输入数字：")
    if tag == '1' and not Timer.is_running:
        Timer.start()
        time.sleep(10)

    if tag == '2' and Timer.is_running:
        if Timer.point_time is None:
            Timer.point_time = datetime.datetime.now()
            Timer.elapsed_time = Timer.point_time - Timer.start_time
        else:
            prior = Timer.point_time
            Timer.point_time = datetime.datetime.now()
            Timer.elapsed_time = Timer.point_time - prior

        print(Timer.elapsed_time)
        time.sleep(10)

    if tag == '3' and Timer.is_running:
        Timer.end_time = datetime.datetime.now()
        time0_all = Timer.end_time - Timer.start_time
        print(time0_all)
        break
