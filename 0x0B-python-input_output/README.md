# 0x0B. Python - Input/Output
----
!["Holberton Logo"](https://www.holbertonschool.com/holberton-logo-twitter-card.png)

## open() function


## Files incluided in this repository
Character |  Meaning
------------ | -------------
'r' | open for reading (default)
'w' |  open for writing, truncating the file first
'x' | open for exclusive creation, failing if the file already exists
'a' | open for writing, appending to the end of the file if it exists
'b' | binary mode
't' | text mode (default)
'+' | open a disk file for updating (reading and writing)
'U' | [universal newlines](https://docs.python.org/3.4/glossary.html#term-universal-newlines) mode (deprecated)



* r   read
* w   write
* a   appending
* r+  opens the file for both reading and writing
* b   binary mode

    f = open('file', 'w')

### Read content

    f.read()

*If the end of the file has been reached, f.read() will return an empty string ('')*

>If you want to read all the lines of a file in a list you can also use:
    list(f)
or 
    f.readlines().



    f.readline()
>reads a single line from the file;


    f.write(string)
>writes the contents of string to the file, returning the number of characters written.


    f.tell()
>returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.

To change the file object’s position, use:
    f.seek(offset, from_what)

When you’re done with a file, call:
    f.close()


### All the methods for objects

Method |  Meaning
------------ | -------------
writelines(sequence): |  It is a sequence of strings to the file usually a list of strings or any other iterable data type. It has no return value. 
tell(): |  It returns an integer that tells us the file object’s position from the beginning of the file in the form of bytes 
seek(offset, from_where): |  It is used to change the file object’s position. Offset indicates the number of bytes to be moved. from_where indicates from where the bytes are to be moved. 
flush(): |  Flush the internal buffer, like stdio‘s fflush(). It has no return value. close() automatically flushes the data but if you want to flush the data before closing the file then you can use this method. 
fileno(): | Returns the integer file descriptor that is used by the underlying implementation to request I/O operations from the operating system. 
isatty(): | Returns True if the file is connected to a tty(-like) device and False if not. 
next(): | It is used when a file is used as an iterator. The method is called repeatedly. This method returns the next input line or raises StopIteration at EOF when the file is open for reading( behaviour is undefined when opened for writing). 
truncate([size]):  | Truncate the file’s size. If the optional size argument is present, the file is truncated to (at most) that size. The size defaults to the current position. The current file position is not changed. Note that if a specified size exceeds the file’s current size, the result is platform-dependent: possibilities include that the file may remain unchanged, increase to the specified size as if zero-filled, or increase to the specified size with undefined new content. 
close(): | Used to close an open file. A closed file cannot be read or written any more. 


### Atributes

Atribute|  Meaning
------------ | -------------
closed: | returns a boolean indicating the current state of the file object. It returns true if the file is closed and false when the file is open.
encoding: | The encoding that this file uses. When Unicode strings are written to a file, they will be converted to byte strings using this encoding.
mode: | The I/O mode for the file. If the file was created using the open() built-in function, this will be the value of the mode parameter.
name: | If the file object was created using open(), the name of the file.
newlines: | A file object that has been opened in universal newline mode have this attribute which reflects the newline convention used in the file. The value for this attribute are “\r”, “\n”, “\r\n”, None or a tuple containing all the newline types seen.
softspace: | It is a boolean that indicates whether a space character needs to be printed before another value when using the print statement. 