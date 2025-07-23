# SkinsRadar
## [➡ Russian ReadMe](docs/RuREADME.md)

<img src="assets/icon_white.png" alt="SkinsRadar Logo" width="200"/>
<img src="https://img.shields.io/badge/python-3.9--3.13-blue.svg" alt="Python" />


SkinsRadar is a powerful **CS2 skins monitoring tool** for [steamcommunity.com](https://steamcommunity.com) 🚀. It helps you track and analyze skin prices, bypass Steam's request limits using proxies (**❗Only socks4:// socks5://** ), and find profitable deals for trading or other purposes. **No account registration or login required** 🔑—dive right in!

With two core modes—**Radar Mode** ⚡ for rapid scanning of all CS2 items and **Browser Mode** 📊 for detailed exploration of specific items—SkinsRadar is perfect for active skin traders, buyers, or anyone looking to navigate Steam's marketplace without restrictions.

## ✨ Features

- **Radar Mode** ⚡:
  - Scan all CS2 skins and items to find profitable deals based on customizable parameters:
    - 💰 Profit percentage (with Steam's commission, default 13.0%).
    - 📈 Monthly sales volume.
    - 🗂️ Filter by item groups (e.g., Souvenir, StatTrak™, ★ Knife | Gloves).
    - 🗲 Skip boosted items with a configurable boost percentage (default 30.0%).
- **Browser Mode** 📊:
  - Browse over **23,000 CS2 items** with detailed listings:
    - 🔍 View all lots, including stickers and charms for skins.
    - 🎨 Filter by Exterior (wear), number of lots (Amount), and currency.
    - 💸 Instantly see profit percentage compared to the Autobuy price.
- **Proxy Management** 🌐:
  - Add proxies via text files, stored in a database with rotation to bypass Steam's request limits.
- **Multi-Currency Support** 💱:
  - Supports ~40 Steam-supported currencies in Browser Mode; Radar Mode uses USD.
- **Settings** ⚙️:
  - 💸 Customize Steam commission (default 13.0%).
  - 🗲 Set maximum boost percentage (default 30.0%).
  - 📂 Add proxies via file explorer (`Update Proxy` button).
  - 🗑️ Clear proxy database (`Wipe Proxies Database` button).
  - 🗄️ Update or rebuild the CS2 items database (`Update Skins Database` button).
  - 🌙 Switch between Dark and Light themes (defaults to system theme).
- **No Registration Required** 🔓:
  - Access all features without needing a Steam account or API key.
- **Logging** 📜:
  - Configurable logging for debugging with language (`--lang=ru` or `--lang=en`) and log level options (`DEBUG`, `INFO`, etc.).

## 🛠️ Installation

SkinsRadar is tested and supported on Python 3.9 to 3.13 for optimal performance 🐍.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Max2772/SkinsRadar.git
   cd SkinsRadar
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure proxies** (optional) 🌐:
   - Use the `Update Proxy` button to add proxies via a text file.
   - The app automatically filters working proxies and avoids duplicates.
4. **Initialize the skins database** (optional) 🗄️:
   - Use the `Update Skins Database` button to create or update the CS2 items database.

### Dependencies 📋
- Python 3.9–3.13
- `flet==0.28.3`
- `httpx==0.28.1`
- `httpx_socks==0.10.1`
- `aiosqlite==0.21.0`
- `aiofiles==24.1.0`
- `tqdm==4.67.1`
- `fuzzywuzzy==0.18.0`
- `python-Levenshtein==0.27.1`
- `tzdata==2025.2`

See `requirements.txt` for the full list.

## 🚀 Usage

### Running the Application
- **Via Python**:
  ```bash
  python3 main.py
  ```
  Optional arguments:
  - `--lang=ru` or `--lang=en`: Set the terminal logger language (Russian or English).
  - `--log-level=DEBUG|INFO|WARNING|WARN|ERROR|FATAL|CRITICAL`: Configure the logging level.

- **Via Pre-built Binaries**:
  - Use the executables in the `build/` directory for Windows or Linux.

### Example Workflow
1. **Launch the app**:
   ```bash
   python3 main.py --lang=en --log-level=INFO
   ```
2. **Radar Mode** ⚡:
   - Set profit percentage, sales volume, and item groups.
   - Enable 🗲 Skip Boosted to filter out boosted items (default 30.0%).
   - Scan for profitable CS2 items.
3. **Browser Mode** 📊:
   - Select an item from 23,000+ CS2 items.
   - Filter by Exterior, Amount, and Currency.
   - View profit percentages and lot details (stickers, charms).
4. **Settings** ⚙️:
   - Adjust Steam commission or theme.
   - Add proxies via `Update Proxy` or rebuild the database with `Update Skins Database`.

## 📸 Screenshots and Logs

### Screenshots 🖼️
Below are placeholders for the main windows of SkinsRadar.

- **Browser Mode**:
  ![Browser Mode](assets/screenshots/browser_mode.png)
  *Explore detailed listings for over 23,000 CS2 items with filters for Exterior, Amount, and Currency.*

- **Radar Mode**:
  ![Radar Mode](assets/screenshots/radar_mode.png)
  *Rapidly scan all CS2 items to find profitable deals with customizable filters.*

- **Settings**:
  ![Settings](assets/screenshots/settings.png)
  *Customize Steam commission, proxy settings, database updates, and app theme.*

### Example Logs 📜
SkinsRadar provides detailed logging for debugging and monitoring. Below are example logs for **Browser Mode** and **Radar Mode**.

#### Browser Mode Logs
```log
2025-07-22 16:16:18,598 - [MainProcess] INFO - Selected random proxy: socks4://98.188.47.150:4145
2025-07-22 16:16:18,599 - [MainProcess] INFO - Request for https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Asiimov%20(Minimal Wear)/render?start=0&count=10&currency=1&format=json
2025-07-22 16:16:20,685 - [MainProcess] INFO - Successful response from https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Asiimov%20(Minimal Wear)/render?start=0&count=10&currency=1&format=json
2025-07-22 16:16:21,462 - [MainProcess] INFO - Request for https://steamcommunity.com/market/itemordershistogram?norender=1&country=NL&language=english&currency=1&item_nameid=176024804&two_factor=0
2025-07-22 16:16:21,462 - [MainProcess] INFO - Successful response for https://steamcommunity.com/market/itemordershistogram?norender=1&country=NL&language=english&currency=1&item_nameid=176024804&two_factor=0
```

#### Radar Mode Logs
```log
2025-07-22 16:16:41,113 - [MainProcess] INFO - Radar Mode started
2025-07-22 16:16:41,125 - [MainProcess] INFO - Selected item: name=AK-47 | Black Laminate (Field-Tested), item_nameid=1321767
2025-07-22 16:16:43,059 - [MainProcess] INFO - Request for https://steamcommunity.com/market/itemordershistogram?norender=1&country=NL&language=english&currency=1&item_nameid=1321767&two_factor=0
2025-07-22 16:16:43,059 - [MainProcess] INFO - Successful response for https://steamcommunity.com/market/itemordershistogram?norender=1&country=NL&language=english&currency=1&item_nameid=1321767&two_factor=0
2025-07-22 16:16:44,230 - [MainProcess] INFO - Request for https://steamcommunity.com/market/listings/730/AK-47 | Black Laminate (Field-Tested)
2025-07-22 16:16:44,230 - [MainProcess] INFO - Successful response for https://steamcommunity.com/market/listings/730/AK-47 | Black Laminate (Field-Tested)
2025-07-22 16:16:44,235 - [MainProcess] INFO - Difference -9.6775590551181% < 5.0% item skipped
2025-07-22 16:16:44,235 - [MainProcess] INFO - Item not added to AutoTable due to filtering
2025-07-22 16:16:45,267 - [MainProcess] INFO - Selected item: name=AK-47 | Black Laminate (Minimal Wear), item_nameid=1321591
2025-07-22 16:16:46,157 - [MainProcess] INFO - Request for https://steamcommunity.com/market/itemordershistogram?norender=1&country=NL&language=english&currency=1&item_nameid=1321591&two_factor=0
2025-07-22 16:16:46,157 - [MainProcess] INFO - Successful response for https://steamcommunity.com/market/itemordershistogram?norender=1&country=NL&language=english&currency=1&item_nameid=1321591&two_factor=0
2025-07-22 16:16:47,282 - [MainProcess] INFO - Request for https://steamcommunity.com/market/listings/730/AK-47 | Black Laminate (Minimal Wear)
2025-07-22 16:16:47,283 - [MainProcess] INFO - Successful response for https://steamcommunity.com/market/listings/730/AK-47 | Black Laminate (Minimal Wear)
2025-07-22 16:16:47,286 - [MainProcess] INFO - Item skipped because boosted
2025-07-22 16:16:47,286 - [MainProcess] INFO - Item not added to AutoTable because it is boosted
2025-07-22 16:16:48,299 - [MainProcess] INFO - Selected item: name=AK-47 | Black Laminate (Well-Worn), item_nameid=1322161
2025-07-22 16:16:48,837 - [MainProcess] INFO - Radar Mode paused
```

## ⚠️ Disclaimer

SkinsRadar has no affiliation with Steam, Valve, or the CS2 developers. It is an independent project created by a third party and is not supported, sponsored, or endorsed by Steam or Valve. Any issues related to Steam or CS2 should be addressed directly to Valve. You are responsible for ensuring that your use of SkinsRadar complies with all applicable laws and regulations. The developer does not encourage or endorse any illegal use of the software.

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

We welcome contributions! 🎉 To get started:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Make your changes and commit (`git commit -m 'Add some AmazingFeature'`).
4. Push to your fork (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📬 Contact

Have questions or suggestions? Reach out via:
- **Email**: [bib.maxim@gmail.com](mailto:bib.maxim@gmail.com)
- **GitHub Issues**: [Create an Issue](https://github.com/Max2772/SkinsRadar/issues)
