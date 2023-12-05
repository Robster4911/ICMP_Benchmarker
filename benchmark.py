from scapy.all import *
import time




class Benchmarker():
	def __init__(self, t, r, b, s, o):
		self.targets = t
		self.rate = r
		self.bpp = b
		self.src = s
		self.timeout = o


	def test_target(self, target):
		print(f'Benchmarking target {target}.')
		total_t = 0
		total_b = 0
		dropped = 0
		dummy_bytes = b'\x00' * self.bpp
		for i in range(self.rate):
			packet = IP(dst=target, src=self.src) / ICMP(id=1, seq=i) / Raw(load=dummy_bytes)
			start = time.time()
			response = sr1(packet, timeout=self.timeout, verbose=False)
			if response:
				end = time.time()
				round_trip = end - start
				total_t += round_trip
				total_b += len(packet)
			else:
				dropped += 1
				total_t += self.timeout
		bandwidth = 0
		if total_b != 0:
			bandwidth = (total_b / total_t) / 1000
		latency = total_t / self.rate
		print(f'+--------------+')
		print(f'| Test Results |')
		print(f'+--------------+')
		print(f'target: {target}\nlatency: {latency} s\nbandwidth: {bandwidth} mbps\npackets dropped: {dropped}\n')


	def run(self):
		for target in self.targets:
			self.test_target(target)
		return