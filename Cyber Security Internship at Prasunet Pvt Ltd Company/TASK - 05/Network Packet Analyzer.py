from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"\n[+] New Packet: {ip_layer.src} -> {ip_layer.dst}")

        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"Protocol: TCP")
            print(f"Source Port: {tcp_layer.sport}, Destination Port: {tcp_layer.dport}")

        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"Protocol: UDP")
            print(f"Source Port: {udp_layer.sport}, Destination Port: {udp_layer.dport}")

        if Raw in packet:
            print(f"Payload: {packet[Raw].load}")

def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
