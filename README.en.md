# df-scope-hold

[简体中文](README.md) | English

Auto-hold-breath helper for Delta Force — while you hold the right mouse
button, the tool presses a configurable key (default `F12`) and releases it
when you let go. Aim with right-click only; no extra key press needed.

## How it works

Pure local mouse→keyboard mapping. The script listens for right-mouse-button
events and presses/releases your configured "hold breath" key in sync. It
activates only while the game process is running. **No game memory is read,
no game files are modified, no game-server traffic is involved** — the
behavior is equivalent to a hardware mouse macro.

The in-game "hold breath" binding must be set to **hold mode**, not toggle
mode, or the simulated key release on right-mouse-up will get out of sync
with the game's scope state.

## Usage

1. **Bind "hold breath" in-game** to a key that does not conflict with other
   actions (e.g. `F12`).
2. **Download** the latest `df-scope-hold-vX.X.X.zip` from [GitHub Releases](https://github.com/ZhengchenTao/df-scope-hold/releases) and unzip anywhere. If GitHub is slow in your region, a mirror is available at [Gitea Releases](https://git.zhengchentao.win/zhengchen.tao/df-scope-hold/releases) (auto-synced from each GitHub release).
3. **Edit `config.ini`** so `key` matches the in-game binding.
4. **Run `df-scope-hold.exe`**. UAC will prompt for admin privileges — accept,
   as the anti-cheat-protected game process is otherwise undetectable.

```ini
[config]
key = f12                                              ; must match in-game binding
delay_press = 5                                        ; ms between RMB-down and simulated key-down
program_running = DeltaForceClient-Win64-Shipping.exe  ; game process name (case-sensitive)
```

Press `Ctrl+C` in the console to exit.

## Runtime

Single Windows `.exe` (~10 MB), built with PyInstaller — bundles the Python
runtime and dependencies (`pynput`, `psutil`). No Python install required.

Verified on Windows only (the Delta Force client is Windows-exclusive).

## From source

```bash
pip install -r requirements.txt
python script.py
```

Requires Python 3.10+. For day-to-day use, just download a release.

## Build

```bash
pip install -r requirements.txt
pyinstaller --onefile --uac-admin --console --name df-scope-hold script.py
```

Output at `dist/df-scope-hold.exe`. GitHub Actions builds on `windows-latest`
(see `.github/workflows/release.yml`) when you push a `v*` tag, publishes the
zip to [GitHub Releases](https://github.com/ZhengchenTao/df-scope-hold/releases),
and mirrors it to [Gitea Releases](https://git.zhengchentao.win/zhengchen.tao/df-scope-hold/releases)
via the Gitea API — no local build needed.

## Disclaimer

- This is a purely local mouse→keyboard mapping tool, functionally identical
  to the macro feature of any gaming mouse.
- That said, the game publisher's policy on third-party input tools may
  change. **Any consequences from using this tool (including but not limited
  to account bans) are at the user's own risk.**
- For personal use and learning only. Do not use in ranked / competitive play.

## License

MIT
