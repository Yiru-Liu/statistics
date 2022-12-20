#!/usr/bin/env python3

def main():
    inputs = []
    while True:
        current_input = input()
        if current_input == "done":
            break
        inputs.append(current_input)
    list2d = [i.split() for i in inputs]
    print(list2d)


if __name__ == '__main__':
    main()
