from typing import Dict, List

from node import Node


def get_node(char: str, freq: int, left: Node | None, right: Node | None) -> Node:
    return Node(char, freq, left, right)


def encode(root: Node, string: str, huffman_code: Dict) -> None:
    if root is None:
        return

    if root.left_node is not None and root.right_node is not None:
        huffman_code[root.char] = string
        print(root.left_node.char)
        # print(root.right_node.char)
    encode(root.left_node, string + "0", huffman_code)
    encode(root.right_node, string + "1", huffman_code)
    # print(huffman_code)


def decode(root: Node, index: int, string: str) -> None:
    if root is None:
        return

    if root.left_node is not None and root.right_node is not None:
        # print(root.char)
        return

    index += 1

    if string[index] == "0":
        decode(root.left_node, index, string)
    else:
        decode(root.right_node, index, string)


def build_huffman_tree(text: str):
    freq: Dict = {}
    for ch in text:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1

    pq: List = []

    for pair in freq:
        key = pair
        val = freq[key]
        pq.append(get_node(key, val, None, None))
    # pq.sort()
    while len(pq) != 1:
        left: Node = pq.pop(0)
        right: Node = pq.pop(0)

        summ = left.freq + right.freq
        # print(left.char)
        # print(right.char)
        pq.append(get_node("0", summ, left, right))

    root: Node = pq[0]
    huffman_code: Dict = {}
    # print(f"Root: {root.freq}")
    encode(root, "", {})
    # print(huffman_code)
    # print("Huffman codes are: ")
    # for pair in huffman_code:
    #     key = pair
    #     print(key)
    #     val = freq[key]
    #     print(key + " " + val)
    # print(f"Original string was: {text}")
    #
    # string: str = ""
    # for ch in text:
    #     string += huffman_code[ch]
    # print(f"Encoded string is: {string}")
    #
    # index = -1
    # print("Decoded string is: ")
    # while index < int(len(string) - 2):
    #     decode(root, index, string)


def main():
    text: str = "Huffman coding is a data compression algorithm."
    build_huffman_tree(text)


if __name__ == "__main__":
    main()
