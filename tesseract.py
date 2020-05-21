try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re
# print(pytesseract.image_to_boxes(Image.open('worked.png')))
# print(pytesseract.image_to_boxes(Image.open('worked.png')))
def read_image_string(image_string):
    lines_of_files = image_string.split('\n')#a lot of these lines are empty
    potential_keys_and_values = [line for line in lines_of_files if line.strip() != '']#line.strip() takes all lines of spaces and converts that line to ''. line.strip() also gets rid of space before start of string and after.
    # print(potential_keys_and_values)
    queue = []
    kv_map={}
    first_key_found = False
    c=0
    for line in potential_keys_and_values:
        if ':' in line:
            keys_splitted = line.split(':')
            for key in keys_splitted:
                print(key)
                queue.append(key)
            first_key_found = True
        if ':' not in line and first_key_found:
            values_splitted = line.split(' ')
            print('ye')
            print(line)
            for val in values_splitted:
                if len(queue) != 0:
                    kv_map[queue.pop(0)] = val
        c+=1
        if c==3:
            break
    print(kv_map)

    
image_string = pytesseract.image_to_string(Image.open('leftright.png'))
key_value_pairs = read_image_string(image_string)
def find_first_key(image_string):
    pattern = ""
# def extract_data(img_file_path):
#     data = pytesseract.image_to_data(Image.open(img_file_path))
#     # print(data)
#     arrays = map(lambda s: s.split('\t'), data.split('\n'))[1:]
#     words = map(lambda arr: arr[0:6] + map(lambda i: int(i), arr[6:-1]) + [arr[-1]], arrays)
#     words = filter(lambda arr: arr[CONF_INDEX] >0 and arr[WORD_INDEX], words)
#     lines = [processingOneLineOfWords(map(lambda x: x, it)) for k, it in groupby(words, lambda arr: ','.join(arr[0:5]))]
#     return [lines]
# print(extract_data('worked.png'))
