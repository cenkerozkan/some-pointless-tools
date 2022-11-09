import os

# I use manjaro linux on my laptop.
# There is a driver called "intel p_state"
# which is responsible from setting 
# clock speeds of the cpu, but it doesn't work
# as intended on my laptop for no reason I found so far.
# So this tiny python script activates the performance 
# mode then switches back to powersave mode to 
# set the right clock speed limits for my CPU (Intel i5 9300H 800MHz - 4.10Ghz)

if __name__ == "__main__":
	os.system("sudo cpupower frequency-set --governor performance")
	print("Performance mode.\n")
	os.system("cpupower frequency-info")

	os.system("sudo cpupower frequency-set --governor powersave")
	print("Powersave mode.\n")
	os.system("cpupower frequency-info")

	# CPU coniditons
	#os.system("watch cpupower frequency-info")