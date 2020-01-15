---
author: Emil Stenström
categories:
- Django
- Tutorial
date: 2008-10-31 18:37:18
guid: http://friendlybit.com/tutorial/install-mysql-python-on-mac-os-x-leopard/
id: 299
permalink: /tutorial/install-mysql-python-on-mac-os-x-leopard/
title: Install MySQL-python on Mac OS X (leopard)
---

What a pain. Getting mysql to work with python is the single most annoying step in getting Django up and running (if you choose MySQL as the database). You see, python requires drivers to be able to talk to MySQL, and you have to compile those yourself. I just devoted several hours last night to help friends do what I did some months ago. This time, I thought I document it right here.

## How to install MySQL-python on Mac OS X

**Step 1**: **Brace yourself**, this proccess is really really annoying.

**Step 2**: [**Download MySQL** for Mac](http://dev.mysql.com/downloads/mysql/5.0.html#macosx-dmg) (Skip registration by clicking the link below the login form). You probably want "[Mac OS X 10.5 (x86)](http://dev.mysql.com/get/Downloads/MySQL-5.0/mysql-5.0.67-osx10.5-x86.dmg/from/http://mysql.mirror.kangaroot.net/)". Is it possible to use some other version of MySQL? Yes, as long as you have a version that includes the source code ([MAMP](http://www.mamp.info/en/mamp.html) does not include them, so it won't work). You'll need the source later on.

**Step 3**: **Install MySQL** by mounting the image you just downloaded, and double-clicking the package file for MySQL. Also install the prefPane that's included in the package. That adds an icon the system admin that lets you start and stop MySQL, very convenient.

**Step 4**: **Make the mysql command accessible from anywhere** by adding it to your PATH (a variable that holds all directories the terminal looks in to find the command you're trying to execute). The below just adds mysql's bin directory (it's probably the one I'm using below) to the PATH you currently are using:

```bash
export PATH=/usr/local/mysql/bin:$PATH
```

You probably want to add this line to a file called **.bash_profile** (yes, it starts with a dot), that is situated in your home directory (which you get to by just typing "cd"). This file gets run each time you start a new terminal, so it makes sure the mysql command is always accessible, no matter where you are.

**Step 5**: **[Download MySQL-python](https://sourceforge.net/project/showfiles.php?group_id=22307&amp;package_id=15775)**, you probably want the file that ends with .**tar.gz**.

**Step 6**: **Unpack the file** you just downloaded in an empty directory (anywhere)

**Step 7**: **[Download XCode](http://developer.apple.com/technology/xcode.html)** from Apple. The reason you need this is because XCode includes a C++ compiler you will use when installing MySQL-python soon. The download is huge (1 Gb), and to be able to download you first need to fill in a long form. The registration process for Apple Developer Connection is about the worst things Apple has ever created, so after completing it, you will either laugh or be really annoyed, just pick and choose. You do need XCode however.

**Step 8**: **Install the XCode Tools** **package** by first mounting the file you just downloaded, and then double-clicking on the **XCode Tools** package. It's the only one you need from the huge set of junk you just downloaded.

**Step 9**: Try installing MySQL-python by going to the directory where you unpacked it and typing:

```bash
python setup.py install
```

This will attempt to install the drivers, but **will fail**. This is because the coders behind MySQL-python have failed to fix a very simple bug in types.h ([1808476](https://sourceforge.net/tracker/?func=detail&amp;aid=1808476&amp;group_id=22307&amp;atid=374932) - "#define of uint breaks compiling on Mac OS X 10.5"). However, you can easily fix it yourself: Look for a reference to types.h in the terminal. When you find it, open that file in your favorite text editor and comment out line 92, which should say something about `#define` and `uint` (comments in C++ are double forward slashes: //).

**Step 10**: Now, **try the above command again**. It should install fine. If it doesn't, you will probably find out why by looking in the terminal for errors while compiling.

What did I say, isn't this process about 7 steps to long? Well, I hope this little guide helps someone.
