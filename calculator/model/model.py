from exceptions.parenthesis_exception import ParenthesisError
import numexpr as ne

class Calculator:
    def __init__(self):
        self.previous_value = 0

    def make_calculation(self, operation):
        if operation == "":
            return str(self.previous_value)
        
        if not self.is_balanced(operation):
            raise ParenthesisError
        
        try:
            if self.previous_value == 0:
                resolved_operation = ne.evaluate(operation)
            else:
                current_operation = f"{self.previous_value}{operation}"
                resolved_operation = ne.evaluate(current_operation)
            
            self.previous_value = resolved_operation
            return str(resolved_operation)
        except Exception as e:
            raise ValueError("Revise la cuenta por favor")
    
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

