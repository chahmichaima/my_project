const family = {
    father: "Ahmed",
    mother: "Fatima",
    son: "Youssef",
    daughter: "Aicha"
};
for (let key in family) {
    console.log("Key:", key);
}
for (let key in family) {
    console.log("Value:", family[key]);
}