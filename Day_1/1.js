const readline = require("readline");

// Here we learn how to add or delete new elements in the array of data structure and algorithms with javaScript in the Hindi language. there we cover all topics and operations of DSA in javascript.

const ARRAY = [1, 2, 3, 4, 5, 6, 7];

function sol() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  console.log(
    "Enter the Position you want to remove from this ARRAY --> [" + ARRAY + "]"
  );

  rl.question("Enter your input: ", (input) => {
    console.log(`You entered: ${input}`);

    rl.close();
  });
}
sol();
