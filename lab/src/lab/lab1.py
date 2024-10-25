import traceback

def run_code(code, func_name, *args):
    context = {} 
    try:
        exec(code, context)
        if func_name in context and callable(context[func_name]):
            result = context[func_name](*args)
            return {"result": result}
        else:
            return {"error": f"Function '{func_name}' is not defined or is not callable."}
    
    except RecursionError:
        return {"error": "RecursionError: Maximum recursion depth exceeded"}
    except Exception:
        tb = traceback.format_exc().strip().split('\n')
        error_msg = '\n'.join(tb[4:]) if len(tb) > 4 else '\n'.join(tb)
        return {"error": error_msg}
    
def run_python(code,q):
    l = q
    r=[]
    for i in range(0, len(l), 2):
        result = run_code(code, 'fn', int(l[i]))
        if 'error' in result:
            r.append([result['error'], 0])
        else:
            r.append([result.get('result', 'Key not found in context'), 1])

    r.append(l)
    return r

if __name__ == "__main__":
    recursive_code = """
def fn(n):
    if n == 0:
        return 1
    else:
        return n * fn(n-1)
"""
    q=['5','124','2','3']
    print(run_python(recursive_code,q))