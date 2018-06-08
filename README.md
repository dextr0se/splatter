# splatter
HTML Generator for Note/Code Snippet References

## Summary
Put code or other interesting things that you would like to organize for ease of copy splatting in an xml file with the tags specified below.  When you are finished entering your data into the xml file, execute the python script and walah... an HTML file with collapsible buttons is auto-generated.

The xml has 5 tags:<br />
&nbsp;&nbsp;``<root>`` starts and ends the xml file.<br />
&nbsp;&nbsp;&nbsp;&nbsp;``<subject>`` first collapsible button.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``<section>`` sub-collapsible button.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``<content-title>`` Plain text to title your section within the section tag.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``<content>`` Text that will be placed into a small code box. Any line that begins with a # will be a different color (like a comment)<br />
 
## CSS JavaScript Browsers
Has been tested on the following browser versions
  * CHROME Version 67.0.3396.62 (Official Build) (64-bit)<br />
  * FIREFOX 60.0.1 (64-bit)<br />
  * INTERNET EXPLORER 11.48.17134.0<br />

Download the javascript and css files.
If you choose to uncomment the script src and use the internet versions of bootstrap and jquery, it may or may not work

## Known Issues
  * Don't name subjects or sections the same name The collapse feature will cease to work for that section or subject<br />
  * Don't put any special characters or whitespace in the subject or section It will also break the collapse feature<br />

## Screenshot 1
![ScreenShot1](https://github.com/dextr0se/splatter/raw/master/images/screenshot1.png "Screen Shot 1")
## Screenshot 2
![ScreenShot2](https://github.com/dextr0se/splatter/raw/master/images/screenshot2.png "Screen Shot 2")
