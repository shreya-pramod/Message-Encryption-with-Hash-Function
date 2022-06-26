# Message-Encryption-with-Hash-Function
 Implemented a non-trivial hash function that produces a 32-bit hash.

Designed and implemented my own, nontrivial hash function that produces a 32-bit hash.

Requirements for the design:

-Output has to be in binary format.
-Input of any size shall be accepted.
-Use multiple rounds of computations to process one block of input data.
-Add some randomization by incorporating constant values like in case of SHA2 and SHA3.

Command line argument: inputFile.txt (file containing the message text to be encrypted)
-The hash function designed has 3 rounds of computations for each message blocks and the randomization is incorporated by taking 3 constant random values for each round.
