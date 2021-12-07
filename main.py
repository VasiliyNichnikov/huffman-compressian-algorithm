from typing import Dict, List

from node import Node


def get_node(char: str, freq: int, left: Node | None, right: Node | None) -> Node:
    return Node(char, freq, left, right)


def sort_by_freq(node: Node):
    return node.freq


def compare_node(a: Node, b: Node):
    if a.freq < b.freq:
        return -1
    return 1


def encode(root: Node, string: str, huffman_code: Dict) -> None:
    if root is None:
        return

    if root.left_node is None and root.right_node is None:
        huffman_code[root.char] = string

    encode(root.left_node, string + "0", huffman_code)
    encode(root.right_node, string + "1", huffman_code)


def decode(root: Node, index: int, string: str) -> int:
    if root is None:
        return index

    if root.left_node is None and root.right_node is None:
        print(root.char, end='')
        return index

    index += 1

    if string[index] == "0":
        index = decode(root.left_node, index, string)
    else:
        index = decode(root.right_node, index, string)
    return index


def build_huffman_tree(text: str):
    freq: Dict = {}
    for ch in text:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1
    pq: List = []

    for pair in freq:
        key = pair
        val = freq[key]
        pq.append(get_node(key, val, None, None))

    pq.sort(key=sort_by_freq)

    while len(pq) != 1:
        left: Node = pq.pop(0)
        right: Node = pq.pop(0)

        summ = left.freq + right.freq
        pq.append(get_node("\0", summ, left, right))

    root: Node = pq[0]
    huffman_code: Dict = {}
    encode(root, "", huffman_code)

    print("Коды Хаффмана:")
    for pair in huffman_code:
        key = pair
        val = huffman_code[key]
        print(f"{key} : {val}")
    print(f"Оригинальная строка: {text}")

    string: str = ""
    for ch in text:
        string += huffman_code[ch]
    print(f"Закодированная строка: {string}")

    index = -1
    print("Декодированная строка:", end=' ')
    while index < int(len(string) - 2):
        index = decode(root, index, string)


def main():
    text: str = "Ничников Василий Алексеевич"
    build_huffman_tree(text)


if __name__ == "__main__":
    main()
