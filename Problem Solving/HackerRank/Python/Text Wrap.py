import textwrap

def wrap(string, max_width):
    final_result = ""
    result = [string[i:i+max_width] for i in range(0, len(string), max_width)]
    for i in result:
        final_result += f"{i}\n"
    return final_result
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)