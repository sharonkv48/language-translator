mkdir -p ~/.streamlit/

echo "/
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = trie\n\
\n\
" > ~/.streamlit/confog.toml