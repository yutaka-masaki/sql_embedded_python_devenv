from jinja2 import pass_context

@pass_context
def string_var(context, name):
    return_value = "'" + context.get(name, None) + "'"
    if return_value is None:
        raise ValueError(f"Variable '{name}' not found in context.")
    return return_value

@pass_context
def var(context, name):
    return_value = context.get(name, None)
    if return_value is None:
        raise ValueError(f"Variable '{name}' not found in context.")
    return return_value