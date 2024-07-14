Network Packet Analyzer
Develop a packet sniffer tool that captures and analyzes network packets. Display relevant information such as source and destination IP addresses, protocols, and payload data. Ensure the ethical use of the tool for educational purposes.

Explanation:
packet_callback Function:

This function is called whenever a packet is captured.
Checks if the packet has an IP layer.
Extracts and prints the source and destination IP addresses.
Checks for TCP or UDP protocols and extracts relevant information like source and destination ports.
If the packet contains raw data (payload), it prints the payload.
main Function:

Starts the packet sniffer with the sniff function, which captures packets and calls packet_callback for each captured packet.
store=0 ensures packets are not stored in memory, preventing memory overflow.
Usage:
To use this program, run it with administrator/root privileges because capturing network packets usually requires elevated permissions. For example, on Unix-based systems, use: