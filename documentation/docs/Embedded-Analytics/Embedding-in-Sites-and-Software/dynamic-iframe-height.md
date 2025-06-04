---
stoplight-id: nt3co7oh36g5s
---

# Dynamic Iframe Height

Setting the iframe height larger than the height of embedded dashboard is important to avoid scroll traps on mobile and double scroll bars on desktop. This is done by listening for the rendered height and setting the iframe container dynamically. Many embed customers choose to add a few more extra pixels to the height just to be sure the content is not pushed into a scrollable state. Here are two examples for how this can be done whether you have a single iframe or multiple iframes on the same page, as documented <a href="https://stackoverflow.com/questions/15329710/postmessage-source-iframe" rel="noopener" target="_blank">here</a>.

## Single and Multiple iframe Examples
---

Use the following Dynamic iframe height code examples to help avoid scroll traps:

### **Single iframe:**
```html
<html>
  <head>   
    <script>
        window.addEventListener("message", receiveMessage, false);
        function receiveMessage(event) {
          //if we get some data back
          if (event.data && event.data.params && event.data.params.height) document.getElementById("iframe1").style.height = event.data.params.height;
        }   
    </script>
  </head>
  <body>   
        <iframe id="iframe1" src="https://public.domo.com/embed/pages/abcde" width="100%" height="1620" marginheight="0" marginwidth="0" frameborder="0"></iframe>
  </body>
</html>
```

### **Multiple iframes:**
(loop through the responses and determine which came from which source. Add a couple additional px to the height in order to take into account scroll bars that could just barely push things into a scrollable state)

```html
<html>
   <head>
      <script>
         window.addEventListener("message", receiveMessage, false);
             function receiveMessage(event) {
                var frames = document.getElementsByTagName('iframe');
                for (var i =0; i <frames.length; i++) {
                   //loop through the responses and determine which came from which source
                    if (frames[i].contentWindow === event.source) {
                    if (event.data && event.data.params && event.data.params.height) frames[i].style.height = event.data.params.height + 15;
                     }
               }
        }
      </script>
</head>
   <body>
      <iframe id="iframe1" src="https://public.domo.com/embed/pages/abcde"width="100%" height="1620" marginheight="0" marginwidth="0" frameborder="0"></iframe>
       <iframe id="iframe2" src="https://public.domo.com/embed/pages/fghij"width="100%" height="1620" marginheight="0" marginwidth="0" frameborder="0"></iframe>
   </body>
</html>

```


