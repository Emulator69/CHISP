# CHISP
Cookie History Security Parser

    802.11 being the shared medium that it is allows for an attacker to see 
    everything that passes by within range.  If an attacker were to have the 
    credentials for the WiFi, they could use a tool such as pyDot11 to 
    decrypt on the fly, or wireshark for offline analysis.  They could even
    take it a step further and capture the EAPOL and use aircrack-ng to attempt
    brute-forcing the key for without prior knowledge.
    
    After analysis has occured, the attacker would be left with a list of the
    victim's cookies in addition to whatever else the pcap may reveal.
    Depending on the cookie configuration, the attacke might have access to a 
    cookie that provides a token, gaining access to an https website.
    
    A surprising number of websites use HTTPS, but fail to implement the Secure
    or HTTP Only flags on the cookies they set for their users. This mistake
    can prove fatal.  It is up to System Administrators to ensure the systems
    they run are secure as best as they can be.  Something as trivial as the
    Secure Flag should never be discovered during a Penetration Test, 
    yet time after time this occurs.
    
    The idea behind this tool is simple; login/surf all sites for a given
    organization.  After you accomplished that simple step, you're done.  The
    tool does the rest.  This can be extremly ideal for large organizations
    where the Blue Team is responsible for ensuring that 1000s of domains are
    secure across the board.
    
    As of right now, this tool is very beta, there are a lot of checks and
    balances that need to occur.  As well, I'm planning on adding in the
    HTTPonly checks and Firefox support down the road.
    
    It works like this:
        - Make 2 lists of cookies, those with and without the Secure flag
        - Make 2 lists of URL history, http and https
        - Compare and contrast the cookies without the secure flag, to the list
        of domains that have https.
            - Take into account subdomains
            - Take into account mixed usage
                - http and https on the site depending on the subdomain or view
                - Secure and Non-Secure cookies
        - Voila, you now have a list of potential vulerable sites to look
        further into for deeper examination security wise

    How to use:
        - Depends on OS and browser
        - Linux
            - Chrome
                - ~/.config/google-chrome/Default/Cookies
                - ~/.config/google-chrome/Default/History
            - Chromium
                - ~/.config/chromium/Default/Cookies
                - ~/.config/chromium/Default/History
        - Windows
            - Chrome
                - %APPDATA%\AppData\Local\Google\Chrome\User Data\Default\Cookies
                - %APPDATA%\AppData\Local\Google\Chrome\User Data\Default\History

        - ./chisp <Cookie File> <History File>
