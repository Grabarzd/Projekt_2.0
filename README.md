# Project 2
## Project: "QGIS plugin - PyQGIS"
### How does it work and what is it for?
--------------------
The main goal of the project is to create a plug compatible with QGIS software. The plugin will allow the user to use some useful functionalities in QGIS. Below is a list of the possibilities that the application has:

- Calculation of height difference between two given points:
	- The plugin calculates the height difference between these points.
	- The result is displayed in the information bar of the QGIS interface.
	- If a single point is selected, the plug-in will return an error.
	- If no points are selected, the plugin will return an error.

- Calculation of the surface area for at least three selected points:
	- The plugin calculates the area of a figure based on these points using the Gaussian method.
	- The result is displayed in the information bar of the QGIS interface.
	- If you select two points, the plugin will return an error.
	- If no points are selected, the plugin will return an error.


### Additional options
--------------------
- Development of the file inside the plugin:
	- The user can indicate the PL1992 or PL2000 plane coordinate system of the file to be uploaded.
	- In the PL2000 system, it is possible to select the zone [15 degrees - 24 degrees]
	- Ability to select and open a text file [.txt or .csv].
	- The content of the file is loaded into the application cache and placed in a table (QTableWidget).
	- Added layer in proper datum [EPSG] to current QGIS project.

- Drawing a polygon based on selected points and calculating the area:
	- User can select points on active layer to create polygon.
	- The plugin draws this polygon and adds it to a new layer in the QGIS project.
	- If no points are selected, the plugin will return an error.


- Clearing the result console and object selections on user's request.

- Selection of the option to display the area in m2, ares or ha according to the user's choice.

### Example of a txt/csv file
--------------------

The file generated in the plugin in the first column is the ID from the given point, the second X coordinate, the third Y coordinate and the third Z coordinate.
The plugin supports only data for attributes consisting of ID,X,Y,Z. Otherwise, the program will show an error or the calculation results will be wrong.

In the .txt file, do not enter the number of the point and the header, it is defined automatically. The coordinates are separated by spaces, and if there is an extra space, the program will display an error.

##### .txt file
```bash
0 0 100
200 0 700
250 100 600
200 300 500
-100 300 400
150 100 300
0 100 200
```

In the .csv file, we must provide the numerical point ID and include the header. The coordinates are separated by commas, if the file format is incorrect, the program will load the file, but not the coordinates.

##### .csv file
```bash
id,x,y,z
1,0,0,100
2,200,0,700
3,250,100,600
4,200,300,500
5,-100,300,400
6,150,100,300
7,0,100,200
```

### Plugin conditions
--------------------

- In order to calculate the area, the points must be entered in a clockwise direction.

- Differences in the height of points are counted in accordance with the order of the indexes.

- The polygon is generated in the order of the indexes.

- When adding points from a file or creating a polygon, it creates a new temporary layer.

- Adding data to the table is conditioned according to the index order.

- When using the "Add file" option, no file was selected, the program will display "No file selected".

### System requirements

- Operating system: Windows 10/11
- Python version 3.9
- QGIS version 3.30 or 3.28

### Installation process
--------------------

1. Download plugin from [[Zdalne repozytorium Github]](https://github.com/Grabarzd/Projekt_2.0/tree/main)

	After downloading all plug-in files, move them to a folder named "Wtyczka_Projekt_2" for installation.

2. Open QGIS.

3. Go to "Plugins" > "Manage and Install Plugins...".

<img src="https://i.imgur.com/jKS1MVq.png">

4. Select "Load plugin from file..." and select the downloaded plugin file with the .zip extension.

<img src="https://i.imgur.com/l8hqrLX.png">

5. Once the plugin is loaded, it will be activated and visible in the side panel or QGIS menu.

<img src="https://i.imgur.com/7WA4vAC.png">


### Plugin support
--------------------

-Calculation of height difference

<img src="https://j.gifs.com/jYwQv4.gif">

-Calculation of the surface area

<img src="https://j.gifs.com/pZDwRy.gif">

-Elaboration of the file inside the plugin

<img src="https://j.gifs.com/nRAQG5.gif">

-Polygan drawing based on points

<img src="https://j.gifs.com/qQERA7.gif">

- Prompt and clear the console

<img src="https://j.gifs.com/vQMqm8.gif">

- Loading data into the table

<img src="https://j.gifs.com/w0N9nr.gif">
