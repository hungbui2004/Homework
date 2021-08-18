let mang = [5,8,9,4,4,6,51,2,23,88,42,1,5,4]
function oddEven(arr) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] % 2 !== 0) {
            return "No"
        }
    }
    return "Yes"
}
function chiaHetChoNam(num) {
    if (num % 5 == 0) {
        console.log(num)
    }
}
mang.forEach(chiaHetChoNam)