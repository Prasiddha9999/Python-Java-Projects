# Coding Challenge 2
# Name:
# Student No:

# A Morse code encoder/decoder
import sys

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
    while (c !=('d' or 'D') or c !=('e' or 'E')):
        c = input("Would you like to encode (e) or decode (d):")
        if c ==('e'or 'E'):
            inp= input("What message would you like to encode:")
            for d in range (0,len(inp)):
               return (c, str.upper(inp))
        elif c ==('d' or 'D'):
            inp= input("What message would you like to decode:")
            return (c, str.upper(inp))
            
        
        else:
            print("Invalid Mode")
    

def encode(message):
    encoded_message=''
    for char in message:
        if(char==' '):
            encoded_message+="  "
        else:
            for var in MORSE_CODE:
                if var[1]==char :
                    encoded_message+=var[0]+" "
                    break
    return(encoded_message)
                
        


def decode(message):
    decoded_message=''
    words = message.split('   ')
    for w in words:
        characters = w.split(' ')
        for c in characters:
            for var in MORSE_CODE:
                if var[0]==c:
                    decoded_message+=var[1]
        decoded_message+=" "
    return(decoded_message)

# ---------- Challenge Functions (Optional) ----------


def process_lines(filename, mode):
    pass


def write_lines(lines):
    pass


def check_file_exists(filename):
    pass


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
    
    choice, message = get_input()
    if choice==('e','E'):
        print(encode(message))
    
    else :
        print(decode(message))
        

# Program execution begins here
print_intro()
if __name__ == '__main__':
    main()
r= input('Would you like to encode/decode another message? (y/n):')
while r not in ('y','Y','n','N'):
    r= input('Would you like to encode/decode another message? (y/n):')
while r in ('y','Y'):
    main()
    r= input('Would you like to encode/decode another message? (y/n):')
print ('Thanks for using the program, goodbye!')
