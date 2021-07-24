for (let i = 1; i <= 1000; i++) {
  let numOfFactors = 0;
  for (let j = 1; j <= i; j++) {
    if (i % j === 0) {
      numOfFactors += 1;
    }
  }
  if (numOfFactors === 2) {
    console.log(i);
  }
}
