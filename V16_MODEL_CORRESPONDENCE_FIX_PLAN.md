# V16 Model Correspondence Fix Plan

## Objective
Close the gap between the Abaqus model and the Duobu Hydropower Station engineering description.

## Phase 1: Complete engineering structures

Add and verify:

- Dam body zones
- Filter and drainage zones
- Concrete cutoff wall
- Geomembrane equivalent anti-seepage layer
- Right-bank grout curtain

## Phase 2: Geological model closure

Establish explicit mapping:

- Q3al-I
- Q3al-II
- Q3al-III
- Q3al-IV
- Q3al-V
- Right-bank unloading fractured rock zones

## Phase 3: Material traceability

Create:

Engineering layer -> Abaqus material -> permeability parameter source

## Phase 4: Hydraulic verification

Define:

- Initial pore pressure
- Upstream water head
- Downstream boundary
- Drainage boundary
- Seepage output variables

## Phase 5

Generate V16.1 engineering baseline model and validate before sensitivity studies.
