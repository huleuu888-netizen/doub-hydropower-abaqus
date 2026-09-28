# V16 Material Mapping Plan

## Purpose
Establish traceable correspondence between engineering geology and Abaqus materials.

## Required mapping

| Engineering unit | Abaqus material |
|---|---|
| Dam shell gravel material | M_DAM_SHELL |
| Filter layer | M_FILTER |
| Drainage layer | M_DRAINAGE |
| Q3al-II | M_Q3AL_II |
| Other alluvial layers | M_Q3AL_GROUP |
| Right-bank unloading zone | M_RIGHT_BANK_UNLOAD |
| Cutoff wall | M_CUTOFF_WALL |
| Curtain zone | M_GROUT_CURTAIN |

## Verification requirements

Each material should have:

- Permeability coefficient source
- Engineering geological meaning
- Element set correspondence
- Abaqus material definition
