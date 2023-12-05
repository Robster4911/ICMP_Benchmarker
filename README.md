# ICMP_Benchmarker
This tool was written as part of a larger project in my Computer Networks course to setup and test different aspects of a Software Defined Network.

## How it works and stuff
This tool uses ICMP echo requests to calculate both latency and bandwidth. 
It is very portable, and the only unique setup required is configuring the config.json with proper addresses.

It will run benchmark tests on every address in the `targets` array, so when configured properly on every node in the network you should be able to get latency and bandwidth of every edge of the network topology.

## Notes
- Make sure that you set src to be the correct IP address of the node running the test, otherwise the ICMP echos will never be sent back to the proper address.
- Since this uses scapy rather than normal network sockets, don't bother trying to get loopback to work. Scapy is real weird with loopback addresses. Its only in the config file on this repo as a placeholder.
