# Alternative Arithmetic  (Intermediate Flag)
## MISC
> Please submit the final flag of this challenge (after correctly answering the 5 questions)
>
> Connect via
>
> `nc java.sdc.tf 1337`

There is a Java quiz with three questions

- Find a nonzero `long x` such that `x == -x`, enter numbers only, no semicolons

The answer lies in Long.MAX_VALUE (9,223,372,036,854,775,807) and Long.MIN_VALUE (-9,223,372,036,854,775,808) value in Java.

If we attempt to assign a value of 9,223,372,036,854,775,808 (Long.MAX_VALUE + 1), it will be -9,223,372,036,854,775,808 (= Long.MIN_VALUE). 
It happens due to overflow.

9223372036854775808 is not in a valid format, so, the answer is -9223372036854775808.

- Find 2 different `long` variables `x` and `y`, differing by at most 10, such that `Long.hashCode(x) == Long.hashCode(y)`

The Long.hashCode implementation looks like [this](https://docs.oracle.com/javase/7/docs/api/java/lang/Long.html#hashCode%28%29):
```
public int hashCode()
Returns a hash code for this Long. The result is the exclusive OR of the two halves of the primitive long value held by this Long object. That is, the hashcode is the value of the expression:
    (int)(this.longValue()^(this.longValue()>>>32))
```
Obviously, any number and its bitwise negation will give the same hashes. 

Therefore, we need to look for a pair of negative number + positive number, while the difference between the numbers should be no more than 10.

So, we are looking for numbers close to 0.

A suitable pair is x = 0, y = -1

- Enter a `float` value `f` that makes the following function return true:
```
boolean isLucky(float magic) {
    int iter = 0;
    for (float start = magic; start < (magic + 256); start++) {
        if ((iter++) > 2048) {
            return true;
        }
    }
    return false;
}
```
For the loop to return true, it needs to be executed at least 2049 times, but the loop contains only 256 iterations.

It's about rounding.

We need to choose a sufficiently large starting number so that it does not increase during loop iterations with increment.

A good number is 3.35e + 7.

Flag= sdctf{JAVA_Ar1thm3tIc_15_WEirD}