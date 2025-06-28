💌 Monday Motivation Mailer

Every great week starts with a spark — a quote, a thought, or a moment of inspiration. This project is a simple yet impactful Python automation that sends one **random motivational quote** from a curated list of 100 to your email inbox every **Saturday** (you can change it to Monday too)!

> **“Don't brood. Get on with living and loving. You don't have forever.”** – Leo Buscaglia  
> _(One of the quotes you might receive!)_



🚀 Project Overview

This Python script:
- Reads quotes from a `quotes.txt` file
- Picks one random quote
- Sends it via email automatically using Gmail's SMTP service
- Triggered based on day of the week (currently Saturday)

🔐 How It Works

- Uses `smtplib` for sending emails
- Uses Gmail App Password (secure)
- Quotes stored in plain text, one per line
- Runs conditionally based on `datetime.weekday()` (5 = Saturday)

📸 Screenshot

![image](https://github.com/user-attachments/assets/a078e389-fe1d-4716-bb44-dd2ccbc0de39)
![image](https://github.com/user-attachments/assets/21ee40a4-7ad1-4012-b1e6-0973af086ce0)
![image](https://github.com/user-attachments/assets/d3a80939-3048-49e2-a5c6-66e8270d49b1)

🧠 Why I Built This

In the fast-paced world of deadlines and distractions, I wanted to build something small but joyful — a moment of motivation that lands in your inbox without you even asking.  
Built using **pure Python**, this is a reminder that even simple scripts can spark big smiles. 😊

🛠️ Tech Used

- Python 3
- smtplib
- datetime
- random

---

🔐 Security Note

This script uses a Gmail App Password — make sure you:
- Enable 2FA in Gmail
- Use an app password instead of your regular password
- Keep `quotes.txt` clean and inspiring 😉
