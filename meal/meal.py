def main():
    clock = input("What time is it? ")
    time4 = convert(clock)
    if time4 >= 7 and time4 <= 8:
        print("breakfast time")
    elif time4 >= 12 and time4 <= 13:
        print("lunch time")
    elif time4 >= 18 and time4 <= 19:
        print("dinner time")
    else:
        pass


def convert(time):
    time2 = time.split(":")
    time3 = float(time2[0]) + float(time2[1])/60
    return time3

if __name__ == "__main__":
    main()
