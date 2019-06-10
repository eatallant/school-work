Implement the following functions:

1.	int binary_to_decimal_signed(string b);
// precondition: b is a string that consists of only 0s and 1s
// postcondition: the decimal integer that is represented by b


2.	string decimal_to_binary_signed(int n);
// precondition: n is an integer
// postcondition: n’s binary representation is returned as a string of 0s and 1s


3.	string add_binaries_signed(string b1, string b2);
// precondition: b1 and b2 are strings that consists of 0s and 1s, i.e. b1 and b2 are binary 
//                          two’s complement representations of two integers
// postcondition: the sum of b1 and b2 is returned. For instance, if b1 = “11”, b2 = “01”, 
//                          then the return value is “100” 


4.	string signed_extension(string b);
             // precondition: s is a string that consists of only 0s and 1s that is at most 16 bits
// postcondition: a 16 bit string has been returned as signed extension of s. For instane, 
// if s = "0101" then return value will be "00000000000000000101" total 12 
            //  0s are added in front of s


5.	string twos_complement(string s);
            // precondition: s is a string that consists of only 0s and 1s
// postcondition: two's complement of s is returned as an 16 bits binary integer. For 
//                       instance, if s = "1101", then return value will be "1111111111111101"
                     
