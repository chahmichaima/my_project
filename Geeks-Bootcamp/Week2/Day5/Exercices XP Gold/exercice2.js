let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentine"
};
let studentName = prompt("Please enter your name:").toLowerCase();
if (studentName in guestList) {
    console.log(Hi! I'm ${studentName}, and I'm from ${guestList[studentName]}.);
} else {
    console.log("Hi! I'm a guest.");
}