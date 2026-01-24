const readline = require("readline");

// Here we learn how to add or delete new elements in the array of data structure and algorithms with javaScript in the Hindi language. there we cover all topics and operations of DSA in javascript.

const ARRAY = [0, 1, 2, 3, 4, 5, 6, 7];

function sol() {
  let userInput;
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  console.log(
    "Enter the Position you want to remove from this ARRAY --> [" + ARRAY + "]"
  );

  rl.question("Enter your input: ", (input) => {
    console.log(`You entered: ${input}`);
    userInput = parseInt(input); // Ensure input is converted to a number
    console.log("you want to remove".toUpperCase(), ARRAY[userInput]);

    for (let i = userInput; i < ARRAY.length - 1; i++) {
      ARRAY[i] = ARRAY[i + 1];
    }
    ARRAY.length = ARRAY.length - 1;
    console.log("Updated ARRAY: ", ARRAY);
    rl.close();
  });
}
sol();
