def is_leap(year) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


if __name__ == "__main__":
    print(is_leap(2017))
    print(is_leap(1900))
    print(is_leap(2000))

