"""lz78 Module Code

This current module is the module that contains the LZ78 class
and it's components which are responsible to compress and decompress files.
"""

from typing import List
from typing import Union
from typing import Tuple
import numpy as np

__all__ = ['Node', 'Trie', 'LZ78']

class Node:
    """
    Node

    This is a class is the Node class, a piece of the Trie Tree component used to reestructure the text
    in order to compress it.

    Attributes
    ----------

    char: str
        The char string that this node represents.

    index: int
        It is the unique identification of the node in the tree.

    father_index: int
        It contains the id of the father node that is prefix of the current char string.

    Methods
    -------

    is_subscription_transaction( ) -> bool
        It returns if this object is or not a subscription transaction

    is_cancelled_transaction( ) -> bool
        It returns if this transaction was cancelled or not.

    get_warrenty_end_date( ) -> datetime
        It returns the default date where the warrenty is valid

    append_child( node: Node ) -> None
        This method append a new node to the list of child nodes of the current node.

    list_children( ) -> List[Node]
        Using this function, it will return a list of all nodes that is child of this current one.

    has_any_child( ) -> bool
        This will say if the current node has at least one child or not.

    get_shortcut( ) -> Tuple[Union[int,str]]
        Using this method it will return for each node a 2-Tuple containing at the first
        position the index of the father node and at the second position, will be the value of the
        current node string.

    Usage Example
    -------------

    node = Node('s', 10, 8)

    """
    def __init__(
        self,
        char:str=None,
        index:int=None,
        father_index:int=None,
    ) -> None:
        self._char:str = char
        self._index:int = index
        self._father_index:int = father_index
        self._children: List['Node'] = []

    @property
    def char(self) -> str:
        """
        This is the Getter and setter methods of the node char property.
        Is a the character string that this node represents.

        Parameters
        ----------
        (str)

        Return
        ------
        (str)
        """
        return self._char
    @char.setter
    def char(self, value: str) -> None:
        self._char = value

    @property
    def index(self) -> int:
        """
        This is the Getter and setter methods of the node char property.
        Is a the integer unique identification of the node in the tree.

        Parameters
        ----------
        (int)

        Return
        ------
        (int)
        """
        return self._index
    @index.setter
    def index(self, value: int) -> None:
        self._index = value

    @property
    def father_index(self) -> int:
        """
        This is the Getter and setter methods of the node char property.
        Is a the integer id of the father node that is prefix of the current char string.

        Parameters
        ----------
        (int)

        Return
        ------
        (int)
        """
        return self._father_index
    @father_index.setter
    def father_index(self, value: int) -> None:
        self._father_index = value

    def append_child(self, node:'Node'= None)->None:
        """
        This function can be used to append a new node to the list of child nodes of the current node.

        Parameters
        ----------

        node : Node
            A new node to be append as a node child of this current one.
        """
        if node is not None and isinstance(node, Node):
            self._children.append(node)

    def list_children(self)->List['Node']:
        """
        This function can be used to return a list of all nodes that is child of this current one.

        Return
        ------

        List[Node]
            It will return a list of child nodes of the current one.

        """
        return self._children

    def has_any_child(self)->bool:
        """
        This function can be used to check if the current node has at least one child node.

        Return
        ------

        bool
            True when the current node has one or more child, else will be false.

        """
        return len(self._children) > 0

    def get_shortcut(self)->Tuple[Union[int,str]]:
        """
        This function to the get the tuple that represent the current character on the
        Trie Tree.

        Return
        ------

        Tuple[Union[int,str]]
            It returns a 2-Tuple containing at the first position the index of the
            father node and at the second position, will be the value of the
            current node string.
        """
        return (self._father_index, self._char)

class Trie:
    """
    Trie

    This is a class is the Trie class, a data structure to store text as a Tree.
    It could be used to compress texts using the LZ78 algorithm.

    Attributes
    ----------

    root: Node
        The Trie tree as any tree has a root node that represent the start of the
        data structure, then this property will store the root node.

    index_counter: int
        Along the process of building the Trie, it's necessary to identify each node, using this index
        will be possible to increment a counter for the entire class.

    Methods
    -------

    build(text: str) -> List[Tuple[Union[int, str]]]
        Using this method will be possible receive a text and then process it in order
        to build a trie tree. At the end of the processs it will return a tuple
        of each node organized as LZ78 algorithm uses to compress the text.

    Usage Example
    -------------

    trie:Trie = Trie()
    encoded_text:List[Tuple[Union[int, str]]] = trie.encode(text='She sells sea shells by the sea shore.')
    """
    def __init__(self)->None:
        self._root:Node = Node()
        self._index_counter:int = 0
        self._initialize_root()

    def _initialize_root(self) -> None:
        """
        This function can be used internally to initialize the global counter and clear the root node.
        Also it could be used any time to estruture a new Trie based on a new text.
        """
        self._index_counter = 0
        self._root = Node('',self._index_counter,self._index_counter-1)
        self._index_counter += 1

    def _partial_search(self, node:Node, char:str)->Node:
        """
        This function can be used to proceed with a partial search.
        Given a node and a character ( piece of string ) it will search into all child node of the
        received node and return the node which has the character that matched with the received one.

        If it doesn't find any node with matched pattern it will return None.

        Parameters
        ----------

        node : Node
            A Trie Node.

        char : str
            A single string character.

        Return
        ------

        Node
            A child node from the received node which match the pattern of character of the current str.

        """
        response:Node = None
        if node.has_any_child():
            for each_node in node.list_children():
                if each_node.char == char:
                    response = each_node
                    break
        return response

    def build(self, text:str)->List[Tuple[Union[int, str]]]:
        """
        This function can be used to encode a entry text into a list of tuples
        with the representation of each pattern on the received text using the compression
        technique of the Trie.

        Parameters
        ----------

        text : str
            A string text.

        Return
        ------

        List[Tuple[Union[int, str]]]
            Using this method, it will return a tuple
            of each node organized as LZ78 algorithm uses to compress the text.

        """
        self._initialize_root()
        response:List = []
        size:int = len(text)
        if text and isinstance(text, str) and len(text)>=1:
            index:int = 0
            reference_node:Node = self._root
            inserted:bool = False
            while index < size:
                tmp_char:str = text[index]
                inserted = False
                result_node:Node = self._partial_search(node=reference_node, char=tmp_char)
                if result_node is None:
                    father_index:int = reference_node.index
                    node_index:int = self._index_counter
                    self._index_counter+=1
                    new_node:Node = Node(char=tmp_char, index=node_index, father_index=father_index)
                    inserted = True
                    response.append(new_node.get_shortcut())
                    reference_node.append_child(new_node)
                    reference_node = self._root
                else:
                    reference_node = result_node
                index+=1
            if not inserted:
                response.append(reference_node.get_shortcut())
        return response

class LZ78:
    """
    LZ78

    This is a class is the LZ78 class, the class that will receive a file
    and create a compressed file based on this received text content.
    Here is the total implementation of compression and descompression
    using the LZ78 algorithm and the Trie data structure.

    Methods
    -------

    read_file( file_path:str ) -> str
        Using this function, it will receive a path file as input paramenter
        and then will return the string containing the full content of the
        referenced file.

    write_file( file_path:str, content:str ) -> None
        Using this function, it will receive a path file as input paramenter
        and some string content and then will write the content on the file_path.

    decode_list_to_text( encoded_values:List[Tuple[int, str]] ) -> str
        Using this function, it will receive a list of 2-tuples and run throught it
        to obtain the original text string that this list represents and then
        return it.

    encode( file_path:str, output_file_path:str, base:int=10) -> None
        This function will receive a input and output path file, then will
        read the content from the input, decode it using the LZ78 algorithm and then
        will write the output on the output_file path.

    decode( file_path:str, output_file_path:str, base:int=10) -> None
        This function will receive a input and output path file, then will
        read the content from the input, decode it using the LZ78 algorithm and then
        will write the output on the output_file path.

    Usage Example
    -------------

    trie:Trie = Trie()
    encoded_text:List[Tuple[Union[int, str]]] = trie.encode(text='She sells sea shells by the sea shore.')
    """
    def __init__(self) -> None:
        pass

    def read_file(self, file_path:str)->str:
        """
        This function will receive a path file as input paramenter
        and then will return the string containing the full content of the
        referenced file.

        Parameters
        ----------

        file_path : str
            A string containing the file path to a certain file.

        Return
        ------

        str
            A string with the full input file content.
        """
        content:str = None
        with open(file_path, 'r') as file:
            content = file.read()
        return content

    def write_file(self, file_path:str, content:str)->None:
        """
        This function will receive a path file as input paramenter a
        and some string content and then will write the content on the file_path.

        Parameters
        ----------

        file_path : str
            A string containing the file path to a certain file.

        content : str
            A string with some text content.
        """
        with open(file_path, 'w') as file:
            file.write(content)

    def decode_list_to_text(self, encoded_values:List[Tuple[int, str]])->str:
        """
        This function will receive a list of 2-tuples and run throught it
        to obtain the original text string that this list represents and then
        return it.

        Parameters
        ----------

        encoded_values : List[Tuple[int, str]]
            A tuple of each node organized as LZ78 algorithm uses to compress the text.

        Return
        ------

        str
            A string with the original text content represented by the encoded_values input.

        """
        decoded_text:str = ''
        elements_list:List[str] = [None]
        for en, key in encoded_values:
            insert:str = ''
            if en == 0:
                insert = key
            else:
                insert = elements_list[en] + key
            elements_list.append(insert)
            decoded_text += insert
        return decoded_text

    def encode(self, input_file_path:str, output_file_path:str, base:int=10)->None:
        """
        This function will read the input file content use LZ78 algorithm to compress the
        data content and the write it on the output file. The representation of the numerical
        value will be used by representing the number in the base(parameter) numerical representation.

        Parameters
        ----------

        input_file_path : str
            The input file to read the text content.

        output_file_path : str
            The output file that the compressed content should be written.

        base: int
            A integer from 2 to 36 which represents the base of encoding to write a large
            integer number. Choosing 2 will be the binary base, 6 the hexadecimal base
            and 10 the decimal base. The best results is to choosing this value as 36.
        """
        content:str = self.read_file(input_file_path)
        trie:Trie = Trie()

        pre_encoded_content:List[Tuple] = trie.build(text=content)
        maximal_index:int = len(pre_encoded_content)
        bits_required:int = maximal_index.bit_length()
        input_str:str = ''
        final_bit_seq:int = 0

        for en, (value, key) in enumerate(pre_encoded_content[::-1]):
            input_str+=key
            final_bit_seq |= (value << en*bits_required)
        input_str = input_str[::-1]
        encoded_string:str = '{}|{}|{}'.format(
            str(maximal_index),
            str(final_bit_seq if base == 10 else np.base_repr(final_bit_seq, base)),
            input_str
        )
        self.write_file(output_file_path, encoded_string)

    def decode(self, input_file_path:str, output_file_path:str, base:int=10)->None:
        """
        This function will read the input file content use LZ78 algorithm to descompress the
        data content and the write it on the output file. The representation of the numerical
        value will be used by read the number represented on the base(parameter) numerical representation.

        Parameters
        ----------

        input_file_path : str
            The input file to read the text content.

        output_file_path : str
            The output file that the compressed content should be written.

        base: int
            A integer from 2 to 36 which represents the base of encoding to write a large
            integer number. Choosing 2 will be the binary base, 6 the hexadecimal base
            and 10 the decimal base. The best results is to choosing this value as 36.
        """
        list_values:List[Tuple] = []

        encoded_content:str = self.read_file(input_file_path)
        index_initial_perp:int = encoded_content.find('|')
        index_final_perp:int = encoded_content[index_initial_perp+1:].find('|') + index_initial_perp+1

        maximal_index:int = int(encoded_content[:index_initial_perp])
        bits_required:int = maximal_index.bit_length()

        final_bit_seq:int = int(encoded_content[index_initial_perp+1: index_final_perp], base)
        base_code:int = 1
        for _ in range(bits_required-1): base_code = (base_code<< 1) | 1

        for char in encoded_content[index_final_perp+1:][::-1]:
            value:int = base_code & final_bit_seq
            list_values.append((value, char))
            final_bit_seq >>= bits_required

        original_text:str = self.decode_list_to_text(list_values[::-1])
        self.write_file(output_file_path, original_text)
