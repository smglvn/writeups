# A Primed Hash Candidate
## CRYPTO
> After the rather embarrassing first attempt at securing our login, our student intern has drastically improved our security by adding more parameters. Good luck getting in now!
>
> [server.py](https://github.com/smglvn/writeups/blob/master/San%20Diego%20CTF%202021/A%20Primed%20Hash%20Candidate/server.py)
>
> Connect via
>
> `nc phc2.sdc.tf 1337`

1. We need to find the password by its hash.
2. Examining the hash function. It contains three secrets: two strings and one three-digit number.
3. Let's find a secret3. It belongs to the set of natural numbers [100, 1000).
4. Examining the secret2. We do not need to know a specific string, it will be enough to know its length.
Lucky for us if we send a wrong password to the server, it will return its hash. Let's take advantage of this by sending an empty password, and using simple operations we find out the length of the secret2.
5. It's not so simple with the secret1. We need to find out a specific line. We send the server any sufficiently long password, then we get its hash.
We begin to perform inverse transformations with the hash: sequentially divide by secret3, remove the length of secret2 from the end of the hash, and xor with the original password. We get the secret1.
6. Knowing all three secrets, we perform the same reverse operations with the given hash and get the password.
7. A solution [script](https://github.com/smglvn/writeups/blob/master/San%20Diego%20CTF%202021/A%20Primed%20Hash%20Candidate/solution.py)

Flag=sdctf{W0W_s3cur1ty_d1d_dRaStIcAlLy_1mpr0v3}