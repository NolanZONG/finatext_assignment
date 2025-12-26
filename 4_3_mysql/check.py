from scapy.all import rdpcap, Raw
from scapy.layers.inet import TCP

pkts = rdpcap("mysql.pcap")

for p in pkts:
    if p.haslayer(TCP) and p.haslayer(Raw):
        if p[TCP].sport == 3306 or p[TCP].dport == 3306:
            data = p[Raw].load
            try:
                text = data.decode(errors="ignore")
                if "SELECT" in text or "flag" in text.lower():
                    print(text)
            except:
                pass