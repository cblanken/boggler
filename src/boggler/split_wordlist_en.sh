#!/bin/sh

if [ -z $1 ] || [ -z $2 ]; then
    echo "Usage: WORDLIST OUT_DIR"
    exit 0
else
    grep -ioP "^a[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_a.txt" 
    grep -ioP "^b[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_b.txt"
    grep -ioP "^c[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_c.txt"
    grep -ioP "^d[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_d.txt"
    grep -ioP "^e[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_e.txt"
    grep -ioP "^f[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_f.txt"
    grep -ioP "^g[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_g.txt"
    grep -ioP "^h[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_h.txt"
    grep -ioP "^i[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_i.txt"
    grep -ioP "^j[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_j.txt"
    grep -ioP "^k[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_k.txt"
    grep -ioP "^l[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_l.txt"
    grep -ioP "^m[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_m.txt"
    grep -ioP "^n[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_n.txt"
    grep -ioP "^o[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_o.txt"
    grep -ioP "^p[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_p.txt"
    grep -ioP "^q[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_q.txt"
    grep -ioP "^r[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_r.txt"
    grep -ioP "^s[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_s.txt"
    grep -ioP "^t[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_t.txt"
    grep -ioP "^u[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_u.txt"
    grep -ioP "^v[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_v.txt"
    grep -ioP "^w[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_w.txt"
    grep -ioP "^x[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_x.txt"
    grep -ioP "^y[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_y.txt"
    grep -ioP "^z[a-z]+" $1 | tr [A-Z] [a-z] | sort | uniq > "$2/words_z.txt"
    touch "$2/words__.txt"
    exit 0
fi
