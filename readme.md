# Shape Generator

## Purpose
This library allows for the generation of random `.svg` and `.png` images and the scoring of the generated images relative similarity using (https://en.wikipedia.org/wiki/Locality-sensitive_hashing).

This means that you are able to generate random images and determine which of the randomly generated images are most similar in shape to a given target image.

## How to use

### Set your preferences

* In the file `constants.txt`:
 * set the value of `nmax` to the number of times you'd like to *iterate* the shape generating function. The default is set to `10000`.
 * set the `path` to the `startingShape` of your choice. Make sure that it is an `.svg` file. We suggest a starting shape with no more than `8` vertices. The detault is a *circle*.
 * set the `path` to the `generatedShape` that you'd like to be the end product of the image generation process.

### Generate shapes
In order to generate your first set of shapes, open the root folder of this project and type the following into your command line:

`python draw.png`

This will generate as many images as specified by `nmax` and save them to the folder `genimages` and save the image most similar to the target image in `topimages`.
