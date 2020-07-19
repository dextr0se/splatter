# splatter
XML to HTML Generator for Note/Code Snippet Quick Reference
Splatter your code everywhere

## Summary
Put code or other interesting things that you would like to organize for ease of copy splatting in an xml file with the tags specified below.  When you are finished entering your data into the xml file, execute the python script and walah... an HTML file with collapsible buttons is auto-generated.

The xml has 5 tags:<br />
&nbsp;&nbsp;``<root>`` starts and ends the xml file.<br />
&nbsp;&nbsp;&nbsp;&nbsp;``<subject>`` Left-side Toggle Menu Title<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``<section>`` Left-side toggle menu subitem and non-collapsible section header on right side<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``<content-title>`` Collapsible title button in main window``</content-title``<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``<content>`` Text that will be placed into a small code box.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any line that begins with a # will be a different color (like a comment)``</content>``<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``</section>``<br />
&nbsp;&nbsp;&nbsp;&nbsp;``</subject>``<br />
&nbsp;&nbsp;``<\root>``<br />

## Dependencies
The CSS, JS, XML and FILES directories must be in the same directory as the splatter.html generated file.
If you choose to uncomment the script src and use the internet versions of bootstrap and jquery, it may do weird things.

## Known Issues
  * Don't name subjects or sections the same name The collapse feature will cease to work for that section or subject<br />
  * Don't put any special characters or whitespace in the subject or section It will also break the collapse feature<br />

## Screenshot 1
![ScreenShot1](https://github.com/dextr0se/splatter/raw/master/images/screenshot1.png "Screen Shot 1")
## Screenshot 2
![ScreenShot2](https://github.com/dextr0se/splatter/raw/master/images/screenshot2.png "Screen Shot 2")
