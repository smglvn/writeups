# Company leak
## Misc
> Someone hacked and leaked some very important data from an evil company. Find their dirty secrets and expose them!
>
> [Data](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Company_leak/leaked.zip)

- We have a zip-archive. Let's unzip it, there are 2 files - [README.md](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Company_leak/README.md) and [super_secret.zip](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Company_leak/super_secret.zip) inside.
- We cannot unzip the second zip-archive because of the password, but when we try to do it, we understand that the [super_secret.zip](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Company_leak/super_secret.zip) contains the same README.md as the first one.
- This gives us the ability to use the plaintext attack, which means you have to know part of the encrypted data in order to break the cipher.
- Let's use [pkcrack](https://github.com/keyunluo/pkcrack).
- Write a command:
```
pkcrack -C super_secret.zip -c README.md -P crack.zip -p README.md -d decrypted_file.zip -a
```
- After execution, the program write the result to a [new zip-archive](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Company_leak/decrypted_file.zip). Unzip it and get a new file [top_secret.txt](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Company_leak/top_secret.txt) with a flag inside.

Flag=dctf{wew_lad_y0u_aCtually_d1d_it}

There are several nuances to consider when using this solution method. 

The instructions say that the archive with the plaintext should be compressed by the same compression method as the encrypted one (zip has several of them), 
but there is no information that they should be created on the same platform: if the encrypted one was created on a unix system, then the archive with the plaintext should be created on a unix system too. 
But the original [leaked.zip](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Company_leak/leaked.zip) was created on Windows and the [super_secret.zip](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Company_leak/super_secret.zip) inside it was created on Unix, which caused a lot of problems when solving.

