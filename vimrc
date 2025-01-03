syntax on
set background=dark
set shiftwidth=4        " when indenting with '>', use 4 spaces width
set tabstop=4           " show existing tab with 4 spaces width
set expandtab           " On pressing tab, insert 4 spaces
autocmd FileType go setlocal noexpandtab  " Disable expandtab for Go files

set showcmd             " Show (partial) command in status line.
set ignorecase          " Do case insensitive matching
set smartcase           " Do smart case matching
set incsearch           " Incremental search
set hidden              " Hide buffers when they are abandoned
set scrolloff=5         " keep at least 5 lines above/below

set hlsearch            " highlight search results (:noh to temporarily supress)
set autoindent          " when opening new line, copy indentation from line above

" magic to fix color scheme in tmux
set background=dark
set t_Co=256

if &term =~ '^screen'
    " tmux will send xterm-style keys when its xterm-keys option is on
    execute "set <xUp>=\e[1;*A"
    execute "set <xDown>=\e[1;*B"
    execute "set <xRight>=\e[1;*C"
    execute "set <xLeft>=\e[1;*D"
endif

" include pylint
set makeprg=pylint\ --reports=n\ --msg-template=\"{path}:{line}:\ {msg_id}\ {symbol},\ {obj}\ {msg}\"\ %:p
set errorformat=%f:%l:\ %m

let g:black_use_virtualenv = 0  " use the system black instead of separate virtualenv one
call plug#begin('~/.vim/plugged')
Plug 'Konfekt/FastFold'
Plug 'tmhedberg/SimpylFold'
Plug 'psf/black'
call plug#end()

" run black on save
augroup black_on_save
  autocmd!
  autocmd BufWritePre *.py Black
augroup end
