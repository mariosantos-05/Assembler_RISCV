def read_file(path):
    with open(path, 'r') as f:
        return f.readlines()
    

''' 
Parser again and again. is not much but if i were to win a coin for each time i write a parser in a non related
parser course, i would have 2 coins. what is not much but is odd 

'''
def parse_line(line):
    line = line.split('#')[0]  # remove inline comments
    line = line.strip() # get rid of leading and trailing whitespace

    if not line or line.startswith('#'):  # get out of here stink comments. we assemblers do not care
        return None
    
    parts = line.replace(',',' ').split()  # parse the line into parts 
    
    
    return parts


# Formato R [ funct7 ][ rs2 ][ rs1 ][ funct3 ][ rd ][ opcode ]
def encode_add(rd, rs1, rs2):

    opcode = "0110011"
    funct3 = "000"
    funct7 = "0000000"

    rd_bin  = format(int(rd[1:]), '05b')  # 32 bits, 5 bits for the register number (x0-x31)
    rs1_bin = format(int(rs1[1:]), '05b')
    rs2_bin = format(int(rs2[1:]), '05b')

    binary = funct7 + rs2_bin + rs1_bin + funct3 + rd_bin + opcode
    return format(int(binary, 2), '08X')  # 8 dígitos hex


# mif = Memory Initialization File
# it must be in the format of an hexadecimal

def write_mif(hexadecimal_code, output_path='output.mif'):
    with open(output_path, 'w') as f:
        #MIF Header
        f.write("WIDTH=32;\n")
        f.write("DEPTH=256;\n")

        #Adress and data in hexadecimal

        f.write("ADDRESS_RADIX=HEX;\n")
        f.write("DATA_RADIX=HEX;\n")


        f.write("CONTENT BEGIN\n") #start of memory data 

        for i, code in enumerate(hexadecimal_code):
            f.write(f"{i:02X} : {code};\n") # write the address and the data in hexadecimal format

        f.write("END;\n") #end of memory data


def main():
    lines = read_file('input.asm')

    hexadecimal_code = []

    for line in lines:
        parsed = parse_line(line)
        if parsed is None:
            continue 

        if parsed[0] == "add":
            if len(parsed) != 4:
                print(f"Erro de formato: {parsed}")
                continue

            _, rd, rs1, rs2 = parsed
            hexadecimal_code.append(encode_add(rd, rs1, rs2)) 

        else:
            print(f"Invalid instruction: {parsed[0]}")

    write_mif(hexadecimal_code)
    print("Output written to output.mif")


if __name__ == "__main__":
    main()