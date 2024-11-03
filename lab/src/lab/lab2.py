import subprocess
import tempfile
import traceback

def compile_and_run_c_code(c_code, func_name, *args):
    try:
        with tempfile.NamedTemporaryFile(suffix=".c", delete=False) as c_file:
            c_file.write(c_code.encode())
            c_file_path = c_file.name
        executable_path = c_file_path[:-2] 
        compile_process = subprocess.run(
            ["gcc", c_file_path, "-o", executable_path],
            capture_output=True,
            text=True
        )
        
        if compile_process.returncode != 0:
            return {"error": f"Compilation failed:\n{compile_process.stderr}"}
        input_data = "\n".join(map(str, args)) + "\n"
        
        run_process = subprocess.run(
            [executable_path],
            input=input_data,
            capture_output=True,
            text=True
        )
        
        if run_process.returncode != 0:
            return {"error": f"Execution failed:\n{run_process.stderr}"}
        
        return {"result": run_process.stdout.strip()}
    
    except Exception as e:
        tb = traceback.format_exc().strip().split('\n')
        error_msg = '\n'.join(tb[4:]) if len(tb) > 4 else '\n'.join(tb)
        return {"error": error_msg}

def run_c_code(c_code, q):
    l = ['1','2','2','4']
    r = []
    for i in range(0, len(l), 2):
        arg = l[i]
        if arg.replace('.', '', 1).isdigit():
            if '.' in arg:
                arg = float(arg)
            else:
                arg = int(arg)
        
        result = compile_and_run_c_code(c_code, 'main', arg)
        if 'error' in result:
            r.append([result['error'], 0])
        else:
            r.append([result.get('result', 'Key not found in context'), 1])

    r.append(l)
    return r


c_code = """
#include <stdio.h>

int fn(n)
{
 int  r = n*2;
return r;}


int main() {
    int num;
    scanf("%d", &num); // Example scanf
    printf("%d", fn(num)); // Example operation: double the input
    return 0;
}
"""

results = run_c_code(c_code, "test input")
print(results)
