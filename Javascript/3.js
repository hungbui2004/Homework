function average(phys,chem,bio,math,comp) {
    var diemTB = (phys + chem + bio + math + comp) * 10 / 5
    if (diemTB >= 90) {
        return "Grade A"
    } else if (diemTB >= 80) {
        return "Grade B"
    } else if (diemTB >= 70) {
        return "Grade C"
    } else if (diemTB >= 60) {
        return "Grade D"
    } else if (diemTB >= 40) {
        return "Grade E"
    } else {
        return "Grade F"
    }
}