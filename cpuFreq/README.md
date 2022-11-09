# About
**WARNING: Be careful while using os.system function in python, It might be harmful if you don't know what you are dealing with.**


I am using manjaro linux on my laptop. The 'intel p_state' driver, which is responsible for adjusting the clock speed of intel processors, is running in the linux kernel.

But for some reason I don't know yet, this driver is not working properly on my computer. It turns off the turbo boost feature by itself and sets the maximum clock speed to 2.40 GHz (Which normally should be 4.10Ghz max) and does not allow it to go higher.

This script, on the other hand, is a small tool that I write to automate the work I do by hand, called by the operating system every time I turn on the computer, and pulls the processor mode first to performance and then to power saving mode.


- ![image](https://user-images.githubusercontent.com/68559468/200822779-da3156ad-5897-442c-abda-9891d2c76246.png)
- ![image](https://user-images.githubusercontent.com/68559468/200822996-be44dcf9-88fd-4945-a736-6eacbdbad8d1.png)
