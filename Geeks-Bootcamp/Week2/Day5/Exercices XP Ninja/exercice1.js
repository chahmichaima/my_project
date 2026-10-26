const person1 = {
    fullName: "John Smith",
    mass: 78, // بالـ kg
    height: 1.75, // بالـ meters
    calcBMI: function() {
        return this.mass / (this.height * this.height);
    }
};

const person2 = {
    fullName: "Sarah Miller",
    mass: 65,
    height: 1.68,
    calcBMI: function() {
        return this.mass / (this.height * this.height);
    }
};
function compareBMI(p1, p2) {
    const bmi1 = p1.calcBMI();
    const bmi2 = p2.calcBMI();
    if (bmi1 > bmi2) {
        console.log(${p1.fullName} has the largest BMI (${bmi1.toFixed(2)}));
    } else if (bmi2 > bmi1) {
        console.log(${p2.fullName} has the largest BMI (${bmi2.toFixed(2)}));
    } else {
        console.log("Both have the same BMI.");
    }
}
compareBMI(person1, person2);