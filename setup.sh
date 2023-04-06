mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#d33682'\n\
backgroundColor = '#254117'\n\
secondaryBackgroundColor = '#586e75'\n\
textColor = '#fff'\n\
" > ~/.streamlit/config.toml