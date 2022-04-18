def hash_table_for(header):     ## this function will return the hash_table for the header
    header_count = 0
    hash_table = {}
    for length in range(1,8):       ## this loop is used to maintain all lengths in order for the sequence of keys
        flag = 0
        for integer_key in range((2**length)-1):     ##this loop is used to maintain the sequence from 0 to 2**n -1 for every length 
            if header_count == len(header):
                flag = 1
                break
            binary_key = bin(integer_key)[2:]
            binary_key = "0" * (length - len(binary_key)) + binary_key
            hash_table[binary_key] = header[header_count]           ## all characters are mappped to the keys in a specified sequence
            header_count += 1
        if flag == 1:
            break
    return hash_table  


def decode(binary_pattern,hash_table):   ## this is the important function where actual decoding of message is done, this function will return the decoded message
    decoded_message = ""
    i = 0
    while i < len(binary_pattern):
        length_of_key = int(binary_pattern[i:i+3],2)      
        i += 3
        if length_of_key == 0:
            return decoded_message          ## when ever the length becomes 0 we return the decoded message here, without further process
        else:
            while binary_pattern[i : (i + length_of_key)] != ("1" * length_of_key):     ## this loop is maintained until no of ones in key is equal to the length
                decoded_message += hash_table[binary_pattern[i : (i + length_of_key)]]   ## from the hash table we take the origina l message charecter for the actualy key int in the binary pattern
                i += length_of_key
                if i >= len(binary_pattern):
                    return decoded_message   ## when ever the iterable value become greater than or equal to length of given binary pattern it return decoded message
            i += length_of_key
    return decoded_message


def main(path):                         ## this is main function where all segments are divided sequencially and processes each segment individually
    input_file = open(path)
    lines = input_file.read().split("\n")[::-1] # all lines are read from input file and we are making a list in reverse order of that lines , to make our work easier
    header = lines.pop()
    output_lines = []    
    while lines:                 ## this loop exits until all segments are finished
        #print(head)
        hashtable = hash_table_for(header)     ## we create a hashtable from header by calling hash_table_for(header) function
        #print(hash_table)
        binary_pattern = ""
        while lines:        ## this loop exists until all binary lines are concatinated into a single string for a segment
            line = lines.pop()
            try:
                int(line,2)
                binary_pattern += line
            except:
                break
        header = line
        output_of_segment = decode(binary_pattern,hashtable)      ## finally we call decode function to get actual mesaage from binary pattern using hash_tabel
        if output_of_segment != "":
            output_lines.append(output_of_segment)      ## when ever the message is not empty the output for that segment will be printed in the console
    for line in output_lines:
        print(line)
main(input("enter file name:"))     ## here we call the mainfunction to get the output


