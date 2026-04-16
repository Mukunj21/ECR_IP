# South Elevation / East Elevation / North Elevation / West Elevation

## Diagram analysis

**Part 1 — Diagram type and relationship type**

This is an **architecture/system** diagram: a set of architectural elevation drawings for a house. It shows four exterior views of the same building: **South Elevation, East Elevation, North Elevation, and West Elevation**.

The relationship between elements is primarily **compositional** and **hierarchical**:
- Each elevation is a composition of architectural components such as roof, walls, windows, doors, vents, porch/steps, grade lines, and notes.
- The four elevations are separate but related views of the same structure.
- Annotation callouts create directed relationships from notes to the building features they describe.

**Part 2 — Structured extraction**

### 1) South Elevation
- **Roof**
  - Label: `Class "A" Roofing, typical`
  - Category: roof annotation
  - Visible structure: low-pitched roof with a central raised gable-like section
- **Windows**
  - `sliding window`
  - `casement window- hinges on outside`
- **Doors / openings**
  - Central entry door with multiple vertical panels
  - Garage door on right side
- **Vents**
  - `underfloor vents`
  - `underfloor ventilation calculation`
  - `1,136 = 7.6 sq.ft. underfloor ventilation required`
- **Elevation title**
  - `South Elevation`
  - Scale: `1/4" = 1'-0"`
- **Connections / callouts**
  - Curved arrow from `sliding window` label to left window
  - Curved arrow from `casement window- hinges on outside` label to the paired center-right windows
  - Arrow from `underfloor vents` label to small vent openings near base
  - Arrow from `underfloor ventilation calculation` note toward the garage/ventilation area
  - Leader lines from ventilation requirement box to the relevant area beneath the house

### 2) East Elevation
- **Roof**
  - Roof with central raised section
  - `1x4 trim typical`
- **Wall finish / siding**
  - `5/8" plywood siding`
- **Windows / doors**
  - Two small windows on left
  - One vertical door near center-left
  - One window near center-right with `1x4 trim typical`
  - Sliding door / large opening on right side leading to porch
- **Porch / deck / stairs**
  - Porch with railing
  - Stairs descending on far right
  - `handrail must be self return & grippable, see UBC section 1003.3.6`
  - `36" landing, min`
  - `2' 0"`
- **Ground / foundation / grade**
  - `6" min earth to wood`
  - `stepped footing outline`
  - `show grade line`
  - `4' 9"` dimension near stair/foundation area
- **Window note**
  - `awning window- hinge on top`
- **Elevation title**
  - `East Elevation`
  - Scale: `1/4" = 1'-0"`
- **Connections / callouts**
  - Arrow from `awning window- hinge on top` note to left-side windows
  - Arrow from `5/8" plywood siding` note to wall surface
  - Arrow from `1x4 trim typical` note to window trim
  - Arrow from handrail code note to stair handrail
  - Arrow from `stepped footing outline` note to dashed footing line
  - Arrow from `show grade line` to the grade profile
  - Dimension callouts indicate vertical measurements near stair and landing

### 3) North Elevation
- **Roof**
  - Main roof with central raised section
  - Roof pitch notation: `12` over `4 (Typical Pitch)`
- **Windows / openings**
  - Left window near stairs/porch
  - Center large sliding door/opening
  - Right window on main wall
- **Porch / railing / structure**
  - Left stair/porch area with railing
  - Central deck or platform area with exposed bracing
  - `2 x 4 cross bracing`
  - Note box: `Cut line indicates that the railing is continuous but not shown so the structure behind can be seen`
- **Ground / grade**
  - `Grade should slope away from house 1/4" in 1'-0" for 4' min.`
  - Dashed grade / footing lines under structure
- **Elevation title**
  - `North Elevation`
  - Scale: `1/4" = 1'-0"`
- **Connections / callouts**
  - Arrow from note box about cut line to the railing area
  - Arrow from `2 x 4 cross bracing` label to the under-deck bracing
  - Text note on right refers to sloping grade away from house

### 4) West Elevation
- **Roof**
  - Low roof with central raised section
  - Roof pitch callout: `12` / `4 (Typical Pitch)`
- **Vent**
  - `Gable Vent`
- **Windows / openings**
  - One rectangular window on left-center wall
- **Wall / foundation**
  - Simple wall plane with several small base vents/openings
  - Grade line at bottom
- **Elevation title**
  - `West Elevation`
  - Scale: `1/4" = 1'-0"`
- **Connections / callouts**
  - Arrow from `Gable Vent` label to vent opening near roof peak

### 5) Shared architectural elements across the sheet
- Exterior building shown in four orthographic elevations
- Roof lines, wall planes, windows, doors, vents, stairs, porches, grade lines, and foundation outlines
- Annotation arrows and leaders connect descriptive notes to specific physical features
- The sheet is a unified architectural presentation of the same house from four sides

### 6) Visible text transcribed
- `Class "A" Roofing, typical`
- `sliding window`
- `casement window- hinges on outside`
- `underfloor vents`
- `underfloor ventilation calculation`
- `1,136 = 7.6 sq.ft. underfloor ventilation required`
- `South Elevation`
- `1/4" = 1'-0"`
- `1x4 trim typical`
- `5/8" plywood siding`
- `6" min earth to wood`
- `awning window- hinge on top`
- `stepped footing outline`
- `show grade line`
- `2' 0"`
- `handrail must be self return & grippable, see UBC section 1003.3.6`
- `36" landing, min`
- `4' 9"`
- `East Elevation`
- `Grade should slope away from house 1/4" in 1'-0" for 4' min.`
- `Cut line indicates that the railing is continuous but not shown so the structure behind can be seen`
- `2 x 4 cross bracing`
- `North Elevation`
- `12`
- `4 (Typical Pitch)`
- `Gable Vent`
- `West Elevation`
- `SAMPLE HOUSE PLANS BPC-022`
- `Revised: 12/27/2018, Reviewed 01/2020`
- `Page 2 of 4`