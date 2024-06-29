def run_embedded_python_code(code, args):
    local_context = {"args": args}
    exec(code, {}, local_context)
    return local_context




def run_code(code):
    arguments = {"num": 4}
    context = run_embedded_python_code(code, arguments)

    if (context['result']==24):
        print("passed")
    else:
        print(context)