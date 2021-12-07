class Node:
    __char: str = ""
    __freq: int = 0
    __left_node = None
    __right_node = None

    def __init__(self, char, freq, left_node, right_node) -> None:
        self.__char = char
        self.__freq = freq
        self.__left_node = left_node
        self.__right_node = right_node

    @property
    def freq(self) -> int:
        return self.__freq

    @property
    def char(self) -> str:
        return self.__char

    @property
    def left_node(self):
        return self.__left_node

    @property
    def right_node(self):
        return self.__right_node
