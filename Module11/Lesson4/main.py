import inspect

def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = []
    methods = []

    for item in dir(obj):
        if callable(getattr(obj, item)):
            methods.append(item)
        else:
            attributes.append(item)

    module = inspect.getmodule(obj)
    module_name = module.__name__ if module else None

    return {
        "type": obj_type,
        "attributes": attributes,
        "methods": methods,
        "module": module_name,
    }

number_info = introspection_info(42)
print(number_info)

class IntrospectionClass:
    def __init__(self, value):
        self.value = value

    def method1(self):
        pass

intro_class = IntrospectionClass(42)
intro_class_info = introspection_info(intro_class)
print(intro_class_info)
