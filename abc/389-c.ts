
import { readFileSync } from "node:fs";
const inputLines: string[] = readFileSync("/dev/stdin","utf8").trim().split("\n");;
const Q = Number(inputLines[0]);
const snakes: bigint[] = [0n];
let counter: number = 0;
let number_of_snakes = 0;
for (let _ = 0; _ < Q; _++){
    const query:string[] = inputLines[_+1].split(" ");
    const tp: number = Number(query[0]);
    if (tp == 1){
        const l: bigint = BigInt(query[1]);
        snakes.push(l + snakes[number_of_snakes]);
        number_of_snakes += 1;
    }else if(tp == 2){
        counter += 1;
    }else{
        const k: number = Number(query[1]);
        const ans:bigint = snakes[k + counter-1] - snakes[counter];
        console.log(ans.toString());
    }
}