
---

# ☁️ Discord Username Checker

**Checker** is a robust tool for checking the availability of Discord usernames.  
**gen** is a simple helper for generating lists of random usernames to check.

---

## 🛠️ Main Components

### 🔎 checker (**main tool**)
- Checks username availability on Discord.
- Supports proxies, logging, multithreading, and webhook notifications.
- Reads username lists from `data/names_to_check.txt`.
- Saves available usernames to `results/hits.txt`.

### 🧩 gen (**helper tool**)
- Generates random usernames (letters, digits, `_`).
- Lets you choose username length and count.
- Saves to `data/names_to_check.txt` for checker to use.

---

## 🚀 Getting Started

1. **Generate usernames**  
   Run the generator to create a list of usernames:
   ```
   python usernamegen.py
   ```
   - Choose username length (e.g., 3, 4, 5).
   - Choose how many to generate.
   - Output: `data/names_to_check.txt`

2. **Check usernames**  
   Run the checker to test availability:
   ```
   python main.py
   ```
   - Supports proxies and webhooks (see prompts).
   - Results: `results/hits.txt`

---

## 📂 File Structure

```
project/
├── main.py            # Checker - main tool
├── usernamegen.py     # Username generator - helper tool
├── data/
│   └── names_to_check.txt   # List of usernames to check
├── results/
│   └── hits.txt            # Available usernames found
├── logs/
│   └── log.txt
│   └── error.txt
└── data/
    └── proxies.txt         # (Optional) List of proxies
    └── config.json         # Tool configuration
```

---

## 💡 Usage Tips

- **checker** is the main tool. Always run it after preparing your username list.
- Use **gen** only to create or refresh `names_to_check.txt`.
- You can also manually edit `names_to_check.txt` if you want to check specific usernames.
- For best results, use proxies to avoid rate limits.
- Webhook support lets you get instant notifications for available usernames.

---

## 📝 Example Workflow

1. Generate 4-letter usernames:
   ```
   python usernamegen.py
   ```
2. Check which are available:
   ```
   python main.py
   ```

---

## 📢 Credits

- Main checker by [Balram-1](https://github.com/Balram-1)
- Generator helper script inspired by community tools

---

**Happy checking!** 🚀

