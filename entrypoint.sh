cat > config.toml <<- EOF
[discord]
token = "$DISCORD_TOKEN"
user_id = "$DISCORD_USER_ID"

[urlroulette]
host = "$URLROULETTE_HOST"
secret = "$URLROULETTE_SECRET"
EOF

python main.py
