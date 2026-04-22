Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #slicing
>>> a="codegnan"
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[:8]
'codegnan'
>>> a[4:]
'gnan'
>>> a="work hard until you succeed"
>>> a[16:19]
'you'
>>> a[20:26]
'succee'
>>> a[20:27]
'succeed'
>>> a[10:15]
'until'
>>> a[5:9]
'hard'
>>> a[0:4]
'work'
>>> b="beautiful is better than ugly"
>>> b[13:19]
'better'
>>> b[25:29]
'ugly'
>>> b[0:9]
'beautiful'
>>> a="patience is strength"
>>> a="patience is strength"
a{-8:-1]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a[-8:-1]
'strengt'
a[-8:]
'strength'
a[-20:-13]
'patienc'
a[-20:-12]
'patience'
a="sun rises in the east"
a[-8:-5]
'the'
a[-4:]
'east'
a[-20:-12]
'un rises'
a[-17:-12]
'rises'
a[-21:-18]
'sun'
a[:-18]
'sun'
#striding
a="cloud computing"
a[::5]
'c u'
a[::3]
'cucpi'
a[3:]
'ud computing'
a[:9]
'cloud com'
a[::7]
'cog'
a[5:11]
' compu'
a[::2]
'codcmuig'
a="python programming
SyntaxError: unterminated string literal (detected at line 1)
a="python programming"]
SyntaxError: unmatched ']'
a="python course"
a[-1:-9:-3]
'eu '
a[-4:-12:-4]
'un'
a[-3:-14:-2]
'ro otp'
#mirror image
a[::-1]
'esruoc nohtyp'
