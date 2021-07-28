def isSpecialNumber(num):
    uoc = []
    so_uoc_chan = 0
    so_uoc_le = 0
    if (num < 1 or num > 10**9):
        return "Không thể xác định"
    for i in range(1, num+1, 1):
        if (num % i == 0):
            uoc.append(i)
    for j in range(0,len(uoc),1):
        if (uoc[j] % 2 == 0):
            so_uoc_chan += 1
        else:
            so_uoc_le += 1
    if (so_uoc_chan == so_uoc_le):
        return True
    else:
        return False

print(isSpecialNumber(10))
