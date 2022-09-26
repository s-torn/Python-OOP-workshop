from functools import wraps

def add_logging(log_file):
    def _add_logging(fn):
        @wraps(fn)
        def logging(*args):
            with open(log_file, 'a') as file:
                file.write(f'Running function: {fn.__name__}.\n')
                return_value = fn(*args)
                file.write(f'Function result: {return_value}.\n')
            return return_value
        return logging
    return _add_logging
