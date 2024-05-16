class Calculator:
    def __init__(self):
        self.previous_value = 0

    def make_calculation(self,operation):
        print(operation)
        if operation == "":
            return str(self.previous_value)
        
        if self.previous_value == 0:
            resolved_operation = eval(operation)
            self.previous_value = resolved_operation
            return str(resolved_operation)
        
        current_operation = str(self.previous_value) + operation
        resolved_operation = eval(current_operation)
        self.previous_value = resolved_operation
        return str(resolved_operation)
