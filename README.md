# Blues Clues
A collection of scripts/notebooks for setting up red team assessments using Jupyter Notebooks

## Demo
![](Demo_20240317.gif)

## Setup
### Interacting with VM
First setup SSH on the VM to handle the key connection:  

`ssh-keygen -t rsa -b 4096`  
`ssh-keygen -p -m PEM -f /path/to/your/openssh_key`  
_Ensure `PubkeyAuthentication yes` is uncommented in `/etc/ssh/sshd_config`_  
`cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys`  
`systemctl restart sshd`  

## Development
- Set the notebook to automatically query for infrastructure information and store for future use
- Define initial recon actions and perform initial recon
- Do subsequent steps

## Considerations
Had an issue when using variables generated dynamically (for example, getting 'ext_ip' and using in a subsequent cell) because a '\n' was appended to the end. I fixed this with a strip in the output, but unclear whether this should be handled on a case-by-case basis or if the newly created command format is handled poorly.

## TODO
### General
- [ ] Finish project _4Head_
- [x] Fix the "cell_executed" functionality to avoid re-running blocks that already have output associated (unless forced)
  - Added Jupyter "pickles" which requires each cell to have a cell command to pass to the caching function, and either add to cache or display
  - Also added 'force_run' to the top of every cell to easily set whether the cell needs to be run again
- [ ] Add a way to define what cells are executed based on "assessment type" (probably just need to set the variable at the top, or maybe create separate files based on assessment type for readability)
  - Might need to just make different templates for each assessment type, this should lead to a cleaner setup
- [x] Fix SSH using key (probably local issue, fix permission error on Nix)
  - [ ] Add better error handling if key isn't working
- [ ] Add "loot" and "targets" feature to logs or commands to store specific info that can be used in future commands/good to know
- [ ] Build out Installation, and a requirements.txt
- [ ] Consider adding Infrastructure Setup page
  - [ ] Add a new command type for 'command_vm_proxy' which checks proxychains config and shows in logs the attack chain
  - [ ] Add checks to see if VM is bridged/using VPN address (curl ip.beer)
- [ ] Add error reporting in Windows/VM command
- [ ] Fix/streamline the command syntax within each cell to make a more repeatable method of creating new actions
  - Added '#Action Template' and all command handling is done in the same cell as caching now (with a handover to each cell for Windows/VM)
  - Consider adding 'Actions' class and combining Windows/VM into same cell

### Bugs
- [ ] In _command_exe_* the error output when returned with result returns a tuple and looks bad in output. The new way I reformatted command syntax made the error text show the ssh comms output. Need to handle that better in case there is errors (or maybe its a non-issue, needs testing)


### Initial Recon
- [ ] Add more options to read from file (depending on what information is available)