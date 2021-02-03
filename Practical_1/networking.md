## Name resolution and Routing

### Exercise: show that every IPv4 can be represented by four 8bit unsigned integers, and that every 8bit unsigned integer is between 0 and 255.

IPv4 uses a 32-bit address space or 2^32. We can split it into 2^8 * 2^8 * 2^8 * 2^8. 8bit unsigned integers are between 00000000 (which is 0) and 11111111 (which is 255).


### Exercise: how many IPv4 addresses are there? Is it enough? Explain.

IPv4 addresses have the size of 2^32, so it limits the address space to 4294967296 addresses. It is enough as long as we do not need more unique identifiers (subnets can provide some extension). The IoT growth is one of the reason to expand the limit, e.g. with the use of IPv6.


### Exercise: use ping in a terminal to resolve a domain name. Copy-paste the command you used, and the result.

~\ $ ping -c 5 sports.ru

PING sports.ru (37.209.240.8) 56(84) bytes of data.

64 bytes from 37.209.240.8 (37.209.240.8): icmp_seq=1 ttl=57 time=5.21 ms

64 bytes from 37.209.240.8 (37.209.240.8): icmp_seq=2 ttl=57 time=4.74 ms

64 bytes from 37.209.240.8 (37.209.240.8): icmp_seq=3 ttl=57 time=5.92 ms

64 bytes from 37.209.240.8 (37.209.240.8): icmp_seq=4 ttl=57 time=6.58 ms

64 bytes from 37.209.240.8 (37.209.240.8): icmp_seq=5 ttl=57 time=4.95 ms

--- sports.ru ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 4021ms

rtt min/avg/max/mdev = 4.736/5.479/6.577/0.679 ms


## Bandwidth, latency, reliability

### Exercise: The Multipath TCP project aims to allow TCP packets to be split across multiple network links and reassembled at the destination. For example, if you were uploading a 100 megabyte file to a server from your phone, it would allow you to send 75 megabytes by WiFi and 25 megabytes by cellular automatically. How should the ratio be chosen if you want to minimise transmission time? Minimise cellular bandwidth use? Explain.

The ratio should be based on the ratio between WiFi bandwidth and cellular bandwidth in order to keep up with the number of TCP rounds that cellular path can complete before WiFi path does if they start simultaneously.

### Exercise: UDP is popular for streaming media; explain why.

Streaming process tolerates a little amount of lost data. UDP requires fewer resources, thus more popular.

### Exercise: Read the Wikipedia articles on multicast and anycast routing. Why is anycast good for content delivery networks, and why is multicast good for live-streaming? What are some other uses for these?

**Anycast networks** are widely used for CDN because they allow to use the most suitable route at a given moment. It is mostly used for static content such as images or style sheets, so anycast networks allow multiple end-users to follow multiple and more efficient routing paths to it.

**Multicast** is good for live-streaming because it uses network infrastructure efficiently by requiring the source to send a packet only once. If there is a large number of receivers, the responsible parts of the network will replicate the packet to reach multiple receivers only when necessary. Scaling will not require any prior knowledge of who or how many receivers there are.
