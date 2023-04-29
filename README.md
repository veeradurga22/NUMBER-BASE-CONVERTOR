# NUMBER-BASE-CONVERTOR


A number base converter is a tool that allows you to convert a number from one numerical base system to another.
The most commonly used numerical base systems are decimal (base 10), binary (base 2), octal (base 8),
and hexadecimal (base 16).

Python provides bin(),dec(),hex(),oct() functions to convert the numbers..

Used Modules:
  * *Tkinter:* Tkinter is a standard GUI (Graphical User Interface) toolkit for Python that allows you to create desktop applications with graphical user interfaces.
  It provides a set of tools and widgets to build user interfaces, such as buttons, labels, text boxes, menus, and more. Tkinter is part of the standard Python
  distribution, which means that you do not need to install any additional libraries to use it.
  
  * *from PIL import ImageTk, Image:* it is a Python import statement that imports the ImageTk and Image modules from the PIL (Python Imaging Library) library.
  The Image module provides a set of functions to load, manipulate, and save various image file formats, such as JPEG, PNG, and BMP. For example, you can use the
  Image.open() function to load an image file, and then use various methods, such as resize() or rotate(), to manipulate the image.
  
*FLow of code:*

   First we have to create the interface using Tkinter in that keyboard is placed to enter the values..
   In that , the required keys are enabled for the number system for example if we select binary then 0 and 1 wiil be enable and rest of the buttons are disabled.
   In backend convert the numbers using bin(),dec(),hex(),oct() functions which are taken inputs from the Tkinter GUI.
   Convert button will convert the numbers.
   Reset button will reset the data.
   History button will show the history of recent converted values.
   Exit button is for exit.

