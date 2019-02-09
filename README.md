# The Browser Tutorial

This is a very small application intented to provide a starting point for anyone who wants to learn how to develop with Qt in C++ or Python.

Both applications were prepared for a talk at the first edition of the "Jornadas Tecnológicas" in Coín (Málaga, Spain)
in order to show how a Qt application is developed and how the differences between a C++ and a Python Qt application are mostly in the language syntax.

# Setting up a development environment

## C++

To open the C++ project (inside the cpp directory), you'll need Qt Creator, Qt Designer (to design the application interface), Qt Linguist (if you want to create/modify translations), and some development libraries.

### openSUSE Leap/Tumbleweed

```
sudo zypper in libqt5-creator libqt5-qtwebengine-devel libqt5-qtbase-devel libqt5-linguist libqt5-qttools
```

Other distributions will probably have similar package names

## Python

If you want to open the Python project (inside the python directory), you'll need KDevelop, the python plugin for KDevelop, as well as the Python Qt bindings (I used PyQt, but PySide2 is another valid alternative for your application). Please don't forget to read the Known Issues section below for some important notes about the python application.

### openSUSE Leap/Tumbleweed

```
sudo zypper in kdevelop5 kdevelop5-plugin-python3 python3-qt5 libqt5-linguist libqt5-qtto
```

Other distributions will probably have similar package names

# How to run the examples

## C++

Open the thebrowsertutorial.pro file with Qt Creator. In the Build menu, select "Run". The project will be automatically built the first time you run it (and every time you run it and the code is changed).

## Python

Just go into the python directory and run ```python3 thebrowser```. Alternatively, you can open the kdevelop project, in the Run menu, select "Configure Launches..." and there, add a script application with ```python3``` as Script interpreter and the __main__.py file as script file.

# Known Issues

None of the applications are thought to be installed, so please, don't try to install them on your system. They're just intended for learning purposes. Because of this, they both will search for runtime files in relative directories, which sometimes might fail if you run the application from a different directory from the expected one. If you run the C++ version and the translations are not found, please, just change the sources to hardcode the full path to the ```languages``` directory. This is absolutely NOT how it must be done in a real application, but I preferred to do it this way in order to simplify the code. In a real application you would install the files in a standard location in the system and use [QStandardPaths::standardLocations](http://doc.qt.io/qt-5/qstandardpaths.html#standardLocations) to locate them.

# License

This tutorial and its sources are released under the [GPL-3.0 license](LICENSE).

