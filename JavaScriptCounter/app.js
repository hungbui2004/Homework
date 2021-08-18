let x = 0
document.getElementById("btn").addEventListener("click", counter)
function counter() {
    x = x + 1
    document.getElementById("p1").innerText = x
}