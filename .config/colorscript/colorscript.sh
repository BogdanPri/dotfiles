#!bin/zsh

declare -a lst=(tiefighter2 tiefighter1row thebat2 tanks square six rails rally-x panes manjaro jangofett ghosts fade crunchbang-mini)

random_array_element() {
    local arr=("$@")
    return '%s\n' "${arr[RANDOM % $#]}"
}

${lst[@]}
