const people = ["Greg", "Mary", "Devon", "James"];

// Part I :
people.shift();
people[people.indexOf("James")] = "Jason";
people.push("Chaimae");
console.log(people.indexOf("Mary"));
const peopleCopy = people.slice(1, 3);
console.log(peopleCopy); // ["Devon", "Jason"]
console.log(people.indexOf("Foo")); 
const last = people[people.length - 1];
console.log(last);

// Part II - Loops
for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
}

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
    if (people[i] === "Devon") {
        break;
    }
}