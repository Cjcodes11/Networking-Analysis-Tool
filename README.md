# Lynis Security Audit Lab

### Overview
Lynis is a free tool that is designed to check a Linux or MacOS system for security vulnerabilities. It runs many tests and gives the system a hardening index, a score from 0 to 100. 

## Step 1:
On Kali:

<img width="544" height="106" alt="Screenshot 2026-11-13 at 7 17 38 PM" src="https://github.com/user-attachments/assets/71854d6c-cdcd-4f5f-81bb-d787b7d5ce21" />

I check to see that it works:

<img width="540" height="84" alt="Screenshot 2026-11-13 at 7 18 15 PM" src="https://github.com/user-attachments/assets/52988997-af9b-4984-94f0-df27a63744bb" />

## Step 2:
I start the audit

<img width="545" height="81" alt="Screenshot 2026-11-13 at 7 18 42 PM" src="https://github.com/user-attachments/assets/70df0af2-7390-4118-b8cb-e360e5a399aa" />

## Step 3:
With guidance using Claude AI, I write a beginner python script and I call it lynis_summary.py. 
I used Claude to generate the Python script, then built the virtual machine, ran the audit myself, tested the script on my own Dell Latitude system, and can explain what each part does.


<img width="545" height="389" alt="Screenshot 2026-11-13 at 7 38 00 PM" src="https://github.com/user-attachments/assets/bc23d8b4-6315-43f4-bfbb-15c8baa89d45" />



## Step 4:
The report file belongs to root, so the script needs sudo:


<img width="540" height="85" alt="Screenshot 2026-11-13 at 7 21 24 PM" src="https://github.com/user-attachments/assets/b4c239d9-a785-4227-a91d-05490f888b51" />

## What I Learned
I ran my first lynis audit system in Kali Linux
I installed my first virtual machine in virtual Box
A few lines of Python can turn that text into a report
I can save my python file and place it directly into the terminal
