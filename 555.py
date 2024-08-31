import time

def pomodoro_timer(work_duration=25, break_duration=5):
    while True:
        print(f"开始工作: {work_duration} 分钟")
        time.sleep(work_duration * 60)
        print("工作时间结束！休息一下吧！")
        time.sleep(break_duration * 60)
        print("休息时间结束，继续工作！")

# 调用函数开始番茄钟
pomodoro_timer()
