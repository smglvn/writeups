# A Prime Hash Candidate
## CRYPTO
> We hired a fresh MATH 187A student to create our login for us. After 6 months of backbreaking development, we're no longer storing passwords as plain text. Just try to break in!
>
> [Hash function](https://github.com/smglvn/writeups/blob/master/San%20Diego%20CTF%202021/A%20Prime%20Hash%20Candidate/server.py)
>
> Connect via
>
> `nc phc1.sdc.tf 1337`

1. We need to find the password by its hash.
2. Examining the hash function.
3. Let's look at the ASCII character table: characters that can be used in a password have a code from 32 to 126.
Any of the possible codes is greater than the multiplier of the hash function (31), so the code of the last character of the password equal to `hash % 31 + 31x`, where x belongs to the set {1, 2, 3, 4}, since `126 // 31 = 4`.
We find one of the possible codes of the last character of the password, after which we remove it from the hash: `(hash - the possible code of the last character) // 31`.
4. In a loop, we repeat these actions for each possible character in the password, memorizing intermediate results in the stack.
If at the next iteration of the loop the hash becomes equal to 0, we have found a suitable character string.
5. A solution [script](https://github.com/smglvn/writeups/blob/master/San%20Diego%20CTF%202021/A%20Prime%20Hash%20Candidate/solution.py)

Flag=sdctf{st1ll_3553nt14lly_pl@1n_txt}