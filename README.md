# insert catchy name here :)

EDA Package and visual programming language designed for the generation of parametric Cells.  Prototype a design in minutes then take the generated Python code and deploy thousands of variants of a structure.  The system can be extended with a plugin architecture to produce metrology instructions for each generated structure providing a workflow for automating measurements.

## Requirements:
- Labelme:
    https://github.com/wkentaro/labelme
    Used to annotate an image to separate only the animal and also to annotate corresponding points between the animal and the silhouette image.
- ImageJ:
    https://imagej.net/Fiji
    Perform image warping from animal to silhouette. The BUnwarpJ plugin(included with Fiji) is used to perform a B-spline image deformation.
- Potrace:
    http://potrace.sourceforge.net/
    Used to vectorise the binary image of the animals markings.
- Inkscape:
    https://inkscape.org
    Used to prepare the silhouette images and finally to clip the resulting vector polygons into the original silhouette and reincorporate into the passport document.
- Python(3):
    https://www.python.org/
    Used for image processing, the following python libraries are also needed can be installed via pip:
        - PIL
        - Scikit-image
        - Numpy
        - Json
        - Base64

## Workflow:

### Get silhouette vectors
Take animal images showing markings corresponding to the required views of the passport:
- Left
- Right
- Fore - rear
- Hind - rear
- Neck - ventral
- Face
- Muzzle

### Segment and annotate
Taking as an example the left side view. The second page of the passport document was opened in inkscape silhouette vectors were extracted ungrouped and separated and saved out to svg files.
Next note the image file width and height in pixels of the left side image.  Open the left.svg file in inkscape resize the page to the dimensions of the input image, Scale and centre the silhouette graphics on the page then export the image as a .png file, taking care to choose "Page" as the output.
Put both images in the same folder and start the labelme annotation tool.  Click on open dir and select the folder with the images.  Click File->Save Automatically ensuring that this is checked.  Also click Edit->Keep annotations.  Click on create polygon and draw a polygon around the outline of the animal.  Name the polygon as "left", to adjust after creation click on "Edit polygons". This allows the nodes to be repositioned. Shift-click will delete a node and Ctrl-Shift-p to insert a node.
Next choose Edit-> Create Point.
![example1](examples/left-labelled.png)

Next, annotate and name the anatomy, I used the following points, however anything could be used as long as it can be consistent across both images:
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

Once this is done change to the silhouette, all the points should also appear, then it is simply a case of lining all the points up on the edge of the silhouette image.

![example1](examples/left-annotated.png) | ![example1](examples/silhouette-annotated.png)

### Warp image
Once the annotations are complete you should have two .json files, these contain a copy of the image along with the annotations. The next step is to pass these to a couple of python scripts:

**segment_image.py** Takes the left.json file and removes the background outputting a segmented image:

![example1](examples/left-segmentation.png)

**generate_landmarks.py** Takes both the .json files and creates a landmark file that we can pass to the bUnwarpJ plugin in ImageJ.

Follow the instructions for BUnWarpJ https://imagej.net/BUnwarpJ#User_Manual:
Load both images and the landmarks file, in the settings I used:
Mono
Very Coarse to Very Fine
Landmarks: 1.0 and all others settings to 0.0

Generate the morphed image then save it out to a .png file.

![example1](img/processed/warped.png)

### Vectorise

Run the **extract_markings.py** script.  This processes the image in a binary image and performs a couple of morphological transforms to smooth the bands.  An .bmp file is produced as a result.

![example1](img/processed/extracted-closed20.bmp)

Next run the potrace command against this binary image to produce an svg vector image:

*potrace --svg -o left-polygons.svg extracted-closed20.bmp*

The resulting file can be opened in inkscape, a red outline applied to the polygons with a hatch fill.

![example1](examples/polygon-hatched.png)

Finally the polygons can be clipped by the left.svg vector image to create a final result:

![example1](examples/left-final.png)

### Improvements
