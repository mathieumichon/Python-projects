================
=== TCP_chat ===
================

This project exploits the flaw within the IP protocol and its IPID parameter which is supposed to be randomly generated.
Here scapy allows us to edit the IPID of the packages we create, so we will be able to use ASCII code to send a message through multiple packets.

Some explainations:
In both program codes, you might not understand the utility of some variables ("previous_id" ?), so let me give you some details.
Like I just said each message is sent through multiple packets, sending one character of the message each.

For instance, let's say we want to send the message "hi"
So "hi" contains two characters, which means we'll have to send two packets, one for the "h" character and another one for the "i" character.

Here's what we get when we transform those two characters into ASCII code for our IPID's:
	h = 104
	i = 105

Now we add one more character to notice the sniffer when it has recieved the last character of the message:
	h = 1041
	i = 1050

	'1' means there's other characters needed to complete the message
	'0' means that we recieved the last character and we can now display the message

Okay now we have our packets IPID's, but we know that we can not send multiple packets with the same IPID.
In case we wanted to send "hello" we would have two packets with the IPID "1080" (ASCII code of 'l' = 108) due to presence of two 'l' character in the word "hello".

So we choose to add the sum of the previous IPID's to each new packet, which gives us:
	h = 1041 (no previous IPID)
	i = 2090 (104 + 105 = 209)

	And then, in order to find the character we just recieved, we only have to substract the previous IPID to the current one:
	209 - 104 = 105 -> i

	Note that we do not include the last character of the IPID to our addition/substraction since it only serves us as an information for the program and not the calculation.
