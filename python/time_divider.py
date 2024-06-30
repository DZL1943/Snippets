def time_divider(step=30):
    times = []
    for h in range(0, 24):
        for m in range(0, 60, step):
            t = f"{h:02}:{m:02}"
            times.append(t)
            print(t)
    return times

if __name__ == "__main__":
    time_divider()
    pass