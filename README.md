# Shadow-bot-

This repository contains a minimal Discord bot built with `discord.py` and voice support via `PyNaCl`.

Setup (secure, recommended):

- Add the bot token to GitHub repository secrets: `DISCORD_TOKEN` (Repository → Settings → Secrets and variables → Actions).
- The GitHub Actions workflow will run the bot on a schedule and uses the `DISCORD_TOKEN` secret for execution.

Local testing (development only):

- Create a `token.txt` file in the repository root with your bot token on a single line. Ensure `token.txt` is added to `.gitignore` or do not commit it.
- Or export the environment variable locally:

```bash
export DISCORD_TOKEN="your_token_here"
python main.py
```

Invite link (Administrator permissions):

https://discord.com/oauth2/authorize?client_id=1474000847514898462&permissions=8&scope=bot%20applications.commands

Files of interest:

- `main.py` — bot entrypoint; commands: `!reply`, `!join`, `!leave`, `!shutdown` (admin only).
- `requirements.txt` — dependencies.
- `.github/workflows/main.yml` — GitHub Actions workflow (cron: `0 */5 * * *`).

Security note:

Never commit your bot token to the repository. Use GitHub Secrets or other secure storage.
# Shadow-bot-