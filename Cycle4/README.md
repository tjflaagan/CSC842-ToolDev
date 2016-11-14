# MSF Web 1
## General Information
* Author: Tyler Flaagan
* Date: 11/13/16
* Description: This small web app using Node runs and connects to msfrpcd (msfconsole) to allow the user to connect using the web. This way the user doesn't even need a MSF client installed on their machine to connect.


## Use Case and Background Info


The tools available for pen testers and red teamers to connect to MSF are often found to be lacking in certain areas and sometimes expensive. I want to build a tool that can use MSF without having to install any type of client on the machine and that brings more functionality onto the same page. Some of the features I would like to add include:
Mapping of compromised hosts from netstat and arp data
	I have written custom Maltego transforms for this and would like to transfer that type of view to the web so it is all in the same application and doesn't depend on third party licensed software like Maltego.
Data collection
	I would like to be able to integrate this with a tool that allows you to keep data (notes, hosts compromised and details about them, credentials, other useful info, etc) within the same web app in a secure fashion. 
I'm sure if I continue working on this project that there will be scope creep far beyond what I have listed. 


To set up and run the app, perform the following:

1. Install npm and node.
2. Make sure that the dependencies found in packages.json are installed

`> npm install <dependency>`

3. Make sure that msfrpcd is running.

`> node server.js`



## Resources

https://github.com/creationix/nvm/blob/master/README.markdown#install-script
https://www.airpair.com/javascript/node-js-tutorial
https://help.rapid7.com/metasploit/Content/api-rpc/getting-started-api.html
https://github.com/eviltik/msfnode/blob/master/README.md
And a few others along the way*
