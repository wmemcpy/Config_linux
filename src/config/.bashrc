#
# ~/.bashrc
#

[[ $- != *i* ]] && return

# Check if commands exist before setting them.
command -v col > /dev/null && command -v bat > /dev/null && export MANPAGER="sh -c 'col -bx | bat -l man -p'"
export MANROFFOPT="-c"

# Aliases
command -v ls > /dev/null && alias ls='ls --color=auto -F --group-directories-first'
alias ll='ls --color=auto -lF --group-directories-first'
alias la='ls --color=auto -aF --group-directories-first'
alias l='ls --color=auto -CF --group-directories-first'

command -v grep > /dev/null && alias grep='grep --color=auto'

YELLOW="\[\033[33m\]"
RED="\[\033[31m\]"
RESET="\[\033[00m\]"

parse_git_branch()
{
    local branch
    branch=$(git rev-parse --abbrev-ref HEAD 2> /dev/null)
    if [[ ! -z $branch ]]; then
        local git_status
        git_status=$(git for-each-ref --format '%(upstream:track)' "$(git symbolic-ref -q HEAD)" 2> /dev/null)
        local num_ahead num_behind
        num_ahead=$(echo $git_status | awk '/ahead/ {gsub(/[^0-9]/, "", $0); print $0}')
        num_behind=$(echo $git_status | awk '/behind/ {gsub(/[^0-9]/, "", $0); print $0}')
        local ahead behind
        [[ $num_ahead ]] && ahead="↑$num_ahead"
        [[ $num_behind ]] && behind="↓$num_behind"
        echo " ($branch$ahead$behind)"
    fi
}

prompt_command()
{
    local exit_code="$?"
    local ps1_elements=("\w${YELLOW}$(parse_git_branch)${RESET}")

    if [[ $exit_code -ne 0 ]]; then
        if [[ $exit_code -gt 128 ]]; then
            local signal_name
            signal_name=$(kill -l $exit_code 2>/dev/null)
            [[ $signal_name ]] && ps1_elements+=("${RED}(SIG$signal_name)${RESET}") || ps1_elements+=("${RED}($exit_code)${RESET}")
        else
            ps1_elements+=("${RED}($exit_code)${RESET}")
        fi
    fi
    ps1_elements+=('$ ')
    PS1=$(IFS=' '; echo "${ps1_elements[*]}")
}

PROMPT_COMMAND=prompt_command