""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"     ___      ___ ___  _____ ______   ________  ________        "
"    |\  \    /  /|\  \|\   _ \  _   \|\   __  \|\   ____\       "
"    \ \  \  /  / | \  \ \  \\\__\ \  \ \  \|\  \ \  \___|       "
"     \ \  \/  / / \ \  \ \  \\|__| \  \ \   _  _\ \  \          "
"    __\ \    / /   \ \  \ \  \    \ \  \ \  \\  \\ \  \____     "
"   |\__\ \__/ /     \ \__\ \__\    \ \__\ \__\\ _\\ \_______\   "
"   \|__|\|__|/       \|__|\|__|     \|__|\|__|\|__|\|_______|   "
"                                                                "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

autocmd FileType netrw setl bufhidden=wipe " Avoids netrw always stuck open
set autoread " trigger `autoread` when files changes on disk
  autocmd FocusGained,BufEnter,CursorHold,CursorHoldI * if mode() != 'c' | checktime | endif
  " autocmd FileChangedShellPost * " notification after file change
  "   \ echohl WarningMsg | echo "File changed on disk. Buffer reloaded." | echohl None

syntax on

set path+=**
set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
" set smartindent
set nocindent
set number relativenumber
set nu rnu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir="~/.config/nvim/undodir"
set undofile
set incsearch
set spelllang=en_gb,ro,cjk
set spellsuggest=best,9
set pumheight=10
set fileencoding=utf-8
set ruler
set cmdheight=2
set mouse=a
set splitright
set t_Co=256
set conceallevel=0
set smarttab
set indentexpr=""
set indentkeys=""
set laststatus=0
set showtabline=2
set noshowmode
set scrolloff=7
set updatetime=300
set timeoutlen=100
" set formatoptions-=cro
set clipboard="unnamedplus"
set nocompatible

set foldenable
set foldmethod=indent

filetype plugin indent on

set colorcolumn=85
highlight ColorColumn ctermbg=0 guibg=lightgray

" au! BufWritePost $MYVIMRC source %

let mapleader = " "
inoremap jk <ESC>
inoremap JK <ESC>
map <silent> <F5> :set spell!<CR>
