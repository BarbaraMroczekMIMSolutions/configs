syntax on
set background=dark
set shiftwidth=4        " when indenting with '>', use 4 spaces width
set tabstop=4           " show existing tab with 4 spaces width
set expandtab           " On pressing tab, insert 4 spaces

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

call plug#begin('~/.vim/plugged')
" example
" Plug 'tpope/vim-sensible'
Plug 'psf/black', { 'branch': 'stable' }
call plug#end()
