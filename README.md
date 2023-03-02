# Process-injection
A simple tool to inject into a process, and decrypt bytes in memory using Xor. This is made to assist in malware analysis or CTF's
## How to use
-p The process you want to inject into,the full name of the process should be used and it can be gathered by checking your task manager or process explorer ex: "Xor.exe"

-c This is the amount of values in decimal that you want to brute for. ex: -c 70 , this will brute force for values 0-70

-a The offsets in memory of the bytes you want to extract in decrypt. The easiest way to determine the offsets of the values you are interested in is to use binary ninja, the format should be a string of hexadecimal values seperated by commas within the string. ex: "0x401577,0x40157b,0x40157f,0x401583,0x401587,0x40158b"

### Future development
This project has oppurtunities for future development. Additions for more methods of decryption as well as other memory management tactics as well as improved usability. Contributions are welcome!
#### Credits
This project was completed by: Vincent Xu, Andrew Strozewski, Morgan Douglas, Tyson Lindley, Paige Counihan





