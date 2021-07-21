def typeOfTriangle(x,y,z):
    if (x and y and z > 0) or (x and y and z > 10**9):
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
    else:
        return "Không thể xác định"

print(typeOfTriangle(4,4,4))

