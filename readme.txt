To calculate the resulting dimensions of a lithophane given some pixel dimensions, divide each pixel length by 2.5!

Blender:
    To see a vertex coordinates: https://blenderartists.org/t/how-to-see-vertex-coordinates/420220
        In Edit mode, press the letter N. This will pop-up the Transform properties window. This window will
        show the coordinates of any vertex, edge, or face, you select. You can also manual change the coordinates 
        using the Transform properties widow.
    To add a vertex
        Move the red,white,and black target to a new spot then press CTRL-LMB. Using the tool to see vertex cords you
        can determine the x,y cords of each vertex.


    To make a face from selected vertices
        To create a face from selected vertices or edges, select as many as you want to bound your face, then press 'F'.

    
    ORDER OF OPERATIONS
        - run script
        - add finished STL into blender
        - in edit mode, open the Transform properties window (press N)
        - in edit mode, switch to vertex mode, then add 4 vertices by pressing CTRL-LMB, then set the coordinates for those points
        - select the 4 added vertices and make a face from the selection by pressing F
        - for each of the 4 edges of the lithophane, select each segment as well as the bottom edge, and create a face there to close the shape