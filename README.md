# 🚀 💾 LZ78 Compression Algorithm using Trie Data Structure 🌳 - Python Project 🐍

* Author: *Lauro César de Oliveira Teixeira (<lauro-oliveira@ufmg.br>, <0lilauro7@gmail.com>)*
* Course: *Algorithms II*
* Period: *2023/01*
* Creation Date: *2023/05/09*
* Undergraduation: *Computational Mathematics*

## 🌟 Introduction

In this report, we will discuss the implementation of the LZ78 algorithm using Trie trees as data structures. The LZ78 algorithm is a lossless data compression algorithm that was introduced by Abraham Lempel and Jacob Ziv in 1978. The algorithm works by finding repeated patterns in a stream of data and encoding those patterns using a dictionary. The dictionary is built incrementally as the data is processed, and each pattern is assigned a unique code. The compressed data is then represented using these codes, which are smaller than the original data.

Trie trees are an efficient data structure for implementing the LZ78 algorithm. A Trie tree is a tree-like data structure that is used to store strings. Each node in the tree represents a prefix of a string, and the edges leading from the node represent the characters that can be added to the prefix. The Trie tree is built incrementally as the strings are processed, and each string is assigned a unique code based on its position in the tree.

### 📚 References:
* [LZ77 & LZ78 - Wikipedia](https://en.wikipedia.org/wiki/LZ77_and_LZ78)
* [Trie - Wikipedia](https://en.wikipedia.org/wiki/Trie)
* [Tries: Data Structure for Efficient String Searching](https://www.toptal.com/java/the-trie-a-neglected-data-structure)

## 💿 Compression Output

The Writing output of a compression was made by using bitwise operation.

After processing the input stream and encoding the patterns using the Trie tree, the compressed data can be represented using the codes. Since the codes are typically smaller than the original data, they can be represented using fewer bits. One common way to represent the codes is to use a fixed number of bits for each code. For example, if we have 100 codes, we can use 7 bits to represent each code (since 2^7 = 128, which is greater than 100).

To write the compressed output to a file, we can use bitwise operations to pack the codes into bytes. For example, if we are using 7 bits to represent each code, we can pack 8 codes into a single byte by shifting the bits and using bitwise OR to combine them. 

So the final output of the file was writing on the following way: 
```
size_of_nodes|bitwise_index_representation|character_of_each_index
```

As the LZ78 algorithm require to write a list of 2-uples where each 2-uples contains 
the index of the father prefix and the character to be added to the father prefix. We
can write a final output by defininig `size_of_nodes` as the total number of elements required to be represent an text  on the encoded list. Then we could separate the list into 2 sublists, one with every index of the 2-uple and another with
each single char of the 2-uple, those values would be `bitwise_index_representation` and `character_of_each_index` respectively. Considering that the index representation was encoded using bitwise operation.

### 🔢 Writing numbers into non decimal basis
When encoding the patterns using the LZ78 algorithm, we assign each pattern a unique code. The codes are typically represented as integers (decimal representation), but they can also be represented in other bases, such as base 36. In base 36, the digits are the numbers 0-9 and the letters A-Z, so a single digit can represent any value between 0 and 35.

To convert an integer to base 36, we can repeatedly divide the integer by 36 and use the remainder as the least significant digit. We then divide the quotient by 36 and use the new remainder as the next digit, and so on, until the quotient is 0. The digits are written from right to left, so the most significant digit is the leftmost digit.

Using numbers in base 36 instead of base 10 (decimal) can increase the compression output text of the LZ78 algorithm because it reduces the number of bits required to represent each number. In base 10, each digit can be represented by 10 possible values (0 to 9), which means that to represent a number in base 10, we need to use 10 digits. However, in base 36, each digit can be represented by 36 possible values (0 to 9 and A to Z), which means that to represent a number in base 36, we only need to use 6 digits.

This reduction in the number of digits required to represent a number in base 36 means that we can represent the same number using fewer bits, which can result in a more compact representation of the data. This, in turn, can lead to better compression ratios when using the LZ78 algorithm.

It is important to note that the choice of base depends on the specific characteristics of the data being compressed and the compression algorithm being used. While using base 36 can be beneficial in some cases, it may not always be the best choice for every situation.

In our test cases the LZ78 compression ration is higher with using 36-basis to numerical representation. 
And also this is just a single parameter to be changed on the algorithm to use some other base.

## 💻 About the Code 

The [lz78.py](./lz78.py) file contains the entire code required for the compression and decompression of data using the LZ78 algorithm with Trie data structure. The file includes the implementation of the Node, Trie, and LZ78 classes, which are all crucial components of the algorithm.

The Node class represents a single node in the Trie data structure, which is used to store the informations of phrases encountered during compression. The Trie class represents the Trie data structure itself and provides the necessary methods for inserting new nodes and searching for existing nodes in the Trie. Also functions to turn a text into 
a list of 2-uplas of the encoded content as the LZ78 requires.

Finally, the LZ78 class is responsible for implementing the LZ78 algorithm using the Trie data structure. It provides the necessary methods for compressing and decompressing data using the algorithm.

All of the code in the [lz78.py](./lz78.py) file is well-documented, making it easy to understand and modify for specific use cases. If you have any questions or concerns regarding the code, please do not hesitate to reach out for assistance.

### 🔍 Code details

Dear reader,I would like to take a moment to clarify that some pieces of code may appear to be missing from this report. However, please note that this was not an oversight on my part. The code used in this project is thoroughly documented, which means that all important information about the code is already provided in the comments within the code itself.

I believe that well-documented code is not only important for the functionality and maintainability of a project but also for the ease of understanding for future readers. Therefore, I have taken great care to ensure that the code used in this project is properly documented.

If you have any questions or concerns regarding the code used in this project, please do not hesitate to reach out to me. I would be more than happy to provide any additional information or clarification that you may need.

Thank you for taking the time to read my report, and I hope you find it informative.


## ⌨️ CLI usage

The [main.py](./main.py) file is a command-line interface (CLI) file that allows users to compress and decompress files using the LZ78 algorithm with a compact Trie tree as the dictionary data structure. The file has been implemented in Python 3.6 and uses the NumPy library.

The CLI has the following syntax:

Compression
```sh
$ python main.py -c <input_file> [-o <output_file>]
```

Decompression
```sh
$ python main.py -x <input_file> [-o <output_file>]
```

The specification of the output file is optional. If it is not given, the output file name for compression will be the original file name with the `.z78` extension. In the case of decompression, the output file name will be the original file name with the current extension removed and replaced with the `.txt` extension. For example:

Compression
```sh
$ python main.py -c test.txt  
# output file: test.z78
```

Decompression
```sh
$ python main.py -c test.z78
# output file: test.txt
```

The [main.py](./main.py) file is responsible for handling command-line arguments, calling the necessary functions from the lz78.py file to compress or decompress the input file, and outputting the result to the specified output file or a default file name if none is given.

Examples of Call: 

```sh
python main.py -c ./data/mob_dick.txt -o ./output/mob_dick.lz78 # compression
python main.py -x ./output/mob_dick.lz78 -o ./output/mob_dick.txt # descompression
```

## 🌟 Examples

Let's use the algorithm to compress and decompress some text samples and check some statistics of the compression.

To test I prefered to use some real texts.  The Gutenberg Project is a volunteer effort to digitize and archive cultural works, including books, images, and music. It was founded in 1971 by Michael Hart and is the oldest digital library. The project offers over 60,000 free ebooks to download, including many classic works of literature.

The samples text files used in this project were obtained from the Gutenberg Project's website. These texts are famous literary works that have become cultural icons, and their inclusion in this project allows for a comparison of the effectiveness of the LZ78 algorithm with various types of literature.

Here are some brief descriptions of the sample texts used:

* **A Room with a View**: A novel by E.M. Forster about a young woman's journey of self-discovery in Edwardian England.
* **Alice's Adventures in Wonderland**: A classic children's book by Lewis Carroll about a girl's adventures in a fantastical world.
* **Dracula**: A gothic horror novel by Bram Stoker about a vampire who terrorizes London.
* **Moby Dick**: A novel by Herman Melville about a whaling voyage and the obsession of Captain Ahab to hunt down a white whale.
* **Pride and Prejudice**: A novel by Jane Austen about the relationships and social norms of Georgian England.
* **Romeo and Juliet**: A tragedy by William Shakespeare about two young lovers from feuding families in Renaissance-era Verona.
* **The Odyssey**: An epic poem by Homer about the journey of Odysseus home to Ithaca after the fall of Troy.
* **The Picture of Dorian Gray**: A novel by Oscar Wilde about a man who remains youthful while a portrait of him ages and reveals his true nature.
* **Twenty Years After**: A novel by Alexandre Dumas about the adventures of the Three Musketeers after the events of the first book.
* **Ulysses**: A modernist novel by James Joyce about the experiences of various characters in Dublin over the course of a single day.

Let's see some statistics of the compression:





| ID | Book | File | Original Size (Bytes) | Compressed Size (Bytes) | Difference Size (Bytes) | Compression Rate | Compression Time |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ---- |
| 1| A Room with a View | [Link](./data/a_room_with_a_view.txt) | 406490 | 309278 | 97212 | 23.91% |  111s |
| 2| Alice's Adventures in Wonderland | [Link](./data/alices_adventures_in_wonderland.txt) | 170517 | 127124 | 43393 | 25.45% |  19s | 
| 3| Dracula | [Link](./data/dracula.txt) | 865818 | 634442 | 231376 | 26.72% |  813s | 
| 4| Mob Dick | [Link](./data/mob_dick.txt) | 1253915 | 915582 | 338333 | 26.98% |  918s | 
| 5| Pride and Prejudice | [Link](./data/pride_and_prejudice.txt) | 757277 | 515389 | 241888 | 31.94% |  324s | 
| 6| Romeo and Juliet | [Link](./data/romeo_and_juliet.txt) | 163622 | 134995 | 28627 | 17.50% |  20s | 
| 7| The Odyssey | [Link](./data/the_odyssey.txt) | 705353 | 497050 | 208303 | 29.54% |  294s | 
| 8| The Picture of Dorian Gray | [Link](./data/the_picture_of_dorian_gray.txt) | 456686 | 341069 | 115617 | 25.32% |  145s | 
| 9| Twenty Years After | [Link](./data/twenty_years_after.txt) | 1438297 | 949082 | 489215 | 34.01% |  1160s | 
| 10| Ulysses | [Link](./data/ulysses.txt) | 1553116 | 1161135 | 391981 | 25.24% |  1879s |

A general compression rate average of **26.66%**. A very good result to a simple algorithm.

## ❗ Problems...

Using Trie as a data structure for the LZ78 algorithm can be beneficial for compression performance, as it can efficiently store and search for repeated patterns in the text and also is easy to implement. However, it may not be very fast for large input sizes due to the memory requirements and search complexity of the Trie data structure.

Tries are typically implemented using dynamic memory allocation, which means that they can require a lot of memory for storing the nodes and edges of the tree. For large input sizes, the memory requirements of a Trie can become prohibitively high, potentially causing performance issues due to memory swapping or other memory management overhead.

Additionally, the search complexity of Tries can be high for large input sizes, as searching for a pattern in a Trie can require traversing multiple levels of the tree. This can result in slower speed compression performance for larger input sizes, as the algorithm must search through a larger Trie structure to find repeated patterns.

Using lists or dictionaries instead of Trie as a data structure for the LZ78 algorithm can offer some performance benefits for large input sizes.

Dictionaries, on the other hand, can provide a good balance between memory efficiency and search performance. Dictionaries use hash tables to efficiently store and retrieve key-value pairs, making them well-suited for storing and searching for repeated patterns in the text. Since dictionaries use a hash function to locate the relevant entries, the search time is usually constant time, which can be faster than Trie or lists for certain input data characteristics.

In general, the choice of data structure for implementing the LZ78 algorithm will depend on the specific use case and the characteristics of the input data. While Trie may not always be the most efficient option for large input sizes, it can still offer good compression performance for certain types of input data. Lists and dictionaries can provide a simpler and more memory-efficient alternative for certain use cases, but may not always offer the best performance for all input data.

*But for study purpose the choice of Trie was made*... This explain the slower time to compress some large files with a large number of character into a single file content.

## 📚 Libraries

The libraries used over all project are: 


* **numpy**: NumPy is a Python library used for scientific computing. It provides support for large, multi-dimensional arrays and matrices, as well as a large library of mathematical functions to operate on these arrays. In the LZ78 algorithm implementation, NumPy is used to efficiently store and manipulate large arrays of integers that represent the compressed data.

* **typing**: The typing module provides support for type hints in Python code. Type hints are annotations that specify the expected data types of function arguments and return values. They can be used to improve code readability, catch type errors early, and enable better static type checking tools. In the LZ78 algorithm implementation, the typing module is used to specify the expected types of various arguments and return values.

* **argparse**: The argparse module is a Python library used for parsing command-line arguments. It provides a convenient way to define the expected command-line arguments for a Python script, as well as handling errors and generating help messages. In the LZ78 algorithm implementation, argparse is used to parse the command-line arguments for the compression and decompression scripts, including the input and output files, verbosity level, and other optional parameters.

All three of these libraries are commonly used in Python programming and are available for Python 3.6.

The **numpy** was used only to get access of it's function `numpy.base_repr` function provided by the NumPy library in Python that converts an integer to a string representation in a given base.

And **argparse** was defined as the CLI handle, to let easy to pass and format arguments of the main code compression algorithm.

## 🙏 Thanks

Thank you for using this LZ78 compression and decompression tool powered by Lauro César de Oliveira Teixeira. We hope this tool was useful for you and helped you to understand more about data compression algorithms and Trie data structures.

If you have any questions or feedback, feel free to contact us. We're always looking for ways to improve our work and provide better solutions for our users.

Thank you again, and have a great day!

* Lauro Teixeira (lauro-oliveira@ufmg.br)