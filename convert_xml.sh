
#!/bin/bash

# Run from parent directory in kanelbullen
# Before running: chmod +x convert_xml.sh

cd murtazo
cd cloudnaca
cd msh

for f in *.msh; do
    dolfin-convert "$f" "${f%.*}.xml"
done
echo "*** Converted to xml ***"
for x in *.msh; do
     rm "$x"
done
echo "*** Deleted all msh ***"
