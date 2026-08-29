import { readFileSync } from "node:fs";
const A: string[] = readFileSync("/dev/stdin","utf8").split(" ");
let cards: number[] = [];
for (let i = 0; i < 13; i ++ ){
    cards.push(0);
}
for (let i = 0; i < 7; i ++ ){
    cards[Number(A[i])-1]+=1;
}
cards.sort((a, b) => b - a);
//console.log(cards[0]);
//console.log(cards[1]);
if (cards[0] >= 3 && cards[1] >=2){
    console.log("Yes");
}else{
    console.log("No");
}