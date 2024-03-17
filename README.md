# Blues Clues
A collection of scripts/notebooks for setting up red team assessments using Jupyter Notebooks

## Setup
### Interacting with VM
ssh-keygen -t rsa -b 4096
ssh-keygen -p -m PEM -f /path/to/your/openssh_key

## TODO
### General
- [ ] Add checks to see if VM is bridged/using VPN address (curl ip.beer)
- [ ] Fix the "cell_executed" functionality to avoid re-running blocks that already have output associated (unless forced)
- [ ] Add a way to define what cells are executed based on "assessment type" (probably just need to set the variable at the top, or maybe create separate files based on assessment type for readability)
- [ ] Fix SSH using key (probably local issue)
- [ ] Add "loot" and "targets" feature to logs or commands to store specific info that can be used in future commands/good to know
- [ ] Build out Installation, and a requirements.txt
- [ ] Finish project _4Head_

### Initial Recon
- [ ] Add more options to read from file (depending on what information is available)