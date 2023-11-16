from datetime import datetime
# 计算距离下一个8点的延迟时间
def calculate_delay_time(_hour=8, _minute=8, _second=0, _microsecond=0):
    now = datetime.now()
    next_eight = now.replace(hour=_hour, minute=_minute, second=_second, microsecond=_microsecond)
    if now > next_eight:
        next_eight = next_eight.replace(day=next_eight.day + 1)
    delay = (next_eight - now).total_seconds()
    return delay




