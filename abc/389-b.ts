const input: string = readFileSync("/dev/stdin","utf8");
const X:bigint = BigInt(input);
let ans:bigint = 1n;
let cnt:bigint = 1n;
while (cnt < X){
    ans += 1n;
    cnt *= ans;
}
console.log(ans.toString());