# Version 1.2.2
# Imports
import paramiko, os, datetime, subprocess, pickle, socket, scp

# Global Variables
var_target_ip = '127.0.0.1'
var_assess_name = 'TestAssess1'
var_log_location = f'Logs/{var_assess_name}'

#VM Config
var_vm_host = '192.168.138.130'
var_vm_port = 22
var_vm_username = 'bloodvault'
var_vm_password = ''
var_vm_key = 'Keys/kali_dev'
var_vm_lootdir = f'~/BluesClues/{var_assess_name}/loot'

# Append to Log
if not os.path.exists(var_log_location):
    open(f'{var_log_location}.txt', 'a').close()
    
def append_log(source, command, output):
    with open(f'{var_log_location}.txt', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f'Timestamp: {timestamp}\n')
        log_file.write(f'Source: {source}\n')
        log_file.write(f'Command: {command}\n')
        log_file.write(f'Output:\n{output}\n')
        log_file.write('=' * 70 + '\n')


# Run VM Commands
def command_exe_vm(command):
    # Initialize the SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Connect to the VM
    if var_vm_key:
        key = paramiko.RSAKey.from_private_key_file(var_vm_key)
        try:
            client.connect(hostname=var_vm_host, port=var_vm_port, username=var_vm_username, pkey=key)
        except socket.error as e:
            print(f'[!] Unable to connect to {var_vm_host} on {var_vm_port}, check if SSH is running')
        except paramiko.SSHException as e:
            print(f'[!] SSH Configuration Error: {e}')
        except Exception as e:
            print(f'[!] Unknown error: {e}')
    else:
        # If ssh key isn't working or configured, connect via username/password
        client.connect(hostname=var_vm_host, port=var_vm_port, username=var_vm_username, password=var_vm_password)
    
    # Execute the command
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')
    
    # Close the SSH connection
    client.close()
    #TODO Returning errors looks like trash in output, if added in return
    #if error == '':
    #    append_log('VM', command, output)
    #    return output
    #else:
    #    append_log('VM', command, f'Error: {error}')
    #    return output
    append_log('VM', command, output)
    return output

def command_scp_put_vm(local_path, vm_path):
    # Initialize the SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    key = paramiko.RSAKey.from_private_key_file(var_vm_key)
    client.connect(hostname=var_vm_host, port=var_vm_port, username=var_vm_username, pkey=key)

    scpclient = scp.SCPClient(client.get_transport())
    scpclient.put(local_path, vm_path)
    scpclient.close()
    print(f'[*] File transferred to VM: {vm_path}')

# Run Windows Commands Locally
def command_exe_win(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode == 0:
        output = out.decode('utf-8').strip()
    else:
        output = err.decode('utf-8').strip()
    
    append_log('Local', command, output)
    return output

# Start Caching and Command Execution
def cache_data(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def load_cached_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)

def cache_command_output(cache_id, force_run, os_type, run_command):
    cache_folder = 'Cache'
    unique_id = f'{cache_id}.pkl'
    cache_file_path = os.path.join(cache_folder, unique_id)

    os.makedirs(cache_folder, exist_ok=True)

    cached_data = load_cached_data(cache_file_path)
    if cached_data is not None and force_run == False:
        print('[*] Loading data from cache.')
        return cached_data
    elif force_run == 'skip':
        print('[*] Skipping cell execution')
    else:
        print('[+] Cache not found or execution forced, executing command.')
        if os_type == 'win':
            result = command_exe_win(run_command)
        elif os_type == 'vm':
            result = command_exe_vm(run_command)
        cache_data(result, cache_file_path)
        return result
    
# Action Template Explained

# Whether to force the command to run regardless of cache
## [Options: True (executes action), False (prints cache or nothing), skip (skips action execution)]
#force_run = False

# The name of the cache file
#cmd_cache = ''

#The syntax passed to the command
#cmd_syntax = ''

#Whether to run the command on local system or VM (accepts 'win' or 'vm')
#cmd_os = ''

#The cache and run function, no edits necessary
#output = templates.cache_command_output(cmd_cache, force_run, cmd_os, cmd_syntax)

#print(output)