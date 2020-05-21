try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# print(pytesseract.image_to_boxes(Image.open('worked.png')))
print(pytesseract.image_to_data(Image.open('worked.png')))

# def extract_data(img_file_path):
#     data = pytesseract.image_to_data(Image.open(img_file_path))
#     # print(data)
#     arrays = map(lambda s: s.split('\t'), data.split('\n'))[1:]
#     words = map(lambda arr: arr[0:6] + map(lambda i: int(i), arr[6:-1]) + [arr[-1]], arrays)
#     words = filter(lambda arr: arr[CONF_INDEX] >0 and arr[WORD_INDEX], words)
#     lines = [processingOneLineOfWords(map(lambda x: x, it)) for k, it in groupby(words, lambda arr: ','.join(arr[0:5]))]
#     return [lines]
# print(extract_data('worked.png'))
