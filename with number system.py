from itertools import chain
import random

binary_code = lambda word, binary: str(random.choice(binary)) + (
    format(ord(word), "04b")
)
hexadacimel_code = lambda word, hexadacimel: str(random.choice(hexadacimel)) + (
    format(ord(word), "04x")
)
octal_code = lambda word, octal: str(random.choice(octal)) + (format(ord(word), "04o"))


def random_encode(sentence, extra_word):
    list_sentence = sentence.split(" ")
    for word in list_sentence:
        if len(word) >= 3:
            r1 = random.choice(extra_word)
            r2 = random.choice(extra_word)
            secret_words = r1 + word[-1] + word[1:-1] + word[0] + r2
            coded_value.append(secret_words)
        else:
            coded_value.append(word[::-1])
    return " ".join(coded_value)


def random_decode(sentence):
    list_sentence = sentence.split(" ")
    for word in list_sentence:
        if len(word) >= 3:
            unordered_word = word[3:-3]
            natural_word = unordered_word[-1] + unordered_word[1:-1] + unordered_word[0]
            coded_value.append(natural_word)
        else:
            coded_value.append(word[::-1])
    return " ".join(coded_value)


coded_value = []
coded_sentance = []
hexadacimel = list(
    map(
        str,
        [
            5234,
            4000,
            6976,
            9999,
            9564,
            3789,
            2549,
            1287,
            5346,
            5436,
            6666,
            8090,
            5598,
            1290,
            9080,
        ],
    )
)
binary = list(
    map(
        str,
        [
            "0000",
            1000,
            "0100",
            "0010",
            "0001",
            1100,
            1110,
            1111,
            1001,
            "0101",
            1101,
            1010,
            "0110",
            "0111",
            "0011",
        ],
    )
)
octal = list(
    map(
        str,
        [
            1200,
            "0012",
            8000,
            7000,
            8700,
            8712,
            8701,
            8702,
            8877,
            8880,
            5000,
            1234,
            1965,
            5643,
            2341,
        ],
    )
)
extra_word = [
    "dog",
    "gyj",
    "hjk",
    "fgy",
    "eft",
    "sry",
    "yzx",
    "vwh",
    "hyd",
    "ynd",
    "heo",
    "vuy",
    "joy",
    "ban",
    "has",
]
function_choice = [binary_code, hexadacimel_code, octal_code]

print("\033[36m              Encode......1\n              Decode......2\033[0m")
while True:
    str_user_choice = input("\033[36m\nWhich one you choose:")
    print("\033[0m")

    if str_user_choice not in ["1", "2"]:
        print("\033[31m            Enter valid number\033[0m")
        continue
    else:
        user_choice = int(str_user_choice)
        break

if user_choice == 1:
    sentence = input("Enter the sentence: ")
    sentence = random_encode(sentence, extra_word)
    for word in sentence:
        function_name = random.choice(function_choice)
        identified_word = (
            (binary)
            if function_name == binary_code
            else (
                (octal)
                if function_name == octal_code
                else (hexadacimel) if function_name == hexadacimel_code else ""
            )
        )
        coded_word = function_name(word, identified_word)
        coded_sentance.append(coded_word.upper())
    print("\n\033[36mThe Encoded value is:\n")
    print(" ".join(coded_sentance))

else:
    while True:
        secret_codes = input("Enter the secret code: ")
        secret_codes_list = secret_codes.split(" ")
        stop = 1

        for number in secret_codes:
            if number not in [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                " ",
            ]:
                print("\033[31m\n            Enter valid number\n\033[0m")
                stop = 0
                break
        if stop == 0:
            continue

        for element in secret_codes_list:
            if element[:4] not in chain(hexadacimel, binary, octal):
                print("\033[31m\n         Invalid identified code\n\033[0m ")
                stop = 0

        if stop == 0:
            continue
        else:
            break
    secret_codes_list = secret_codes.split(" ")

    for element in secret_codes_list:
        identified_code = element[:4]
        unordered_letter = (
            chr(int(element[4:], 2))
            if identified_code in binary
            else (
                chr(int(element[4:], 16))
                if identified_code in hexadacimel
                else chr(int(element[4:], 8)) if identified_code in octal else "break"
            )
        )
        coded_sentance.append(unordered_letter)

    unordered_sentence = "".join(coded_sentance)
    natural_sentence = random_decode(unordered_sentence)
    print(f"\n\033[36mThe Decoded result is:\n\n{natural_sentence}")
