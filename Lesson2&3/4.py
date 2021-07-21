def divisibility(a,b):
    if (a < 0 or b < 0 or a > 10**9 or b > 10**9):
        return "Không thể xác định"
    return b - a%b

print(divisibility(10,6))