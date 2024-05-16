from exceptions.parenthesis_exception import ParenthesisError
class Calculator:
    def __init__(self):
        self.previous_value = 0

    def make_calculation(self,operation):
        if operation == "":
            return str(self.previous_value)
        
        if not self.is_balanced(operation):
            raise ParenthesisError
    
        if self.previous_value == 0:
            resolved_operation = eval(operation)
            self.previous_value = resolved_operation
            return str(resolved_operation)
        
        current_operation = str(self.previous_value) + operation
        resolved_operation = eval(current_operation)
        self.previous_value = resolved_operation
        return str(resolved_operation)
    
    def is_balanced(self,input_string):
        parentheses_map = {'(': ')'}
        stack = []
    
        for char in input_string:
            if char in parentheses_map:
                stack.append(char)
            elif char in parentheses_map.values():
                if not stack or parentheses_map[stack.pop()] != char:
                    return False
    
        return not stack
    
    def reset_previous_value(self):
        self.previous_value = 0

