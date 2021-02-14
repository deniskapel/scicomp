## Hashing

### Exercise: this doesn't mean the file was transferred correctly; why not?

he pieces can get scrambled.

### Exercise: do the same for files with "cat" and "cat2" instead of "hi" and "hi2"

$ echo cat > testfile; echo cat2 > testfile2

$ md5sum testfile testfile2
54b8617eca0e54c7d3c8e6732c6b687a *testfile
4307ab44204de40235bad8c66cce0ae9 *testfile2

$ sha1sum testfile testfile2
8f6abfbac8c81b55f9005f7ec09e32d29e40eb40 *testfile
f476b8741936d51309437ffc5c87081c7b24ffb1 *testfile2

$ sha512sum testfile testfile2 # sha2, hash size is 512bit
644c7b649d31fc3c432534fb80d71a3a5e2b3eb65e737eb15c6e6af96e40c8ee3dcb55fd172e263783e62f8d94f5c99e12a016d581b860700640e45c9c1b87b3 *testfile
84c308d32247eb3b590ff27b47d5018551dd6ad3e696b6d61b1e70fed7570522812a2c3353e93db38728f4a10de5156996b144d2b150f1ffe92ba7a301b5bfe2 *testfile2

$ b2sum testfile testfile2 # blake2
0247169dd9d258599e4a4327067f74f3dbd7db0e6d623954212738e62c233b410141a1eab4130073b99a8959e3d52f70da7402ae8d94ca6333126ec3b4e0bca7 *testfile
48d92c152ff4c58a948d75f7aaba6ccaf00f8f9beb78e3399fe0f325e758af657c07eb2d83a753f3fe16074b149f46390abce8673c7477f75aae99427c9defa7 *testfile2


## Symmetric cryptography

### Exercise: implement the Caesar cipher in python, which advances each letter of 'M' by 'SEC = n': enc(1, "a") = "b", etc.

see [caesar.py](https://github.com/deniskapel/scicomp/blob/main/Practical_2/caesar.py)
