class MockClass():
    def __init__(self, class_name):
        self.class_name = class_name
        self.methods_mocked = []

    def mock_method_and_return(self, method_name, return_value):
        self.methods_mocked.append(method_name)
        
        return self.and_return(return_value)
    
    def and_return(self, return_value):
        return return_value
    