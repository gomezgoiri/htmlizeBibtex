import os
import argparse
from BeautifulSoup import BeautifulSoup

        
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description="Generates two files with the formated citations.")
    parser.add_argument("bibfname", metavar="bibfname", type=str, help="an string with the filename of the *.bib")
    parser.add_argument("-f", dest="htmlfname", default=None, help="an string with the filename of the *.html where the output HTML snipet will be inserted.")
    parser.add_argument("-s", dest="style", default=None, help="BibTeX style (plain, alpha, ...)")
    args = parser.parse_args()
    
    
    if not os.path.isfile(args.bibfname):
      raise Exception("Such Bibtex file does not exist.")
    
    
    # Generate HTML files from Bibtex    
    optional_style = " " if args.style is None else (" -s %s "%(args.style))
    os.system( "bibtex2html%s%s > /dev/null 2>&1"%(optional_style, args.bibfname) )
    
    fname =  args.bibfname.split('/')[-1].split(".")[0]
    
    # Parse HTML to extract the citations and their ids
    with open("%s.html"%(fname), "r") as fhtml_tables:
      pool = BeautifulSoup(fhtml_tables.read())
      
      keys = pool.findAll("td", {"class":"bibtexnumber"})
      names = pool.findAll("td", {"class":"bibtexitem"})
      
      elements = {}
      for key, name in zip(keys, names):
	k = key.find("a").get("name")
	
	if name.blockquote is not None:
	  name.blockquote.extract()
	
	v = "".join([str(el) for el in name.contents])
	elements[k] = v
      
      
      if args.htmlfname is None:
	# If no target file has been provided, just print the snippet
	
	target = BeautifulSoup('<div id="citations"></div>')
	for k, v in elements.iteritems():
	    soup = BeautifulSoup('<div id="%s">%s</div>'%(k, v.decode('utf-8')))
	    target.div.append(soup)
	print target.prettify()
	
      else:     
	# If a target file has been provided...
	
	with open(args.htmlfname, "r") as fhtml_target:
	  target = BeautifulSoup(fhtml_target.read())
	  
	  # Modify "citation" element
	  citations = target.find(id="citations")
	  citations.clear()
	  for k, v in elements.iteritems():
	    soup = BeautifulSoup('<div id="%s">%s</div>'%(k, v.decode('utf-8')))
	    citations.append(soup)
	  
	  # Override the file with the new content
	  with open(args.htmlfname, "w") as output_fname:
	    output_fname.write(target.prettify())
	  output_fname.close()
	fhtml_target.close()
      
      # remove intermediate file (no longer used)
      os.system( "rm %s.html"%(fname) )
      
    fhtml_tables.close()