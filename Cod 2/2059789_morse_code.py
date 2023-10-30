# Coding Challenge 2
# Name: Prasiddha Regmi.
# Student No: 2059789

# A Morse code encoder/decoder

MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"), 
    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)

def print_intro():
    print("Welcome to Wolmorse\nThis program encodes and decodes Morse code.")


def get_input():
    c=''
    while (c !='d' or c !='e'):     #!= means not equal to
        c = input("Would you like to encode (e) or decode (d):")
        if c =='e':
            inp= input("What message would you like to encode:")
            return (c, str.upper(inp))  #str.upper makes upppercase
        elif c =='d':
            inp= input("What message would you like to decode:")
            return (c, str.upper(inp))  #str.upper makes upppercase
        
        else:
            print("Invalid Mode")   # if invalid chars found, print Invalid mode
            
# Function to encode the string
# From morse code  

def encode(message):
    encoded_message=''
    for char in message:
        if(char==' '):   #check for space
            encoded_message+="  "
        else:
            for var in MORSE_CODE:
                if var[1]==char :
                    encoded_message+=var[0]+" "
                    break    # end the infinite while loop
    return(encoded_message)
                
# Function to decode the string
# from morse to english
        
def decode(message):
    decoded_message=''
    words = message.split('   ')    #message.split makes seperate the different words by space('   ')
    for w in words:
        characters = w.split(' ')   #w.split makes seperate the different words by space(' ')

        for c in characters:
            for var in MORSE_CODE:
                if var[0]==c:
                    decoded_message+=var[1]
        decoded_message+=" "
    return(decoded_message)

# ---------- Challenge Functions (Optional) ----------


def process_lines(filename, mode):
    myfile = open(filename)
    last = myfile.read().splitlines()
    result= []
    myfile.close()
    for i in last:
        if mode=='e':
            result.append(encode(str.upper(i)))
        else:
            result.append(decode(i))    
    return(result)

def write_lines(lines):
    result = open('results.txt','w')
    result.write("\n".join(lines))
    result.close()
    print("Output written to results.txt")


def check_file_exists(filename):
    import os.path
    return(os.path.exists(filename))

def get_filename_input():
    c=''
    file=''
    while (c !='d' or c !='e'):
        c = input("Would you like to encode (e) or decode (d):")
        if c =='e':
            file= input("Would you like to read from a file (f) or the console (c)?")
            if file =='c':
                message = input("What message would you like to encode:")
                return (c, str.upper(message), None)
            elif file =='f':
                while True:
                    filename = input("Enter a filename:")
                    if check_file_exists(filename):
                        return (c, None, filename)
                    else:
                        print("Invalid Filename")
                                        
        elif c =='d':
            file= input("Would you like to read from a file (f) or the console (c)?")
            if file =='c':
                message = input("What message would you like to decode:")
                return (c, str.upper(message), None)
            elif file =='f':
                while True:
                    filename = input("Enter a filename:")
                    if check_file_exists(filename):
                        return (c, None, filename)
                    else:
                        print("Invalid Filename")
        
        else:
            print("Invalid Mode")
    


"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    • Prompt users to select a mode: encode (e) or decode (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encode/decode.
    • Encode/decode the message as appropriate and print the output.
    • Prompt the user whether they would like to encode/decode another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment specification.

Hints:
    • Use the tuple MORSE_CODE above to convert between plain text/Morse code
    • You can make use of str.split() to generate a list of Morse words and characters
      by using the spaces between words and characters as a separator.
    • You will also find str.join() useful for constructing a string from a list of strings.
    • You should use a loop to keep the programming running if the user says that would like to
      encode/decode another message after the first.
    • Your program should handle both uppercase and lowercase inputs. You can make use of str.upper()
      and str.lower() to convert a message to that case.
    • Check the assessment specification for code examples.
"""
def main():
    print_intro()
    while True:
        choice, message, file = get_filename_input()
        if(file== None):
            if choice=='e':
                print(encode(message))
            else :
                print(decode(message))
        elif(message==None):
                write_lines(process_lines(file,choice))
        cont = input("Would you like to encode/decode another message? (y/n):")
        if cont=='n':
            print("Thanks for using the program, goodbye!")
            break


# Program execution begins here
if __name__ == '__main__':
    main()
