from benchmark import Benchmarker
import json




def main():
	# Setup config
	config = {}
	with open("config.json") as config_file:
		config = json.load(config_file)
		config_file.close()

	bm = Benchmarker(config["targets"], config["rate"], config["bpp"], config["src"], config["timeout"])
	bm.run()




if __name__ == "__main__":
	main()
