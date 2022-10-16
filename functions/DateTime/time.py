import datetime


def time_now():
    return datetime.datetime.now().strftime('%I:%M %p')

if __name__ == "__main__":
    print(time_now())