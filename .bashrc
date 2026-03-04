# Load system-wide bashrc if present
if [ -f /etc/bash.bashrc ]; then
    source /etc/bash.bashrc
fi

# Git prompt
source /usr/share/git-prompt.sh
# Git completion
source /usr/share/bash-completion/bash_completion

export PS1="\[\e[32m\]\w\[\e[33m\]\$(__git_ps1 ' (%s)')\[\e[0m\]\$ "
