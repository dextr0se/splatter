# splatter
copy splat code reference generator

## summary
Put code or other interesting things that you would like to organize for ease of copy splatting in an xml file with the tags specified below.  When you are finished entering your data into the xml file, execute the python script and walah... an HTML file with collapsible buttons is auto-generated.

The xml has 5 tags:<br />
&nbsp;&nbsp;``<root>`` starts and ends the xml file.<br />
&nbsp;&nbsp;&nbsp;&nbsp;``<subject>`` first collapsible button.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``<section>`` sub-collapsible button.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``<content-title>`` Plain text to title your section within the section tag.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``<content>`` Text that will be placed into a small code box. Any line that begins with a # will be a different color (like a comment)<br />
 
