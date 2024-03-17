import os

def handle_file(input_path, output_path, handle_function):
    print('input_path: ', input_path)
    print('output_path: ', output_path)
    if not output_path:
        output_path = input_path.split('.')[0] + '_formatted.' + input_path.split('.')[1]
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            input_text = file.read()

        result = handle_function(input_text)
        if isinstance(result, list):
            formatted_text = '\n'.join(result)
        else:
            formatted_text = result

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(formatted_text)
        return output_path

    except Exception as e:
        print(e)