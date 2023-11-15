from datetime import datetime
# 计算距离下一个8点的延迟时间
def calculate_delay_time():
    now = datetime.now()
    next_eight = now.replace(hour=15, minute=21, second=0, microsecond=0)
    if now > next_eight:
        next_eight = next_eight.replace(day=next_eight.day + 1)
    delay = (next_eight - now).total_seconds()
    return delay




