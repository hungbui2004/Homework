function namNhuan(nam) {
    if (nam % 4 === 0 || nam % 400 === 0) { 
        return " là năm nhuận"
    } else { 
        return " không là năm nhuận"
    }
}
var x = prompt("Nhập năm: ")
console.log(x + namNhuan(x))