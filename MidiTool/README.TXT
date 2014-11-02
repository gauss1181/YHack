 
Version : 1.14
Distributed: 12/2012



-------------
Installation:
-------------
needs Java 1.6 or 1.7 runtime environment.
unpack zip-file to any diretory

run.bat contains the java command to start the application. 
(doubleclick)


------
Usage:
------

See project Wiki for the Midi Tool on sourceforge.net
http://sourceforge.net/p/miditool/wiki/Home/

Configuration is done in settings.txt:

	Language, Gui size
	Auto start function of player
	Default directories 
	Default connection properties for I/O 
	Defined keyboards 
	Defined scales
	Panels	
	Default Settings for Lyrics Panel


I recommend having a virus scanner active when loading MIDI
files from the internet 



---------------------------------
known Bugs & Restrictions, Hints:
---------------------------------


Zip support for compressed midi files: extracts the first one it 
finds. 

Instrument changes affect channel 0 only (colored in cornflowerblue)

Loading SF2 sound fonts at runtime causes a problem with some 
Midi files: Funny sound at start. This has been temporarily 
fixed for pure Piano pieces (by eliminating vibrato messages) 

Alternative to loading SF2 files in Midi Player Tool: 
Using a software synthesizer: See project Wiki for setup (it's easy)

SF2 Soundfont maximum size is around 240MB with Windows 32bit
If with SF2 music interruptions occur or GUI becomes unresponsive 
try to extend the java heap space  - see run.bat

Midi Player shows only the first banks instruments.

A few non-piano pieces do not work correctly with Gervill.
Gervill is officially part of java since java 7 but I found it 
also on a Windows 7 installation with Java 1.6.0_35-b10.


Lyrics Panel:
--------------
Now openGL and detached from Swing GUI. F1 opens a help screen. 

Start/stop and browsing songs in a loaded playlist can be done 
per player, playlist, keyboard or presenter.
Auto-function of playlist should be switched off.

Effects need a relatively fast PC or Laptop. 
Maximum frames per second can be set in settings.txt. 
More FPS = smoother scrolling. 
FPS is automatically increased with character size up to 
the defined maxFPS limit.

Full screen mode works only for the primary screen.



Drag & Drop
-----------
Works for IE and Firefox; it does not with Opera Web Browser.
Other Browsers I don´t know. 


USB devices: 
------------
Tool can either process in or out, but not both.
If input is displayed on the piano panel but no sound audible 
try switching from Gervill to a different synthesizer in dev panel. 

Sequence Panel: 
---------------
Output of track info is formated for Excel (copy & paste)
Panel can be activated in settings.txt 










-------------------------------------------
external Software included in this package:
-------------------------------------------

Gervill.jar

Synthesizer for Java with own Soundbank and SF2 import function
http://java.net/projects/gervill/pages/Home
License: Gervill comes as part of Java since Java 1.7

---------

TableLayout.jar 

Daniel Barbalace´s Table Layout for Java Swing
http://www.clearthought.info/sun/products/jfc/tsc/articles/tablelayout/
License: Free

---------

7za.exe

7-zip command line version
Copyright (C) 2012 Igor Pavlov
http://www.7-zip.org/download.html
Java´s jar utility does not support all compression formats used
in Zip-Files, 7za.exe does.
License: GNU LGPL


---------

Lwjgl.jar

Light Weight Java Game Library
http://www.lwjgl.org/
LWJGL provides ways to use OpenGL with Java

License:

* Copyright (c) 2002-2007 Lightweight Java Game Library Project
* All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions 
* are met:
*
* * Redistributions of source code must retain the above copyright
*   notice, this list of conditions and the following disclaimer.
*
* * Redistributions in binary form must reproduce the above copyright
*   notice, this list of conditions and the following disclaimer in the
*   documentation and/or other materials provided with the distribution.
*
* * Neither the name of 'Light Weight Java Game Library' nor the names of
*   its contributors may be used to endorse or promote products derived
*   from this software without specific prior written permission.
*
* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
* "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT 
* LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR 
* A PARTICULAR
* PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
* CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
* EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
* PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
* PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
* LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
* NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
* SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

---------

Slick.jar 

Library for OpenGL 2D applications in LWJGL 
http://slick.cokeandcode.com/
2D Game Library based on LWJGL

License:

* Copyright (c) 2007, Slick 2D
* All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions 
* are met:
*
* * Redistributions of source code must retain the above copyright
*   notice, this list of conditions and the following disclaimer.
*
* * Redistributions in binary form must reproduce the above copyright
*   notice, this list of conditions and the following disclaimer in the
*   documentation and/or other materials provided with the distribution.
*
* * Neither the name of 'Light Weight Java Game Library' nor the names of
*   its contributors may be used to endorse or promote products derived
*   from this software without specific prior written permission.
*
* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
* "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT 
* LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR 
* A PARTICULAR
* PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
* CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
* EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
* PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
* PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
* LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
* NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
* SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/



---------------
Subdirectories: 
---------------

"jar"      Midi Player Tool files 

Everything else (directories metronome, playlists, midis, downloads, 
backgroundimages) can be changed in settings.txt



----------
MIDI Files
----------

The Midi Files distributed with this software are for entertainment 
only and not for commercial use. They have been gathered from 
various web sites on the Internet.
All files are believed to be in the public domain / under CC-BY-SA.
There is no intent to infringe on any copyright. If you hold copyright 
to any music I am distributing with this tool and wish its removal, 
please e-mail me and provide legal proof of your right to demand 
removal. If verified, the music will be removed immediately. 


Files in this distribution have been downloaded from:

Classical:
http://www.piano-midi.de/midis/
http://www.harfesoft.de/midi/
http://www.classicalmidiconnection.com
http://tirolmusic.blogspot.com/
http://www.midiworld.com
http://www.8notes.com/scores/2946.asp?ftype=midi
www2.gobiernodecanarias.org/educacion/17/WebC/Apdorta/cristal/cristal.html

Ragtimer:
http://www.trachtman.org/rollscans/midifiles/
http://www.johnroachemusic.com/

Karaoke:
http://www.busyhands.co.za/midi/
http://chomikuj.pl/

Pop/Rock:
http://files.ifnimidi.com/
http://claymore.engineer.gvsu.edu/%7Eskibinss/misc/midi
http://home.roadrunner.com/~jgglatt/


The one background image was taken from
http://de.simpsons.wikia.com

SF2 soundbanks can be found on
http://hammersound.net/cgi-bin/soundlink.pl
http://www.composition-contest.com
http://www.synthfont.com/soundfonts.html
and other websites.

--------
License:
--------

This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see http://www.gnu.org/licenses/.

This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it.




-------------------------------------------------------------------------
version history:
-------------------------------------------------------------------------

V1.00 	written in 2009, 2010
V1.01 	D&D
V1.02 	Minor bugs fixed, D&D did not work from IE

V1.05 	Different channels -> different colors. 
      	
V1.06	Playlist function added
	Program now accepts input from devices like electronic 
	keyboards etc.
	
V1.07	GUI re-done
	Metronome extended to 16 beats / 4 full notes 
	
V1.08	Fixed bug with Keyboard Reader 
	Config files consolidated into one

V1.09	D&D Support for zip-files

V1.10	panel added for lyrics  

V1.11	bugfix
	implements Java Accessibility API
	
V1.12	SF2 support
	timer

V1.13	Workaround for SF2 bug. USB bug fixed.	
	
V1.14	Lyrics Window detached from GUI (openGL)

