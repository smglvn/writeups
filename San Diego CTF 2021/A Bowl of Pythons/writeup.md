# A Bowl of Pythons
## REVENGE
> A bowl of spaghetti is nice. What about a bowl of pythons?
>
> [chal.py]() 

- We are given an obfuscated code. Let's figure it out.
- First of all, flag in the beginning - is not a flag((
- Let's decrypt all hex lines. 

It becomes clear that h is just a print function, and function d is called in case of an invalid flag.
- Consider a function e that checks the entered flag for correctness.

The first condition checks that the flag starts in the standard way.

The second condition checks that it ends in a standard way.

g is the encoded part of the flag inside the curly braces, which is xor in the third condition. 

Let's write the inverse transformation function `def get_flag()` and get the flag.
- A solution [script]()

Flag=sdctf{v3ry-t4sty-sph4g3tt1}