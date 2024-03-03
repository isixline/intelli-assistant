import re
from intelli_assistant.utils.file_util import handle_file

def check_text_space(text):
    pattern = re.compile(r'(?<=[a-zA-Z])\s*(?=[\u4e00-\u9fa5])|(?<=[\u4e00-\u9fa5])\s*(?=[a-zA-Z])')
    formatted_text = re.sub(pattern, ' ', text)

    return formatted_text

def check_text_space_handle(**kwargs):
    file_path = kwargs.get('file_path')
    output_path = kwargs.get('output_path')
    output_path = handle_file(file_path, output_path, check_text_space)  

if __name__ == "__main__":
    file_path = input("file_path: ")
    output_path = input("output_path: ")
    check_text_space_handle(file_path=file_path, output_path=output_path)
             
