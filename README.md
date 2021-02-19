# insert catchy name here :)

EDA Package and visual programming language designed for the generation of parametric Cells.  Prototype a design in minutes then take the generated Python code and deploy thousands of variants of a structure.  The system can be extended with a plugin architecture to produce metrology instructions for each generated structure providing a workflow for automating measurements.

## Requirements:
- Labelme:
    https://github.com/wkentaro/labelme
    Used to annotate an image to separate only the animal, any other software could also be used for this.
    Used to annotate corresponding points between the animal and the silhouette image
- ImageJ:
    https://imagej.net/Fiji
    The image warping is done through the BUnwarpJ plugin(included with Fiji) to perform a B-spline image deformation.
- Potrace:
    http://potrace.sourceforge.net/
    Used to vectorise the binary image of the animals markings
- Inkscape:
    https://inkscape.org
    Used to prepare the silhouette images and finally to clip the resulting vector polygons into the original silhouette and reincorporate into the passport document.


## Workflow:

Take animal images showing markings corresponding to the required views of the passport:
- Left
- Right
- Fore - rear
- Hind - rear
- Neck - ventral
- Face
- Muzzle

Taking as an example the left side view. The second page of the passport document was opened in inkscape silhouette vectors were extracted ungrouped and separated and saved oout to svg files.  Note the image file width and height in pixels of the left side image.  Open the left.svg file in inkscape resize the page to the dimensions of the input image, Scale and centre the silhouette graphics on the page then export the image as a .png file, taking care to choose "Page" as the output.
Put both images in the same folder and start the labelme annotation tool.  Click on open dir and select the folder with the images.  Click File->Save Automatically ensuring that this is checked.  Also click Edit->Keep annotations.  Click on create polygon and draw a polygon around the outline of the animal.  Name the polygon as "left", to adjust after creation click on "Edit polygons". This allows the nodes to be repositioned. Shift-click will delete a node and Ctrl-Shift-p to insert a node.
Next choose Edit-> Create Point.
Annotate and name the anatomy, I used the following points, however anything could be used as long as it can be consistent across both images:
- Eye
- Upper (from silhouete)
- Mid (from silhouette)
- Lower (from silhouette)
- Jaw
- Ramus
- Chin groove
- Tip of Pinna
- Nares
- Forelimb
    - Fetlock
    - Coronet
    - Heel
    - Knee
        - Palmar
        - Dorsal
    - Elbow
        - Cr
        - Cd
- Shoulder
- Acromion
- Hindlimb
        - Stifle
            - Cr
            - Cd
    - Hock
    - Cannon
         - Cr
         - Cd
    - Fetlock
         - Cr
         - Cd
    - Coronet
    - Heel
- Flank
- Dependent abdomen
- Dock
- Croup
- Biceps femoris 


![example1](examples/left-labelled.png)

