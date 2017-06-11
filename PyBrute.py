import argparse, os, sys, requests, webbrowser, socket, time, csv
from urlparse import urlparse
import datetime

today = datetime.date.today()

__author__ = 'Caleb Kinney'

global url, secure

def get_args():
    parser = argparse.ArgumentParser(
        description='PyBrute')
    parser.add_argument(
        '-d', '--domain', type=str, help='Domain', required=False, default=False)
    parser.add_argument(
        '-s', '--secure', help='Secure', nargs='?', required=False, default=False)
    parser.add_argument(
        '-b', '--bruteforce', help='Bruceforce', nargs='?', default=False)
    parser.add_argument(
        '--upgrade', help='Upgrade', nargs='?', default=False)
    parser.add_argument(
        '--install', help='Install', nargs='?', default=False)
    parser.add_argument(
        '--vpn', help='VPN Check', nargs='?', default=False)

    #return url, secure
    return parser.parse_args()

#url, secure, bruteforce = get_args()

newpath = r'Output/PyBrute'
if not os.path.exists(newpath):
    os.makedirs(newpath)


def banner():
    print("\033[1;31m__________        __________                __     ")
    print("\033[1;31m\______   \___.__.\______   \_______ __ ___/  |_  ____")
    print("\033[1;31m |     ___<   |  | |    |  _/\_  __ \  |  \   __\/ __ \ ")
    print("\033[1;31m |    |    \___  | |    |   \ |  | \/  |  /|  | \  ___/")
    print("\033[1;31m |____|    / ____| |______  / |__|  |____/ |__|  \___  >")
    print("\033[1;31m           \/             \/                         \/ ")


def sublist3r():
    if vpn is not False:
        vpncheck()
    hostnameFile = domain.replace('.', '_')
    rootdomain = domain
    DNSfilename = ("Output/PyBrute/" + hostnameFile + "_sublist3r.txt")
    if bruteforce is not False:
        Subcmd = (("python bin/Sublist3r/sublist3r.py -v -b -t 15 -d %s -o " + DNSfilename) % (rootdomain))
    else:
        Subcmd = (("python bin/Sublist3r/sublist3r.py -v -t 15 -d %s -o " + DNSfilename) % (rootdomain))
    print("\n\033[1;31mRunning Command: \033[1;37m" + Subcmd)
    os.system(Subcmd)
    time.sleep(2)
    with open(DNSfilename) as f:
        SubHosts = f.read().splitlines()
    f.close()
    time.sleep(2)
    f1 = open(DNSfilename, "w")
    for dnsip in SubHosts:
        dnsip = "".join(dnsip)
        f1.writelines("https://%s\n" % dnsip)
        if secure is not False:
            f1.writelines("http://%s\n" % dnsip)
    f1.close()
    time.sleep(1)
    eyewitness(DNSfilename)

def eyewitness(filename):

    rootdomain = domain
    EWHTTPScriptIPS = (
    "python bin/EyeWitness/EyeWitness.py -f " + filename + " --active-scan --no-prompt --headless  -d " + "Output/PyBrute/"+ rootdomain + "-" + time.strftime('%m-%d-%y-%H-%M') + "-Sublist3r-EW ")
    if vpn is not False:
        print("\n\033[1;31mIf not connected to VPN manually run the following command on reconnect:\n\033[1;37m" + EWHTTPScriptIPS)
        vpncheck()
        print("\n\033[1;31mRunning Command: \033[1;37m" + EWHTTPScriptIPS)
        os.system(EWHTTPScriptIPS)
    print("\a")

def upgradeFiles():
    binpath = r'bin'
    if not os.path.exists(binpath):
       os.makedirs(binpath)
    else:
        os.system("rm -r bin")
        os.makedirs(binpath)
    sublist3rUpgrade = ("git clone https://github.com/aboul3la/Sublist3r.git ./bin/Sublist3r")
    print("\n\033[1;31mRunning Command: \033[1;37m" + sublist3rUpgrade)
    os.system(sublist3rUpgrade)
    subInstallReq = ("sudo pip install -r bin/Sublist3r/requirements.txt")
    print("\n\033[1;31mRunning Command: \033[1;37m" + subInstallReq)
    os.system(subInstallReq)
    eyeWitnessUpgrade = ("git clone https://github.com/ChrisTruncer/EyeWitness.git ./bin/EyeWitness")
    print("\n\033[1;31mRunning Command: \033[1;37m" + eyeWitnessUpgrade)
    os.system(eyeWitnessUpgrade)
    print("Sublis3r Installed")
    eyeInstallReq = ("sudo bash bin/EyeWitness/setup/setup.sh")
    print("\n\033[1;31mRunning Command: \033[1;37m" + eyeInstallReq)
    os.system(eyeInstallReq)
    cpphantomjs = ("cp phantomjs bin/EyeWitness/bin/")
    print("\n\033[1;31mRunning Command: \033[1;37m" + cpphantomjs)
    os.system(cpphantomjs)
    movephantomjs = ("mv phantomjs bin/")
    print("\n\033[1;31mRunning Command: \033[1;37m" + movephantomjs)
    os.system(movephantomjs)
    print("EyeWitness Installed")

def vpncheck():
    vpnck = requests.get('http://ipinfo.io')
    # Change "Comcast" to your provider or City")
    if "Comcast" in vpnck.content:
        print("\n\033[1;31mNot connected via VPN \033[1;37m")
        print("\n" + vpnck.content)
        quit()
    else:
        print("\n\033[1;31mConnected via VPN \033[1;37m")
        print("\n" + vpnck.content)
        time.sleep(5)

if __name__ == "__main__":
    banner()
    args = get_args()
    domain = args.domain
    secure = args.secure
    bruteforce = args.bruteforce
    upgrade = args.upgrade
    install = args.install
    vpn = args.vpn
    if upgrade is not False:
        upgradeFiles()
    if install is not False:
        upgradeFiles()
    if domain is not False:
        sublist3r()
    print("Done!")


