HtmlizeBibtex
=============

**HtmlizeBibtex** is made up of the following scripts:

 * *bibtex2html.py*: Formats Bibtex content into HTML (avoiding tables).
 * *htmlizeBibtex.js*: Generates labels for inline citations. When those labels are clicked a dialog appears/disappears. This dialog contains the referred citation in a readable format .


## Citations on your HTML

These are generic instructions to use citations inside your html file. You can find an example in the *index.html* file.

### CSS
Add the CSS in the &lt;head&gt; tag.

    <link rel="stylesheet" href="css/htmlizeBibtex.css" />
    <link rel="stylesheet" href="css/ui-lightness/jquery-ui-1.9.2.custom.min.css" />

### JavaScript
Add the JavaScript files in the &lt;head&gt; tag.

    <script type="text/javascript" src="js/htmlizeBibtex.js"></script>
    <script type="text/javascript" src="js/jquery-1.8.3.min.js"></script>
    <script type="text/javascript" src="js/jquery-ui-1.9.2.custom.min.js"></script>
  
### HTML
Wherever you want to cite in your html file, use the citation id as it appears in the bibtex file.

    ... and here it comes a citation <span class="cite">{citation_id}</span>. Blah blah...

And add this once as a child of the &lt;body&gt; tag.

    <div id="citations">
    </div>


## Generate cites
Execute the following command:

    python bibtex2html.py [path/to/bibtex-file] [path/to/html-with-citations]


## Dependencies

 * [bibtex2html](http://www.lri.fr/~filliatr/bibtex2html/)
 * [jQuery](http://jquery.com/)
 * [jQueryUI](http://jqueryui.com/)
 * [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)