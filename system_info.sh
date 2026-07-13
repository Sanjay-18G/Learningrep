
#!/bin/bash

echo "===== Linux System Information ====="
echo "Hostname: $(hostname)"
echo "Current User: $(whoami)"
echo "Date: $(date)"
echo "Kernel Version: $(uname -r)"
echo "Operating System: $(uname -o)"
echo "IP Address:"
hostname -I
echo "Disk Usage:"
df -h
echo "Memory Usage:"
free -h
# Linux System Information
