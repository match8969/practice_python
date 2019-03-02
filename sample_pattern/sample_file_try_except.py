

"""
Effective Python page.27
"""
import json
UNDEDINED = object()

def divided_json(path):
    handle = open(path, 'r+')  # IOError may happen
    try:
        data = handle.read()  # UnicodeDecodeError may happen
        op = json.loads(data)  # ValueError may happen
        value = (
            op['numerator'] /
            op['denominator'])
    except ZeroDivisionError as e:  # ZeroDivisionError may happen
        return UNDEDINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)  # IOError may happen
        return value
    finally:
        handle.close()  # Always run
