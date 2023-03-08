# Markdown (H1)

## Testing markdown syntax to html (H2)

**This text should be bold**. (Uses double asterisks)
__This text should also be bold__. (Uses double underscores)
*This is Italic*. (Uses single asterisks)

### Blockquotes below (H3)

> This is a test for blockquotes.

> 

> This is what a blockquote looks like after a line break.

>Can we nest blockquotes?

>>yes we can!

**Edit**

Apparently we cannot add block quotes.

The markdown documentation states that we can but apparently it is not working.

[1]: https://www.markdownguide.org/basic-syntax/#blockquotes-1

> - We can add list items on it too!

> 1. They

>> 2. Can

>>> 3. Be

>>>> 4. Ordered!

>Block codes can also be added as such

    def index(request):

    return render(request, "encyclopedia/index.html", {

        "entries": util.list_entries()

    })