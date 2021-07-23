let numOfFactors = 0;

for (let i = 2; i <= 1000; i++) {
  numOfFactors = 0;
  for (let j = 1; j <= i; j++) {
    if (i % j === 0) {
      numOfFactors += 1;
    }
  }
  if (numOfFactors === 2) {
    console.log(i);
  }
}