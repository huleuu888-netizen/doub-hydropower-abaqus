# V16 Geometry Rebuild Checklist

## Purpose
Ensure the Abaqus model corresponds to the Duobu Hydropower Station engineering description before calculation.

## Geometry requirements

- [ ] Dam body gravel zoning completed
- [ ] Riverbed deep overburden layers represented
- [ ] Left bank cover layer represented
- [ ] Right bank unloading rock zones represented
- [ ] Concrete cutoff wall created
- [ ] Geomembrane equivalent seepage layer created
- [ ] Right bank grouting curtain created

## Geological consistency

- [ ] Q3al layer sequence mapped
- [ ] Engineering geological zones linked to Abaqus element sets
- [ ] Each region has traceable geometry source

## Rule
Do not start Abaqus seepage calculation before all required items are checked.
