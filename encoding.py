def hashing(header):
   header_count = 0
   dic = {}
   for length in range(1,8):
       flag = 0
       for i in range((2**length)-1):
           if header_count == len(header):
               flag = 1
               break
           key = bin(i)[2:]
           key = "0" * (length-len(key)) + key
           dic[header[header_count]] = key
           header_count += 1
       if flag == 1:
           break
   return dic



if __name__ == "__main__":
    message = input()
    header = "".join(sorted(list(set(message))))
    hashtable = hashing(header)
    binary = ""
    length = 0
    ones = ""
    for char in message:
        key = hashtable[char]
        if length != len(key):
            binary += ones
            binary += "0" *(3-len(bin(len(key))[2:])) + bin(len(key))[2:]
        ones = "1" * len(key)
        length = len(key)
        binary += key
    binary += ones
    binary += "000"
print(header + "\n" + binary)

