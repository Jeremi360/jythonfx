JythonFX
========

**PL:**
Info na temat instalacji i tutorial po polsku zajdziecie [tu](http://retrofunhd.esy.es/?p=56)

**ENG:**
Simple tricks to make easy to develop apps using Jython + JavaFX.

**Samples:**
- Simple onebutton app (HelloJyFx.py)
- Simple FXML app(FXMLSample.py, FXMLSample.fxml)

**Done:**
- Application class(application.Application)
- EventHandler class(event.EventHandler)
- FXML Files Loader(fxml.FXMLLoader) with support for Tabs
- Tool to fix user jython path and abort to run app on older than 7 Java(fix.getJavaFX)
- Temples

**TODO:**
- Sample for FXML with Tabs
- Class & Sample for make Animation easy
- Recreate some of Gtk 3.12 widgets
- Recreate some Grabbo widgets

**Files included:**
- **samples** - samples with commentary
- **Templates** - file temples for Eclipse IDE

**Required:**
- [Jython](http://www.jython.org/downloads.html) 2.5.x or higher
- [Java](http://www.java.com) 7u11 or higher

**How install:**

1. Add *java_home/jre/lib/jfxrt.jar* to your jython path(only Java 7u*)

1. Copy *jythonfx* directory to *jython_directory/Lib/site-packages*

**Install Templates:**

1. In Eclipse IDE open **Window -> Preferences -> PyDev -> Editor -> Templates**

1. Click on **Import**, browse to *JythonFX/Templates* choose template

