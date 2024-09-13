 MINIFY
=======


This is a Python based program that will minify CSS and JavaScript files.

INSTALLING:
===========

  To install, simply run:

    ./install.sh

  or, you may manually execute each command:

    python3 setup.py clean;

    python3 setup.py build;

    python3 -m pip install --user .
    (preference, you may also install for everyone, if you wish)


This program requires 1 thrid party python module, "rjsmin."

TODO:
=====
  I would like to migrate in the code form rjsmin (leaving credit where credit
  is do), but so are no dependencies.  I would add a "CREDITS" file, and list
  all of the author's imformation of "rjsmin"

  There is a single css function (remove_empty_rules) I found created, but not
  used.  I need to learn more about this function, and see if it should be
  being called.

BUGS:
=====

  I don't think "pypi" currently works.

