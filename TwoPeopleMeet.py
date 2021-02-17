def everMeet(x1, x2, v1, v2):
    if (x1 < x2 and v1 <= v2):
        return False
    if (x1 > x2 and v1 >= v2):
        return False

    if (x1 < x2):

        x1, x2 = x2, x1
        v1, v2 = v2, v1

    while (x1 >= x2):

        if (x1 == x2):
            return True

        x1 = x1 + v1
        x2 = x2 + v2

    return False


if __name__ == "__main__":
    x1, v1, x2, v2 = 6, 6, 4, 8
    if (everMeet(x1, x2, v1, v2)):
        print("Will Meet")
    else:
        print("Never Meet")
