let number;
do {
    number = prompt("Please enter a number:");
    number = Number(number);
} while (isNaN(number) || number < 10);