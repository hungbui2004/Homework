let sendButton = document.getElementById("sendButton")
let taskList = document.getElementById("taskList")

sendButton.addEventListener("click",addTask)

function addTask() {
    if (document.getElementById("inputBox").value !== "") {
        let li = document.createElement("li")
        li.append(document.getElementById("inputBox").value)
        taskList.append(li)
    } else {
        return
    }
}