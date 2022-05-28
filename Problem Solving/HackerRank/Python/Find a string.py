
def count_substring(string, sub_string):
    results = 0
    sub_len = len(sub_string)
    for i in range(len(string)):
        if string[i:i+sub_len] == sub_string:
            results += 1
    return results

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)