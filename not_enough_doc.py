# Author: Wyly Andrews
# File name: not_enough_doc.py
# File version: 2.0
# File created: November 12, 2019
# File last modified: November 12, 2019
# File earliest modified: November 12, 2019
# File idea conceived: November 12, 2019
# File line count: 68
# File character count: 4,846
# File Description: Prints "Hello, World!" to standard output

# We are going to contain most of our functioning code inside the following 'main' function.
# This way, if this file is to be added to later in any way, we can add other functions throughout this code
# or import just this function of the file in the future.
# We name the function 'main' here because 'main' is the common name for the primary part of a file
def main():
    # What is being done here is that we are trying to 'print' the words 'Hello' and 'World' to the screen,
    # with these words interspaced with a comma and a space. The words will also be followed by an 
    # exclamation mark to denote excitement about the message.

    # We are going to accomplish this task in two major steps: First, we are going to denote the full message
    # inside of a string variable.
    
    # Text Sequence Type — str
    # Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways:
    # Single quotes: 'allows embedded "double" quotes'
    # Double quotes: "allows embedded 'single' quotes".
    # Triple quoted: '''Three single quotes''', """Three double quotes"""
    # Triple quoted strings may span multiple lines - all associated whitespace will be included in the string literal.

    # We choose a string type instead of an integer type or a float type because a string type will allow us to save a human-readable
    # message simply and easily, that other types cannot provide as easily.
    
    # To do this, we first have do decide on a variable name. Since we are planning to send this 'message' to the output, 
    # we can choose to save this variable 'message' or 'output'. It doesn't matter which one we use, but here we're 
    # going to choose 'message'.
    
    # We then denote the string value stored inside the message variable by wrapping the value in double quotation marks.
    # This way, the Python interpreter can distinguish the message as a string type.
    
    # Here is the variable assignment. Notice that since we are using Python, we don't have to denote the variable message
    # as a string type, we can just set the variable to equal a string value. Note that this can cause problems later down
    # the line, since message can be re-set to a value that's not a string. Keep this in mind when working.
    message = "Hello World!"
    
    
    #print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
    # Print objects to the text stream file, separated by sep and followed by end. sep, end, file and flush, if present, must be given as keyword arguments.
    # All non-keyword arguments are converted to strings like str() does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; they can also be None, which means to use the default values. If no objects are given, print() will just write end.
    # The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Since printed arguments are converted to text strings, print() cannot be used with binary mode file objects. For these, use file.write(...) instead.
    # Whether output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is forcibly flushed.
    # Changed in version 3.3: Added the flush keyword argument.
    
    # Now, we print the message to standard output. I say standard output instead of regular output, because there
    # are other ways to save information in Python, such as writing to a file or other external programs.
    
    # You may think that we are printing the word "message" to the output. That is not true. Since there are
    # no quotation marks around the word, then we are using the variable message instead of the string "message".
    # Note that we saved "Hello World!" to message earlier, so we can access it here.
    
    # After this line has run, the user should be able to read "Hello World!" as output.
    print(message)

# Remember earlier that we contained all of our work in the function 'main'. We now have to call
# that function so our program will run. We call that function by typing 'main' followed by parenthesis.
# The parenthesis can be used to pass parameters into our function, but our function doesn't require any
# parameters, so we don't add anything between the parenthesis.
main()