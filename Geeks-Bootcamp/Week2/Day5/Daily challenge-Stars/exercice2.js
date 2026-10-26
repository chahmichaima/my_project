function calculateAverage(gradesList) {
    let sum = 0;
    for (let i = 0; i < gradesList.length; i++) {
        sum += gradesList[i];
    }
    return sum / gradesList.length;
}
function findAvg(gradesList) {
    let average = calculateAverage(gradesList);
    console.log(The average is: ${average.toFixed(2)});

    if (average >= 65) {
        console.log("Congratulations! You passed.");
    } else {
        console.log("You failed and must repeat the course.");
    }

    return average;
}
findAvg([70, 85, 90, 60, 75]);