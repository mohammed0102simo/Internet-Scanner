# 🌍 Async IP & Port Scanner

A simple asynchronous Python port scanner that reads IP ranges from a JSON file, generates random IPs, scans common ports, and saves discovered targets to a file.

---

## ⚙️ Features

- 🚀 Asynchronous scanning using `asyncio`
- 🔁 Concurrency control with Semaphore
- 🎯 Random IP generation inside ranges
- 📦 Scans common exposed ports (SSH, FTP, HTTP, RDP, MySQL, etc.)
- 📝 Saves results automatically to `targets.txt`

---

## 📂 Project Structure

```
.
├── Ipgen.py
├── json.json
├── targets.txt
└── README.md
```

---

## 📜 Requirements

- Python 3.10+
- No external libraries required (only standard library)

---

## 🚀 Usage

Run the script:

```bash
python main.py
```

After the scan finishes, results will be saved in:

```
targets.txt
```

Format example:

```
192.168.1.10:22        StateEU
```

---

## 🔧 Configuration

You can change:

### Concurrency limit:
```python
MAX_CONCURRENT = 200
```

### Ports to scan:
```python
PORTS = [...]
```

---

## ⚠️ Disclaimer

This tool is intended for:

- Educational purposes  
- Testing networks you own  
- Authorized security research  

⚠️ Do NOT scan networks without permission. Unauthorized scanning may be illegal.

---

## 👨‍💻 Author

Created with Python & asyncio.
