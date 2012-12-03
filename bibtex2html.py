import os
import argparse
from BeautifulSoup import BeautifulSoup

        
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Generates two files with the formated citations.')
    parser.add_argument('bibfname', metavar='bibfname', type=str, help='an string with the filename of the *.bib')
    parser.add_argument('htmlfname', metavar='htmlfname', type=str, help='an string with the filename of the *.html where the output HTML snipet will be inserted.')
    parser.add_argument('-s', default=None, dest="style", help="BibTeX style (plain, alpha, ...)")
    args = parser.parse_args()
    
    
    fname =  args.bibfname.split('/')[-1].split(".")[0]
    
    os.system( "bibtex2html %s"%(args.bibfname) )
    #os.system( "mv %s_bib.html citations_bib.html"%(fname) )
    
    
    # parse and extract
    
    fhtml_tables = open("%s.html"%(fname), "r")
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
    
    #print elements
    
    # modify target file
    
    with open(args.htmlfname, "r") as fhtml_target:
      fhtml_target = open(args.htmlfname, "r")
      
      target = BeautifulSoup(fhtml_target.read())
      
      citations = target.find(id="citations")
      citations.clear()
      
      for k, v in elements.iteritems():
	soup = BeautifulSoup('<div id="%s">%s</b>'%(k, v.decode('utf-8')))
	citations.append(soup)
      
      # Override
      with open(args.htmlfname, "w") as output_fname:
	output_fname.write(target.prettify())
      output_fname.close()
    fhtml_target.closed
    
    # remove intermediate file (no longer used)
    os.system( "rm %s.html"%(fname) )