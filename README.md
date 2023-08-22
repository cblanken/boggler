# Boggler
A solver for the popular word game Boggle.

# Install
```console
pip install boggler
```

# Setup
To use the script to solve a Boggle board, you'll need to do a few things first.
1. Create `.csv` of the board state like so:

    Here is an example `board.csv`. Note the orientation of the board does not matter.
    ```console
    $ cat board.csv
    y,e,o,s
    r,e,o,v
    d,f,e,y
    n,m,e,qu
    ```
2. Find or create a dictionary wordlist file or create your own

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
<details>
<summary><h3 style="display: inline">CLI usage</h3></summary>
<pre><code>$ poetry run boggler --help
usage: boggler [-h] [-f FORMAT] [-p] [-s] [-d] board wordlists [max_word_length]

Boggle board game solver

positional arguments:
  board                 Path to board CSV file
  wordlists             Path to directory of wordlist files. The directory must contain text files of the form words_X.txt where "X" is a character of the
                        alphabet
  max_word_length       Maximum length of words searched for on provided board

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        Specify alternative output format including [txt, json]
  -p, --include-path    Include full paths for each word in output
  -s, --sort            Sort output alphabetically. By default the results are sorted by the starting block position on the board from top-to-bottom, left-
                        to-right as given in the board file.
  -d, --dedup           Remove duplicates from word-only output. Note that de-duplication does not preserve the original order of the output, so it is
                        recommended to also use the sort option when de-duplicating.
</code></pre>
</details>

<details>
<summary><h3 style="display: inline">Example board solve</h3></summary>
<pre><code>$ poetry run boggler ./boggler/boards/b1.csv boggler/wordlists/scrabble_2019/

BOARD
+---------------+
| S | A | I | P |
+---------------+
| L |QU | A | Y |
+---------------+
| U | L | L | S |
+---------------+
| O | W | H | A |
+---------------+

                               Starting @ (0, 0)
╭──────────┬──────────────────────────────────────────────────────────────────╮
│ Word     │ Path                                                             │
├──────────┼──────────────────────────────────────────────────────────────────┤
│ squall   │ [(0, 0), (1, 1), (0, 1), (1, 0), (2, 1)]                         │
│ squall   │ [(0, 0), (1, 1), (1, 2), (2, 2), (2, 1)]                         │
│ squall   │ [(0, 0), (1, 1), (1, 2), (2, 1), (1, 0)]                         │
│ squall   │ [(0, 0), (1, 1), (1, 2), (2, 1), (2, 2)]                         │
│ squally  │ [(0, 0), (1, 1), (1, 2), (2, 1), (2, 2), (1, 3)]                 │
│ squalls  │ [(0, 0), (1, 1), (1, 2), (2, 1), (2, 2), (2, 3)]                 │
│ squash   │ [(0, 0), (1, 1), (1, 2), (2, 3), (3, 2)]                         │
│ sal      │ [(0, 0), (0, 1), (1, 0)]                                         │
│ sall     │ [(0, 0), (0, 1), (1, 0), (2, 1)]                                 │
│ sallal   │ [(0, 0), (0, 1), (1, 0), (2, 1), (1, 2), (2, 2)]                 │
│ sallals  │ [(0, 0), (0, 1), (1, 0), (2, 1), (1, 2), (2, 2), (2, 3)]         │
│ sallow   │ [(0, 0), (0, 1), (1, 0), (2, 1), (3, 0), (3, 1)]                 │
│ sallowly │ [(0, 0), (0, 1), (1, 0), (2, 1), (3, 0), (3, 1), (2, 2), (1, 3)] │
│ sai      │ [(0, 0), (0, 1), (0, 2)]                                         │
╰──────────┴──────────────────────────────────────────────────────────────────╯
                      Starting @ (0, 1)
╭────────┬──────────────────────────────────────────────────╮
│ Word   │ Path                                             │
├────────┼──────────────────────────────────────────────────┤
│ aqua   │ [(0, 1), (1, 1), (1, 2)]                         │
│ aquas  │ [(0, 1), (1, 1), (1, 2), (2, 3)]                 │
│ al     │ [(0, 1), (1, 0)]                                 │
│ als    │ [(0, 1), (1, 0), (0, 0)]                         │
│ alu    │ [(0, 1), (1, 0), (2, 0)]                         │
│ alula  │ [(0, 1), (1, 0), (2, 0), (2, 1), (1, 2)]         │
│ alulas │ [(0, 1), (1, 0), (2, 0), (2, 1), (1, 2), (2, 3)] │
│ all    │ [(0, 1), (1, 0), (2, 1)]                         │
│ allay  │ [(0, 1), (1, 0), (2, 1), (1, 2), (1, 3)]         │
│ allays │ [(0, 1), (1, 0), (2, 1), (1, 2), (1, 3), (2, 3)] │
│ allow  │ [(0, 1), (1, 0), (2, 1), (3, 0), (3, 1)]         │
│ aa     │ [(0, 1), (1, 2)]                                 │
│ aal    │ [(0, 1), (1, 2), (2, 2)]                         │
│ aals   │ [(0, 1), (1, 2), (2, 2), (2, 3)]                 │
│ aal    │ [(0, 1), (1, 2), (2, 1)]                         │
│ aas    │ [(0, 1), (1, 2), (2, 3)]                         │
│ as     │ [(0, 1), (0, 0)]                                 │
│ ai     │ [(0, 1), (0, 2)]                                 │
│ aia    │ [(0, 1), (0, 2), (1, 2)]                         │
│ aias   │ [(0, 1), (0, 2), (1, 2), (2, 3)]                 │
╰────────┴──────────────────────────────────────────────────╯
Starting @ (0,
      2)
╭──────┬──────╮
│ Word │ Path │
├──────┼──────┤
╰──────┴──────╯
                          Starting @ (0, 3)
╭─────────┬──────────────────────────────────────────────────────────╮
│ Word    │ Path                                                     │
├─────────┼──────────────────────────────────────────────────────────┤
│ pya     │ [(0, 3), (1, 3), (1, 2)]                                 │
│ pyas    │ [(0, 3), (1, 3), (1, 2), (2, 3)]                         │
│ pa      │ [(0, 3), (1, 2)]                                         │
│ paal    │ [(0, 3), (1, 2), (0, 1), (1, 0)]                         │
│ paals   │ [(0, 3), (1, 2), (0, 1), (1, 0), (0, 0)]                 │
│ pal     │ [(0, 3), (1, 2), (2, 2)]                                 │
│ paly    │ [(0, 3), (1, 2), (2, 2), (1, 3)]                         │
│ palas   │ [(0, 3), (1, 2), (2, 2), (3, 3), (2, 3)]                 │
│ pall    │ [(0, 3), (1, 2), (2, 2), (2, 1)]                         │
│ pals    │ [(0, 3), (1, 2), (2, 2), (2, 3)]                         │
│ palsy   │ [(0, 3), (1, 2), (2, 2), (2, 3), (1, 3)]                 │
│ palsa   │ [(0, 3), (1, 2), (2, 2), (2, 3), (3, 3)]                 │
│ pal     │ [(0, 3), (1, 2), (2, 1)]                                 │
│ pall    │ [(0, 3), (1, 2), (2, 1), (1, 0)]                         │
│ palls   │ [(0, 3), (1, 2), (2, 1), (1, 0), (0, 0)]                 │
│ palla   │ [(0, 3), (1, 2), (2, 1), (1, 0), (0, 1)]                 │
│ pall    │ [(0, 3), (1, 2), (2, 1), (2, 2)]                         │
│ pally   │ [(0, 3), (1, 2), (2, 1), (2, 2), (1, 3)]                 │
│ palla   │ [(0, 3), (1, 2), (2, 1), (2, 2), (3, 3)]                 │
│ pallah  │ [(0, 3), (1, 2), (2, 1), (2, 2), (3, 3), (3, 2)]         │
│ pallahs │ [(0, 3), (1, 2), (2, 1), (2, 2), (3, 3), (3, 2), (2, 3)] │
│ palls   │ [(0, 3), (1, 2), (2, 1), (2, 2), (2, 3)]                 │
│ pas     │ [(0, 3), (1, 2), (2, 3)]                                 │
│ pash    │ [(0, 3), (1, 2), (2, 3), (3, 2)]                         │
│ pasha   │ [(0, 3), (1, 2), (2, 3), (3, 2), (3, 3)]                 │
│ pay     │ [(0, 3), (1, 2), (1, 3)]                                 │
│ pays    │ [(0, 3), (1, 2), (1, 3), (2, 3)]                         │
│ pi      │ [(0, 3), (0, 2)]                                         │
│ pia     │ [(0, 3), (0, 2), (1, 2)]                                 │
│ pial    │ [(0, 3), (0, 2), (1, 2), (2, 2)]                         │
│ pial    │ [(0, 3), (0, 2), (1, 2), (2, 1)]                         │
│ pias    │ [(0, 3), (0, 2), (1, 2), (2, 3)]                         │
│ pia     │ [(0, 3), (0, 2), (0, 1)]                                 │
│ pial    │ [(0, 3), (0, 2), (0, 1), (1, 0)]                         │
│ pias    │ [(0, 3), (0, 2), (0, 1), (0, 0)]                         │
╰─────────┴──────────────────────────────────────────────────────────╯
                 Starting @ (1, 0)
╭───────┬──────────────────────────────────────────╮
│ Word  │ Path                                     │
├───────┼──────────────────────────────────────────┤
│ la    │ [(1, 0), (0, 1)]                         │
│ las   │ [(1, 0), (0, 1), (0, 0)]                 │
│ lull  │ [(1, 0), (2, 0), (2, 1), (2, 2)]         │
│ lulls │ [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)] │
╰───────┴──────────────────────────────────────────╯
             Starting @ (1, 1)
╭───────┬──────────────────────────────────╮
│ Word  │ Path                             │
├───────┼──────────────────────────────────┤
│ qua   │ [(1, 1), (0, 1)]                 │
│ quai  │ [(1, 1), (0, 1), (0, 2)]         │
│ quip  │ [(1, 1), (0, 2), (0, 3)]         │
│ qua   │ [(1, 1), (1, 2)]                 │
│ quai  │ [(1, 1), (1, 2), (0, 2)]         │
│ quash │ [(1, 1), (1, 2), (2, 3), (3, 2)] │
│ quay  │ [(1, 1), (1, 2), (1, 3)]         │
│ quays │ [(1, 1), (1, 2), (1, 3), (2, 3)] │
╰───────┴──────────────────────────────────╯
                      Starting @ (1, 2)
╭────────┬──────────────────────────────────────────────────╮
│ Word   │ Path                                             │
├────────┼──────────────────────────────────────────────────┤
│ ai     │ [(1, 2), (0, 2)]                                 │
│ aia    │ [(1, 2), (0, 2), (0, 1)]                         │
│ aias   │ [(1, 2), (0, 2), (0, 1), (0, 0)]                 │
│ aa     │ [(1, 2), (0, 1)]                                 │
│ aal    │ [(1, 2), (0, 1), (1, 0)]                         │
│ aals   │ [(1, 2), (0, 1), (1, 0), (0, 0)]                 │
│ aas    │ [(1, 2), (0, 1), (0, 0)]                         │
│ al     │ [(1, 2), (2, 2)]                                 │
│ ala    │ [(1, 2), (2, 2), (3, 3)]                         │
│ alas   │ [(1, 2), (2, 2), (3, 3), (2, 3)]                 │
│ all    │ [(1, 2), (2, 2), (2, 1)]                         │
│ allow  │ [(1, 2), (2, 2), (2, 1), (3, 0), (3, 1)]         │
│ als    │ [(1, 2), (2, 2), (2, 3)]                         │
│ al     │ [(1, 2), (2, 1)]                                 │
│ all    │ [(1, 2), (2, 1), (1, 0)]                         │
│ alls   │ [(1, 2), (2, 1), (1, 0), (0, 0)]                 │
│ alow   │ [(1, 2), (2, 1), (3, 0), (3, 1)]                 │
│ alu    │ [(1, 2), (2, 1), (2, 0)]                         │
│ alula  │ [(1, 2), (2, 1), (2, 0), (1, 0), (0, 1)]         │
│ alulas │ [(1, 2), (2, 1), (2, 0), (1, 0), (0, 1), (0, 0)] │
│ all    │ [(1, 2), (2, 1), (2, 2)]                         │
│ ally   │ [(1, 2), (2, 1), (2, 2), (1, 3)]                 │
│ alls   │ [(1, 2), (2, 1), (2, 2), (2, 3)]                 │
│ as     │ [(1, 2), (2, 3)]                                 │
│ asyla  │ [(1, 2), (2, 3), (1, 3), (2, 2), (3, 3)]         │
│ ash    │ [(1, 2), (2, 3), (3, 2)]                         │
│ aqua   │ [(1, 2), (1, 1), (0, 1)]                         │
│ aquas  │ [(1, 2), (1, 1), (0, 1), (0, 0)]                 │
│ ay     │ [(1, 2), (1, 3)]                                 │
│ ays    │ [(1, 2), (1, 3), (2, 3)]                         │
╰────────┴──────────────────────────────────────────────────╯
         Starting @ (1, 3)
╭──────┬──────────────────────────╮
│ Word │ Path                     │
├──────┼──────────────────────────┤
│ yip  │ [(1, 3), (0, 2), (0, 3)] │
│ ya   │ [(1, 3), (1, 2)]         │
│ yap  │ [(1, 3), (1, 2), (0, 3)] │
│ yas  │ [(1, 3), (1, 2), (2, 3)] │
╰──────┴──────────────────────────╯
Starting @ (2,
      0)
╭──────┬──────╮
│ Word │ Path │
├──────┼──────┤
╰──────┴──────╯
                 Starting @ (2, 1)
╭───────┬──────────────────────────────────────────╮
│ Word  │ Path                                     │
├───────┼──────────────────────────────────────────┤
│ la    │ [(2, 1), (1, 2)]                         │
│ lap   │ [(2, 1), (1, 2), (0, 3)]                 │
│ las   │ [(2, 1), (1, 2), (2, 3)]                 │
│ lash  │ [(2, 1), (1, 2), (2, 3), (3, 2)]         │
│ lay   │ [(2, 1), (1, 2), (1, 3)]                 │
│ lays  │ [(2, 1), (1, 2), (1, 3), (2, 3)]         │
│ lo    │ [(2, 1), (3, 0)]                         │
│ lou   │ [(2, 1), (3, 0), (2, 0)]                 │
│ low   │ [(2, 1), (3, 0), (3, 1)]                 │
│ lowly │ [(2, 1), (3, 0), (3, 1), (2, 2), (1, 3)] │
╰───────┴──────────────────────────────────────────╯
                 Starting @ (2, 2)
╭───────┬──────────────────────────────────────────╮
│ Word  │ Path                                     │
├───────┼──────────────────────────────────────────┤
│ la    │ [(2, 2), (1, 2)]                         │
│ lap   │ [(2, 2), (1, 2), (0, 3)]                 │
│ lall  │ [(2, 2), (1, 2), (2, 1), (1, 0)]         │
│ lalls │ [(2, 2), (1, 2), (2, 1), (1, 0), (0, 0)] │
│ las   │ [(2, 2), (1, 2), (2, 3)]                 │
│ lash  │ [(2, 2), (1, 2), (2, 3), (3, 2)]         │
│ lay   │ [(2, 2), (1, 2), (1, 3)]                 │
│ lays  │ [(2, 2), (1, 2), (1, 3), (2, 3)]         │
│ la    │ [(2, 2), (3, 3)]                         │
│ las   │ [(2, 2), (3, 3), (2, 3)]                 │
│ lash  │ [(2, 2), (3, 3), (2, 3), (3, 2)]         │
│ lah   │ [(2, 2), (3, 3), (3, 2)]                 │
│ lahs  │ [(2, 2), (3, 3), (3, 2), (2, 3)]         │
╰───────┴──────────────────────────────────────────╯
                          Starting @ (2, 3)
╭─────────┬──────────────────────────────────────────────────────────╮
│ Word    │ Path                                                     │
├─────────┼──────────────────────────────────────────────────────────┤
│ sai     │ [(2, 3), (1, 2), (0, 2)]                                 │
│ sap     │ [(2, 3), (1, 2), (0, 3)]                                 │
│ sal     │ [(2, 3), (1, 2), (2, 2)]                                 │
│ sall    │ [(2, 3), (1, 2), (2, 2), (2, 1)]                         │
│ sallow  │ [(2, 3), (1, 2), (2, 2), (2, 1), (3, 0), (3, 1)]         │
│ sal     │ [(2, 3), (1, 2), (2, 1)]                                 │
│ sall    │ [(2, 3), (1, 2), (2, 1), (1, 0)]                         │
│ sall    │ [(2, 3), (1, 2), (2, 1), (2, 2)]                         │
│ sally   │ [(2, 3), (1, 2), (2, 1), (2, 2), (1, 3)]                 │
│ say     │ [(2, 3), (1, 2), (1, 3)]                                 │
│ sal     │ [(2, 3), (3, 3), (2, 2)]                                 │
│ salal   │ [(2, 3), (3, 3), (2, 2), (1, 2), (2, 1)]                 │
│ sall    │ [(2, 3), (3, 3), (2, 2), (2, 1)]                         │
│ sallow  │ [(2, 3), (3, 3), (2, 2), (2, 1), (3, 0), (3, 1)]         │
│ sh      │ [(2, 3), (3, 2)]                                         │
│ sha     │ [(2, 3), (3, 2), (3, 3)]                                 │
│ shaly   │ [(2, 3), (3, 2), (3, 3), (2, 2), (1, 3)]                 │
│ shall   │ [(2, 3), (3, 2), (3, 3), (2, 2), (2, 1)]                 │
│ shallow │ [(2, 3), (3, 2), (3, 3), (2, 2), (2, 1), (3, 0), (3, 1)] │
│ slap    │ [(2, 3), (2, 2), (1, 2), (0, 3)]                         │
│ slay    │ [(2, 3), (2, 2), (1, 2), (1, 3)]                         │
│ sly     │ [(2, 3), (2, 2), (1, 3)]                                 │
╰─────────┴──────────────────────────────────────────────────────────╯
                 Starting @ (3, 0)
╭───────┬──────────────────────────────────────────╮
│ Word  │ Path                                     │
├───────┼──────────────────────────────────────────┤
│ ou    │ [(3, 0), (2, 0)]                         │
│ olla  │ [(3, 0), (2, 1), (1, 0), (0, 1)]         │
│ ollas │ [(3, 0), (2, 1), (1, 0), (0, 1), (0, 0)] │
│ olla  │ [(3, 0), (2, 1), (2, 2), (1, 2)]         │
│ ollas │ [(3, 0), (2, 1), (2, 2), (1, 2), (2, 3)] │
│ olla  │ [(3, 0), (2, 1), (2, 2), (3, 3)]         │
│ ollas │ [(3, 0), (2, 1), (2, 2), (3, 3), (2, 3)] │
│ ow    │ [(3, 0), (3, 1)]                         │
│ owl   │ [(3, 0), (3, 1), (2, 1)]                 │
│ owl   │ [(3, 0), (3, 1), (2, 2)]                 │
│ owly  │ [(3, 0), (3, 1), (2, 2), (1, 3)]         │
│ owls  │ [(3, 0), (3, 1), (2, 2), (2, 3)]         │
╰───────┴──────────────────────────────────────────╯
                 Starting @ (3, 1)
╭───────┬──────────────────────────────────────────╮
│ Word  │ Path                                     │
├───────┼──────────────────────────────────────────┤
│ wull  │ [(3, 1), (2, 0), (1, 0), (2, 1)]         │
│ wull  │ [(3, 1), (2, 0), (2, 1), (1, 0)]         │
│ wulls │ [(3, 1), (2, 0), (2, 1), (1, 0), (0, 0)] │
│ wull  │ [(3, 1), (2, 0), (2, 1), (2, 2)]         │
│ wulls │ [(3, 1), (2, 0), (2, 1), (2, 2), (2, 3)] │
│ wo    │ [(3, 1), (3, 0)]                         │
│ wolly │ [(3, 1), (3, 0), (2, 1), (2, 2), (1, 3)] │
│ wha   │ [(3, 1), (3, 2), (3, 3)]                 │
╰───────┴──────────────────────────────────────────╯
                      Starting @ (3, 2)
╭────────┬──────────────────────────────────────────────────╮
│ Word   │ Path                                             │
├────────┼──────────────────────────────────────────────────┤
│ ha     │ [(3, 2), (3, 3)]                                 │
│ has    │ [(3, 2), (3, 3), (2, 3)]                         │
│ halal  │ [(3, 2), (3, 3), (2, 2), (1, 2), (2, 1)]         │
│ hall   │ [(3, 2), (3, 3), (2, 2), (2, 1)]                 │
│ hallo  │ [(3, 2), (3, 3), (2, 2), (2, 1), (3, 0)]         │
│ hallow │ [(3, 2), (3, 3), (2, 2), (2, 1), (3, 0), (3, 1)] │
╰────────┴──────────────────────────────────────────────────╯
                      Starting @ (3, 3)
╭────────┬──────────────────────────────────────────────────╮
│ Word   │ Path                                             │
├────────┼──────────────────────────────────────────────────┤
│ as     │ [(3, 3), (2, 3)]                                 │
│ asyla  │ [(3, 3), (2, 3), (1, 3), (2, 2), (1, 2)]         │
│ ash    │ [(3, 3), (2, 3), (3, 2)]                         │
│ al     │ [(3, 3), (2, 2)]                                 │
│ ala    │ [(3, 3), (2, 2), (1, 2)]                         │
│ alap   │ [(3, 3), (2, 2), (1, 2), (0, 3)]                 │
│ alas   │ [(3, 3), (2, 2), (1, 2), (2, 3)]                 │
│ alay   │ [(3, 3), (2, 2), (1, 2), (1, 3)]                 │
│ alays  │ [(3, 3), (2, 2), (1, 2), (1, 3), (2, 3)]         │
│ all    │ [(3, 3), (2, 2), (2, 1)]                         │
│ allay  │ [(3, 3), (2, 2), (2, 1), (1, 2), (1, 3)]         │
│ allays │ [(3, 3), (2, 2), (2, 1), (1, 2), (1, 3), (2, 3)] │
│ allow  │ [(3, 3), (2, 2), (2, 1), (3, 0), (3, 1)]         │
│ als    │ [(3, 3), (2, 2), (2, 3)]                         │
│ ah     │ [(3, 3), (3, 2)]                                 │
│ ahs    │ [(3, 3), (3, 2), (2, 3)]                         │
╰────────┴──────────────────────────────────────────────────╯
</code></pre>
</details>
<br>

# Build
Navigate to the project root folder and run the following.
Run `poetry build`

# License
The included [wordlists](src/boggler/wordlists) are covered by their respective licenses. All other files MIT © Cameron Blankenbuehler
