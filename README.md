# 🐕‍🦺 DorkHound - Google Dorking OSINT Tool by MusicNerd23

**DorkHound** is a powerful, menu-driven OSINT (Open Source Intelligence) tool that automates **Google Dorking** to uncover publicly available data. Designed for **ethical hackers, cybersecurity professionals, and OSINT researchers**, DorkHound streamlines intelligence gathering by categorizing and automating Google search queries.

## 🔥 Features
- **Menu-Based Search** – Choose from categorized Google dorks (People Search, Files, Security, etc.)
- **Custom Dorking** – Enter and automate your own Google dork queries
- **Fast & Automated** – Fetches top results quickly with minimal effort
- **Export Results** – Save findings for later analysis
- **100% Legal** – Uses Google Search, no scraping or violations of Terms of Service

## 🚀 Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/DorkHound.git
cd DorkHound
```
### **2. Install Dependencies**
```bash
pip install googlesearch-python
```

## 🛠 Usage
Run the tool using:
```bash
python dorkhound.py
```
You'll be presented with a **menu** to select **OSINT categories** like:
1. **People Search** (Facebook, LinkedIn, etc.)
2. **Files & Documents** (Exposed PDFs, Google Drive Docs, etc.)
3. **Website Security** (SQL Injection vulnerable sites, open directories, admin panels)
4. **Custom Dork Search**

Once a dork is selected, enter a **search term** (e.g., a name, keyword, or domain), and DorkHound will **fetch and display** the top results.

### **Example Search**
```
[?] Choose a category: 1 (People Search)
[?] Choose a dork: 2 (Find Public Facebook Posts)
[?] Enter search term: "John Doe"
```
DorkHound will return **Google search results** matching the query.

## 📂 Saving Results
You can **save the search results** by selecting `y` when prompted:
```
[?] Save results? (y/n): y
[+] Results saved to google_dork_results_1712345678.txt
```

## ⚖️ Legal Disclaimer
DorkHound is intended **for ethical and legal OSINT research only**. It does not bypass any security measures, and **misuse is strictly prohibited**. The developers are **not responsible for any unethical or illegal use**.

## 🌟 Contributing
Want to add more Google dorks or improve the tool? Contributions are welcome!
1. **Fork the repo**
2. **Create a feature branch** (`git checkout -b feature-new-dork`)
3. **Commit your changes** (`git commit -m "Added new Google Dork for X"`)
4. **Push to GitHub** (`git push origin feature-new-dork`)
5. **Submit a pull request**

## 📜 License
This project is licensed under the **MIT License**.

---
**Find what others miss, the legal way!** 🕵️‍♂️

