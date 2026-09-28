# V16 Pre Analysis Gate

Before running Abaqus, all following gates must pass.

|Gate|Requirement|Status|
|-|-|-|
|Geometry|Engineering structures mapped to Abaqus regions|Pending|
|Material|All regions have material definitions|Pending|
|Permeability|All seepage materials have traceable permeability parameters|Pending|
|Boundary|Upstream/downstream head and drainage conditions defined|Pending|
|Step|Seepage analysis step and initial conditions defined|Pending|
|Output|Q, head, pore pressure and hydraulic gradient outputs defined|Pending|

Only after all gates pass should S01 baseline calculation begin.
