# Boggler
A solver for the popular word game Boggle.

# Install
```bash
$ git clone https://github.com/cblanken/boggler.git
```

To use the script to solve a particular Boggle board configuration, you'll need to do a few things
1. Create `.csv` of the board state like so:
    
    Here is an example `board.csv`. Note the orientation of the board does not matter.
    ```console
    $ cat boards/b1.csv
    s,a,i,p
    l,qu,a,y
    u,l,l,s
    o,w,h,a
    ```
2. Find a dictionary wordlist file or create your own

    The dictionary wordlist should have each word on a single line like so
    ```console
    $ cat wordlists/wordlist.txt
    a
    aa
    aaa
    aah
    aahed
    aahing
    aahs
    aal
    ...
    zwiebacks
    zwieselite
    zwinglian
    zwinglianism
    zwinglianist
    zwitter
    zwitterion
    zwitterionic
    ```

3. Split the dictionary wordlist into separate files based on the first letter of each word.

    To split an English wordlist the `split_wordlist_alpha.sh` script can be used like so:
    ```console
    $ split_wordlist_alpha.sh my_wordlist.txt . 
    ```
    This will generate a series of sub-dictionaries for each letter in the alphabet in the current directory.
    ```console
    $ ls
    my_wordlist.txt  words_d.txt  words_h.txt  words_l.txt  words_p.txt  words_t.txt  words_x.txt
    words_a.txt      words_e.txt  words_i.txt  words_m.txt  words_q.txt  words_u.txt  words_y.txt
    words_b.txt      words_f.txt  words_j.txt  words_n.txt  words_r.txt  words_v.txt  words_z.txt
    words_c.txt      words_g.txt  words_k.txt  words_o.txt  words_s.txt  words_w.txt
    ```

# Usage
```console
$ python boggler.py
Usage: python3 boggler.py <BOARD_FILE> <WORDLISTS_DIR> [MAX_WORD_LENGTH]
$ python boggler.py board.csv wordlists/ 15
Reading in wordlists...
>> d: words_d.txt
>> e: words_e.txt
>> f: words_f.txt
>> m: words_m.txt
>> n: words_n.txt
>> o: words_o.txt
>> qu: words_q.txt
>> r: words_r.txt
>> s: words_s.txt
>> v: words_v.txt
>> y: words_y.txt
Generating WordTrees...
>> (0, 0): y
>> (0, 1): e
>> (0, 2): o
>> (0, 3): s
>> (1, 0): r
>> (1, 1): e
>> (1, 2): o
>> (1, 3): v
>> (2, 0): d
>> (2, 1): f
>> (2, 2): e
>> (2, 3): y
>> (3, 0): n
>> (3, 1): m
>> (3, 2): e
>> (3, 3): qu

BOARD
+---------------+
| Y | E | O | S |
+---------------+
| R | E | O | V |
+---------------+
| D | F | E | Y |
+---------------+
| N | M | E |QU |
+---------------+


Starting @ (0, 0)...
y              : [(0, 0)]
yr             : [(0, 0), (1, 0)]
ye             : [(0, 0), (1, 1)]
yee            : [(0, 0), (1, 1), (0, 1)]
yeo            : [(0, 0), (1, 1), (0, 2)]
yed            : [(0, 0), (1, 1), (2, 0)]
yee            : [(0, 0), (1, 1), (2, 2)]
yer            : [(0, 0), (1, 1), (1, 0)]
yere           : [(0, 0), (1, 1), (1, 0), (0, 1)]
yerd           : [(0, 0), (1, 1), (1, 0), (2, 0)]
yeo            : [(0, 0), (1, 1), (1, 2)]
ye             : [(0, 0), (0, 1)]
yee            : [(0, 0), (0, 1), (1, 1)]
yer            : [(0, 0), (0, 1), (1, 0)]
yerd           : [(0, 0), (0, 1), (1, 0), (2, 0)]
yere           : [(0, 0), (0, 1), (1, 0), (1, 1)]
yeo            : [(0, 0), (0, 1), (1, 2)]
yeo            : [(0, 0), (0, 1), (0, 2)]

Starting @ (0, 1)...
e              : [(0, 1)]
ee             : [(0, 1), (1, 1)]
eer            : [(0, 1), (1, 1), (1, 0)]
eery           : [(0, 1), (1, 1), (1, 0), (0, 0)]
er             : [(0, 1), (1, 0)]
erd            : [(0, 1), (1, 0), (2, 0)]
erf            : [(0, 1), (1, 0), (2, 1)]
ere            : [(0, 1), (1, 0), (1, 1)]
eo             : [(0, 1), (1, 2)]
eos            : [(0, 1), (1, 2), (0, 3)]
eof            : [(0, 1), (1, 2), (2, 1)]
ey             : [(0, 1), (0, 0)]
eyr            : [(0, 1), (0, 0), (1, 0)]
eyre           : [(0, 1), (0, 0), (1, 0), (1, 1)]
eye            : [(0, 1), (0, 0), (1, 1)]
eyed           : [(0, 1), (0, 0), (1, 1), (2, 0)]
eyer           : [(0, 1), (0, 0), (1, 1), (1, 0)]
eo             : [(0, 1), (0, 2)]
eos            : [(0, 1), (0, 2), (0, 3)]

Starting @ (0, 2)...
o              : [(0, 2)]
oos            : [(0, 2), (1, 2), (0, 3)]
oof            : [(0, 2), (1, 2), (2, 1)]
oe             : [(0, 2), (1, 1)]
oer            : [(0, 2), (1, 1), (1, 0)]
ovey           : [(0, 2), (1, 3), (2, 2), (2, 3)]
oe             : [(0, 2), (0, 1)]
oer            : [(0, 2), (0, 1), (1, 0)]
os             : [(0, 2), (0, 3)]

Starting @ (0, 3)...
s              : [(0, 3)]
sv             : [(0, 3), (1, 3)]
so             : [(0, 3), (1, 2)]
sooey          : [(0, 3), (1, 2), (0, 2), (1, 1), (0, 0)]
sooey          : [(0, 3), (1, 2), (0, 2), (0, 1), (0, 0)]
soe            : [(0, 3), (1, 2), (0, 1)]
soe            : [(0, 3), (1, 2), (2, 2)]
sofer          : [(0, 3), (1, 2), (2, 1), (1, 1), (1, 0)]
soy            : [(0, 3), (1, 2), (2, 3)]
soe            : [(0, 3), (1, 2), (1, 1)]
sov            : [(0, 3), (1, 2), (1, 3)]
so             : [(0, 3), (0, 2)]
sooey          : [(0, 3), (0, 2), (1, 2), (0, 1), (0, 0)]
sooey          : [(0, 3), (0, 2), (1, 2), (2, 2), (2, 3)]
sooey          : [(0, 3), (0, 2), (1, 2), (1, 1), (0, 0)]
soe            : [(0, 3), (0, 2), (1, 1)]
sov            : [(0, 3), (0, 2), (1, 3)]
soe            : [(0, 3), (0, 2), (0, 1)]

Starting @ (1, 0)...
r              : [(1, 0)]
rye            : [(1, 0), (0, 0), (1, 1)]
rye            : [(1, 0), (0, 0), (0, 1)]
re             : [(1, 0), (0, 1)]
ree            : [(1, 0), (0, 1), (1, 1)]
reef           : [(1, 0), (0, 1), (1, 1), (2, 1)]
reed           : [(1, 0), (0, 1), (1, 1), (2, 0)]
rd             : [(1, 0), (2, 0)]
rf             : [(1, 0), (2, 1)]
re             : [(1, 0), (1, 1)]
ree            : [(1, 0), (1, 1), (0, 1)]
ref            : [(1, 0), (1, 1), (2, 1)]
red            : [(1, 0), (1, 1), (2, 0)]
ree            : [(1, 0), (1, 1), (2, 2)]
reem           : [(1, 0), (1, 1), (2, 2), (3, 1)]
reef           : [(1, 0), (1, 1), (2, 2), (2, 1)]

Starting @ (1, 1)...
e              : [(1, 1)]
ee             : [(1, 1), (0, 1)]
eer            : [(1, 1), (0, 1), (1, 0)]
eery           : [(1, 1), (0, 1), (1, 0), (0, 0)]
ey             : [(1, 1), (0, 0)]
eyr            : [(1, 1), (0, 0), (1, 0)]
eyre           : [(1, 1), (0, 0), (1, 0), (0, 1)]
eye            : [(1, 1), (0, 0), (0, 1)]
eyer           : [(1, 1), (0, 0), (0, 1), (1, 0)]
eo             : [(1, 1), (0, 2)]
eos            : [(1, 1), (0, 2), (0, 3)]
ef             : [(1, 1), (2, 1)]
ed             : [(1, 1), (2, 0)]
ee             : [(1, 1), (2, 2)]
er             : [(1, 1), (1, 0)]
ere            : [(1, 1), (1, 0), (0, 1)]
erd            : [(1, 1), (1, 0), (2, 0)]
erf            : [(1, 1), (1, 0), (2, 1)]
eo             : [(1, 1), (1, 2)]
eos            : [(1, 1), (1, 2), (0, 3)]
eof            : [(1, 1), (1, 2), (2, 1)]

Starting @ (1, 2)...
o              : [(1, 2)]
oos            : [(1, 2), (0, 2), (0, 3)]
oe             : [(1, 2), (0, 1)]
oer            : [(1, 2), (0, 1), (1, 0)]
os             : [(1, 2), (0, 3)]
oe             : [(1, 2), (2, 2)]
of             : [(1, 2), (2, 1)]
ofer           : [(1, 2), (2, 1), (1, 1), (1, 0)]
oy             : [(1, 2), (2, 3)]
oe             : [(1, 2), (1, 1)]
oer            : [(1, 2), (1, 1), (1, 0)]
ovey           : [(1, 2), (1, 3), (2, 2), (2, 3)]

Starting @ (1, 3)...
v              : [(1, 3)]
vs             : [(1, 3), (0, 3)]
vo             : [(1, 3), (0, 2)]
voe            : [(1, 3), (0, 2), (1, 1)]
voe            : [(1, 3), (0, 2), (0, 1)]
vee            : [(1, 3), (2, 2), (1, 1)]
veer           : [(1, 3), (2, 2), (1, 1), (1, 0)]
veery          : [(1, 3), (2, 2), (1, 1), (1, 0), (0, 0)]
vee            : [(1, 3), (2, 2), (3, 2)]
vefry          : [(1, 3), (2, 2), (2, 1), (1, 0), (0, 0)]
vo             : [(1, 3), (1, 2)]
voe            : [(1, 3), (1, 2), (0, 1)]
voe            : [(1, 3), (1, 2), (2, 2)]
voe            : [(1, 3), (1, 2), (1, 1)]

Starting @ (2, 0)...
d              : [(2, 0)]
dr             : [(2, 0), (1, 0)]
dry            : [(2, 0), (1, 0), (0, 0)]
dree           : [(2, 0), (1, 0), (0, 1), (1, 1)]
drey           : [(2, 0), (1, 0), (0, 1), (0, 0)]
dree           : [(2, 0), (1, 0), (1, 1), (0, 1)]
drey           : [(2, 0), (1, 0), (1, 1), (0, 0)]
dree           : [(2, 0), (1, 0), (1, 1), (2, 2)]
de             : [(2, 0), (1, 1)]
dee            : [(2, 0), (1, 1), (0, 1)]
deer           : [(2, 0), (1, 1), (0, 1), (1, 0)]
dey            : [(2, 0), (1, 1), (0, 0)]
def            : [(2, 0), (1, 1), (2, 1)]
dee            : [(2, 0), (1, 1), (2, 2)]
deem           : [(2, 0), (1, 1), (2, 2), (3, 1)]
der            : [(2, 0), (1, 1), (1, 0)]
dere           : [(2, 0), (1, 1), (1, 0), (0, 1)]
derf           : [(2, 0), (1, 1), (1, 0), (2, 1)]
dn             : [(2, 0), (3, 0)]
dm             : [(2, 0), (3, 1)]

Starting @ (2, 1)...
f              : [(2, 1)]
fe             : [(2, 1), (1, 1)]
fee            : [(2, 1), (1, 1), (0, 1)]
feer           : [(2, 1), (1, 1), (0, 1), (1, 0)]
fey            : [(2, 1), (1, 1), (0, 0)]
feyer          : [(2, 1), (1, 1), (0, 0), (0, 1), (1, 0)]
fed            : [(2, 1), (1, 1), (2, 0)]
fedn           : [(2, 1), (1, 1), (2, 0), (3, 0)]
fee            : [(2, 1), (1, 1), (2, 2)]
fer            : [(2, 1), (1, 1), (1, 0)]
fere           : [(2, 1), (1, 1), (1, 0), (0, 1)]
ferd           : [(2, 1), (1, 1), (1, 0), (2, 0)]
fr             : [(2, 1), (1, 0)]
fry            : [(2, 1), (1, 0), (0, 0)]
free           : [(2, 1), (1, 0), (0, 1), (1, 1)]
freed          : [(2, 1), (1, 0), (0, 1), (1, 1), (2, 0)]
frey           : [(2, 1), (1, 0), (0, 1), (0, 0)]
free           : [(2, 1), (1, 0), (1, 1), (0, 1)]
frey           : [(2, 1), (1, 0), (1, 1), (0, 0)]
fred           : [(2, 1), (1, 0), (1, 1), (2, 0)]
free           : [(2, 1), (1, 0), (1, 1), (2, 2)]
fo             : [(2, 1), (1, 2)]
foo            : [(2, 1), (1, 2), (0, 2)]
foe            : [(2, 1), (1, 2), (0, 1)]
foe            : [(2, 1), (1, 2), (2, 2)]
foy            : [(2, 1), (1, 2), (2, 3)]
foe            : [(2, 1), (1, 2), (1, 1)]
fm             : [(2, 1), (3, 1)]
fn             : [(2, 1), (3, 0)]
fe             : [(2, 1), (3, 2)]
fee            : [(2, 1), (3, 2), (2, 2)]
fey            : [(2, 1), (3, 2), (2, 3)]
fem            : [(2, 1), (3, 2), (3, 1)]
feme           : [(2, 1), (3, 2), (3, 1), (2, 2)]
fe             : [(2, 1), (2, 2)]
fee            : [(2, 1), (2, 2), (1, 1)]
feed           : [(2, 1), (2, 2), (1, 1), (2, 0)]
feer           : [(2, 1), (2, 2), (1, 1), (1, 0)]
feere          : [(2, 1), (2, 2), (1, 1), (1, 0), (0, 1)]
fee            : [(2, 1), (2, 2), (3, 2)]
fem            : [(2, 1), (2, 2), (3, 1)]
feme           : [(2, 1), (2, 2), (3, 1), (3, 2)]
fey            : [(2, 1), (2, 2), (2, 3)]

Starting @ (2, 2)...
e              : [(2, 2)]
eo             : [(2, 2), (1, 2)]
eos            : [(2, 2), (1, 2), (0, 3)]
eof            : [(2, 2), (1, 2), (2, 1)]
ee             : [(2, 2), (1, 1)]
eer            : [(2, 2), (1, 1), (1, 0)]
eery           : [(2, 2), (1, 1), (1, 0), (0, 0)]
evoe           : [(2, 2), (1, 3), (0, 2), (1, 1)]
evoe           : [(2, 2), (1, 3), (0, 2), (0, 1)]
evoe           : [(2, 2), (1, 3), (1, 2), (0, 1)]
evoe           : [(2, 2), (1, 3), (1, 2), (1, 1)]
ee             : [(2, 2), (3, 2)]
em             : [(2, 2), (3, 1)]
emf            : [(2, 2), (3, 1), (2, 1)]
eme            : [(2, 2), (3, 1), (3, 2)]
ef             : [(2, 2), (2, 1)]
ey             : [(2, 2), (2, 3)]
eye            : [(2, 2), (2, 3), (3, 2)]

Starting @ (2, 3)...
y              : [(2, 3)]
yo             : [(2, 3), (1, 2)]
yoe            : [(2, 3), (1, 2), (0, 1)]
yoe            : [(2, 3), (1, 2), (2, 2)]
yoe            : [(2, 3), (1, 2), (1, 1)]
yquem          : [(2, 3), (3, 3), (2, 2), (3, 1)]
yquem          : [(2, 3), (3, 3), (3, 2), (3, 1)]
ye             : [(2, 3), (3, 2)]
yee            : [(2, 3), (3, 2), (2, 2)]
ye             : [(2, 3), (2, 2)]
yeo            : [(2, 3), (2, 2), (1, 2)]
yee            : [(2, 3), (2, 2), (1, 1)]
yee            : [(2, 3), (2, 2), (3, 2)]

Starting @ (3, 0)...
n              : [(3, 0)]
nd             : [(3, 0), (2, 0)]
nm             : [(3, 0), (3, 1)]

Starting @ (3, 1)...
m              : [(3, 1)]
mf             : [(3, 1), (2, 1)]
mfr            : [(3, 1), (2, 1), (1, 0)]
mfd            : [(3, 1), (2, 1), (2, 0)]
md             : [(3, 1), (2, 0)]
me             : [(3, 1), (2, 2)]
meo            : [(3, 1), (2, 2), (1, 2)]
mee            : [(3, 1), (2, 2), (1, 1)]
meed           : [(3, 1), (2, 2), (1, 1), (2, 0)]
meer           : [(3, 1), (2, 2), (1, 1), (1, 0)]
mev            : [(3, 1), (2, 2), (1, 3)]
mee            : [(3, 1), (2, 2), (3, 2)]
mn             : [(3, 1), (3, 0)]
me             : [(3, 1), (3, 2)]
mee            : [(3, 1), (3, 2), (2, 2)]

Starting @ (3, 2)...
e              : [(3, 2)]
ee             : [(3, 2), (2, 2)]
ef             : [(3, 2), (2, 1)]
ey             : [(3, 2), (2, 3)]
eye            : [(3, 2), (2, 3), (2, 2)]
em             : [(3, 2), (3, 1)]
emf            : [(3, 2), (3, 1), (2, 1)]
eme            : [(3, 2), (3, 1), (2, 2)]
emeer          : [(3, 2), (3, 1), (2, 2), (1, 1), (1, 0)]

Starting @ (3, 3)...
qu             : [(3, 3)]
que            : [(3, 3), (2, 2)]
queer          : [(3, 3), (2, 2), (1, 1), (1, 0)]
queery         : [(3, 3), (2, 2), (1, 1), (1, 0), (0, 0)]
quem           : [(3, 3), (2, 2), (3, 1)]
queme          : [(3, 3), (2, 2), (3, 1), (3, 2)]
quey           : [(3, 3), (2, 2), (2, 3)]
que            : [(3, 3), (3, 2)]
quey           : [(3, 3), (3, 2), (2, 3)]
quem           : [(3, 3), (3, 2), (3, 1)]
queme          : [(3, 3), (3, 2), (3, 1), (2, 2)]
```