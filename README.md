# Recon
Bug Bounty Hunting Recon Script

Gist: Some terrible python code leveraging awesome programs that I use personally for bug bounty recon… I hope to spend time to make it better.

NOTE: This is an active recon – only perform on application you have permission to test. 

Tools leveraged:
- Sublist3r by Ahmed Aboul-Ela (https://github.com/aboul3la/Sublist3r)
- EyeWitness by ChrisTruncer  (https://github.com/ChrisTruncer/EyeWitness)

Usage: 
python PyBrute.py example.com –b –s n --vpn 

Commands:

  --install/--upgrade – Both do the same function – install Sublis3r and EyeWitness (Kali is a prerequisite AFAIK)

  -d – domain you want to perfom recon on

  --vpn – Check if you are on VPN (update with your provider)

  -b – Use Sublis3r’s subrute subdomain brute forcing method

  -s n – List of URL’s include HTTPS and HTTP (HTTPS only by default)
