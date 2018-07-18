# -*- coding: utf-8 -*-

etiquetas={


"<h1>":chr(0x1B)+chr(0x1d)+"a"+chr(2)+chr(0xa)+chr(0x1B)+chr(5)+chr(3),
"<h2>":chr(0x1B)+chr(0x1d)+"a"+chr(2),
"</p>":"",
"<p>":chr(0x1B)+chr(0x1d)+"a"+chr(0),
"<left>":chr(0x1B)+chr(0x1d)+"a"+chr(2),
"<h3>":chr(0x1B)+chr(0x1d)+"a"+chr(2),
"</h1>":chr(0xa)+chr(0x1B)+chr(1)+chr(0),
"</h2>":"",
"</h3>":" ",
"<hr/>":"------------------------------------------",
"<br/>":"\n",
"<center>":chr(0x1B)+chr(0x1d)+"a"+chr(1),
"</center>":chr(0x1B)+"a"+chr(0),
"<i>": "",
"</i>": "",
"<b>": "",
"</b>": "",
"<corte/>":chr(0x1D)+"V"+chr(66)+chr(0),
"<cajon>":chr(0x1b)+ chr(7)+chr(5)+chr(5)+chr(7),
"<red>":chr(27)+'r'+chr(1),
"</red>":chr(27)+'r'+chr(0),
"<t/>":'\t',
"<code>":chr(0x1D)+'h'+chr(80)+chr(0x1D)+'w'+chr(4)+chr(0x1D)+'k'+chr(2),
"<code/>":chr(0)+chr(0x1A)
}
