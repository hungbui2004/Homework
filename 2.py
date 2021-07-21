def typeOfTriangle(x,y,z):
    if (x <= 0 or y <= 0 or z <= 0 or x > 10**9 or y > 10**9 or z > 10**9):
        return "Không thể xác định"
    arr = [x,y,z]
    newArr = sorted(arr, reverse=False)
    if (newArr[0] == newArr[1] == newArr[2]):
        return "Tam giác đều"
    elif (newArr[0] == newArr[1] or newArr[1] == newArr[2]):
        return "Tam giác cân"
    elif (newArr[0] + newArr[1] > newArr[2]):
        return "Tam giác thường"
    else:
        return "Không tồn tại tam giác"

print(typeOfTriangle(4,4,4))

