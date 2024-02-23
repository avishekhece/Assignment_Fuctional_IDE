from .models import TestCase


def get_test_case_data(test_case_id):
    try:
        test_case = TestCase.objects.get(id=test_case_id)
        input_data = test_case.input_data
        expected_output = test_case.expected_output
        return input_data, expected_output
    except TestCase.DoesNotExist:
        return None, None


# # Example usage:
# test_case_id = 1
# input_data, expected_output = get_test_case_data(test_case_id)
# if input_data is not None:
#     print("Input Data:", input_data)
#     print("Expected Output:", expected_output)
# else:
#     print("Test case with ID", test_case_id, "does not exist.")


def compile_python_code(code, input_data):
    try:
        # compiled_code = compile(code, "<string>", "exec")
        # namespace = {'input_data': input_data}
        # exec(compiled_code, namespace)
        # print("============================================================================================")
        # print(namespace)
        # output = namespace.get('output')
        # return output, True
        compiled_code = compile(code, "<string>", "exec")
        namespace = {'input_data': input_data, 'output': None}  # Initialize 'output' variable in the namespace
        exec(compiled_code, namespace)
        output = namespace.get('output')  # Retrieve the value of 'output' variable from the namespace
        return output, True
    except SyntaxError as e:
        # Handle syntax errors
        return f"Syntax Error: {e}", False
    except Exception as e:
        # Handle other exceptions
        return f"Error: {e}", False

