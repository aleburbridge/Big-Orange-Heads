import time


def create_suspense(suspense_amount):
    for x in range(1, suspense_amount):
        b = "Supsense" + "." * x
        print(b, end="\r")
        time.sleep(1)


def print_line_break():
    print("--------------------------------------------------------------------")
