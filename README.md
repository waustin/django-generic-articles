Django Generic Articles
=======================
A simple abstract model for article type content.
On many projects I find myself needing a content type that has a title, publish date, publish status, excerpt, and description.
I created this app to store this informaiton in abstract model so I could create new models faster.

The app also contains: 

* A Manager class that filters object by publish status.
* An Admin class with an action for toggling the publish status.
* An Admin Form that adds an 'mceEditor' class to the description field for hooking in a TinyMCE editor.
