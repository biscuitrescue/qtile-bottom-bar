call plug#begin('~/.nvim/plugged')

" syntax highlighting
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Plug 'sheerun/vim-polyglot'

" files hierarchy tree
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Plug 'scrooloose/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'

" toggle NERDTree with <Control N> hot key
map <C-n> :NERDTreeToggle<CR>

" cool icons
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Plug 'ryanoasis/vim-devicons'

let g:webdevicons_enable_nerdtree = 1

" editorconfig support
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Plug 'editorconfig/editorconfig-vim'

" git integration
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'

" lean & mean status/tabline
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
let g:airline_theme='dracula'
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 2
" testing extra-powerline-symbols

" set font terminal font or set gui vim font to a Nerd Font (https://github.com/ryanoasis/nerd-fonts):
set guifont=Droid\ Sans\ Mono\ for\ Powerline\ Plus\ Nerd\ File\ Types\ Mono\ 12

" testing rounded separators (extra-powerline-symbols):
let g:airline_left_sep = "\uE0B4"
let g:airline_right_sep = "\uE0B6"

" set the CN (column number) symbol:
" emmet (like), essential toolkit for abbreviation expansion
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Plug 'mattn/emmet-vim'

" trigger expansion with <Comma> <Comma> keys
let g:user_emmet_leader_key=','

let g:user_emmet_settings = {
\  'javascript' : {
\    'extends' : 'jsx',
\    'quote_char': "'",
\  },
\}

" awesome completion tool
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Plug 'neoclide/coc.nvim', {'branch': 'release'}

" use <Tab> key to trigger completion and navigate to the next complete item
function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~ '\s'
endfunction
inoremap <silent><expr> <Tab>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<Tab>" :
      \ coc#refresh()

" insert or delete parenthesis in pair
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Plug 'vim-scripts/auto-pairs-gentle'

" toggle comments
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" use `gcc` to comment out a line (takes a count),
" `gc` in visual mode to comment out the selection, and much more...
Plug 'tpope/vim-commentary'

" search tool
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Plug 'mileszs/ack.vim'

" my favourite colorscheme, bubblegum
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'joshdick/onedark.vim'
Plug 'arcticicestudio/nord-vim'
Plug 'owozsh/amora'
" vim-plug end, add plugins to &runtimepath
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
"let g:deoplete#enable_at_startup = 1
Plug 'lilydjwg/colorizer' 
Plug 'myusuf3/numbers.vim'

" Automatically sort python imports
Plug 'fisadev/vim-isort'
Plug 'neomake/neomake'

Plug 'francoiscabrol/ranger.vim'
Plug 'rbgrouleff/bclose.vim'
call plug#end()

" activate bubblegum colorscheme
" colorscheme bubblegum-256-dark
" let g:airline_theme='bubblegum'

