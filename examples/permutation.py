import sys

class Permutation:    
    permutation(stringgg):
        permutation2(stringgg, "")

    permutation2(stringgg,prefix):
        if (stringgg.Length == 0):
            print(prefix)
        else:
            for i in range(0,stringgg.le):
                rem = stringgg.Substring(0, i) + stringgg.Substring(i+1)
                permutation2(rem,prefix+stringgg.IndexOf(stringgg.Substring(i)))

    permutation("hello")
