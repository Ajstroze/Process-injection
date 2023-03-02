import pymem
import subprocess
import pwn

# XOR decoder
# Returns:
# -output: a list of XORed characters in 
# ASCII representation
def xorDecrypt(key, file):
    output = []
    for byte in file:
        outbyte = pwn.xor(byte, key)
        output.append(outbyte.decode('latin-1'))
    return output

# Create a python-injected Pymem instance 
# Parameter:
# -process: the name of the process in memory
# Returns:
# -mem: A Pymem representation of the process in memory
    mem = pymem.Pymem(process)
    mem.inject_python_interpreter()
    return mem

# Grabbing bytes from the executable memory area
# Parameters: 
# -mem: The Pymem instance that's working with the process target
# -address_list: A list of address offsets in HEX
# Returns:
# - A list of values that reside within the proximity of
# the offset locations
def getBytes(mem,address_list):
    #address_list = [0x401577,0x40157b,0x40157f,0x401583,0x401587,0x40158b,0x40158f]
    arr = []
    for item in address_list:
        arr.append(mem.read_bytes(int(item) + 3, 1).decode('latin-1'))
    return arr

def bruteForce(key,arr):
    output = [arr]
    for i in range(1,key+1):
        output.append(xorDecrypt(i,arr))
    return output

def main(process,key,address_list):
    mem = processInjection(process)
    bytesArr = getBytes(mem,address_list)
    bruteArr = bruteForce(key,bytesArr)
    for i in range(0,key+1):
        print(i,''.join(bruteArr[i]))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description = 'Xor Brute force a particular location in memory of a program')
    parser.add_argument('-p','--process', type=str,required=True,help='The name of the process to inject into')
    parser.add_argument('-c','--count',type=int,required=True,help='What value to xor up to in decimal')
    parser.add_argument('-a','--address',type=str, help='The memory location of the bytes to Xor, input should be a single string where each hex offet is seperated by a comma', required=True)
    args = parser.parse_args()
    address_list= [int(item,16) for item in args.address.split(',')]
    main(args.process,args.count,address_list)

# for i in range(256):
#output = xorBruteforce(65, arr)
#print(output)
