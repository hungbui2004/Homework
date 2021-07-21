
def countDigits(num):
    if (num < 0 or num > 10**9):
        return "Không thể xác định"
    return len(str(num))