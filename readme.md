# Splines

A small demo showing how to do equaly-spaced interpolation of 3D cubic Bézier splines using numpy

![Screenshot](./readme_extras/Screenshot%202024-03-23%20112746.png)

Based on what I learned from this youtube video: [The Continuity of Splines](https://www.youtube.com/watch?v=jvPPXbo87ds) by Freya Holmér.

I dont think that video covers the solution specifically, so I used some GPT magic and some of my own knowledge to get to this point.

I created this because I couldn't figure out how to make this work using Blender's python API. I know that it can be done using the geometry nodes environment. I think an alternative is to use the `ops.curve.subdivide(number_cuts=...)` function. But I didn't think of that at the time because I wanted a non-destructive alternative.
