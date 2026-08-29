import { readFileSync } from "fs";
const input: string = readFileSync("/dev/stdin", "utf8");
const a: number = parseInt(input[0]);
const b: number = parseInt(input[2]);
const ans: number = a*b;
console.log(ans);