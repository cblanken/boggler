from itertools import chain
from pathlib import Path
import pytest
from boggler.boggler_utils import BoggleBoard, build_full_boggle_tree

WORDLISTS_DIR = Path("./boggler/wordlists/dwyl/").absolute()

@pytest.fixture
def board_4x4():
    return [
        ['u','n','r','e'],
        ['qu','n','i','l'],
        ['i','s','h','a'],
        ['s','e','l','b']
    ]

@pytest.fixture
def expected_words_max_4():
    return [
        "u", "un", "unn", "uns", "uni", "unie", "uni", "unie", "un", "unn", "uni",
        "unie", "n", "ni", "nis", "nisi", "nil", "nile", "nu", "nun", "nuns", "nr", "r",
        "rin", "rie", "riel", "risqu", "rise", "riss", "ria", "rial", "rial", "rin",
        "rins", "rile", "rn", "rle", "rn", "re", "rel", "rei", "rein", "reis", "rein",
        "e", "el", "ela", "elhi", "eli", "elia", "eir", "eila", "er", "erin", "eris",
        "eria", "erin", "ern", "erns", "ern", "qu", "qui", "quin", "quis", "quis", "n",
        "nu", "nun", "nr", "ns", "ni", "nis", "nies", "nies", "nis", "nisi", "ni",
        "nis", "nisi", "nil", "nile", "i", "ir", "ire", "in", "inn", "inns", "ie",
        "ihs", "is", "isn", "ise", "isl", "isle", "isis", "ish", "ia", "in", "inn",
        "ins", "il", "ile", "ila", "l", "le", "lei", "leis", "ler", "lr", "la", "lai",
        "lair", "lain", "lain", "lab", "lah", "lh", "lhb", "li", "lir", "lire", "lin",
        "linn", "lie", "lier", "lis", "lise", "liss", "lish", "lin", "linn", "lins",
        "i", "in", "inn", "ins", "inia", "is", "ise", "ie", "is", "isn", "ise", "isl",
        "isle", "ish", "s", "sn", "si", "sir", "sire", "sin", "sie", "sier", "sia",
        "sial", "sial", "sin", "sinh", "sil", "sile", "se", "sei", "seis", "sel", "ss",
        "ssi", "sl", "sla", "slab", "si", "sin", "sinh", "sis", "sise", "sie", "sh",
        "shi", "shin", "shia", "shin", "she", "shes", "shel", "sha", "shai", "shab",
        "h", "hi", "hir", "hire", "hin", "hie", "his", "hisn", "hiss", "hia", "hin",
        "hins", "hile", "hila", "hl", "hler", "hl", "he", "hes", "hei", "hein", "hes",
        "hel", "hb", "hs", "hsi", "hsi", "ha", "hal", "hale", "hair", "hain", "hain",
        "hail", "hab", "hal", "hals", "hale", "a", "al", "ale", "alin", "alin", "ai",
        "air", "airn", "airn", "aire", "ain", "ainu", "aiel", "ais", "ain", "ainu",
        "ains", "ail", "aile", "ab", "abl", "able", "al", "als", "ale", "ales", "ales",
        "alb", "ah", "ahi", "ahir", "ahs", "s", "si", "sin", "sins", "sinh", "sie",
        "sis", "sisi", "sise", "sish", "ss", "ssi", "ssi", "se", "sei", "seis", "sel",
        "sels", "e", "es", "ess", "eh", "es", "ess", "el", "elhi", "els", "ela", "elb",
        "l", "lh", "lhb", "ls", "la", "lai", "lair", "lain", "lain", "lab", "lah", "le",
        "les", "less", "lei", "leis", "leis", "lehi", "les", "less", "lb", "b", "ba",
        "bal", "bale", "balr", "bali", "bai", "bain", "bais", "bain", "bail", "bal",
        "bals", "bale", "bah", "bhil", "bl", "bls", "blah"
    ]

@pytest.fixture
def expected_words_max_20():
    return [
        "u","un","unn","unrelinquishable","unrelishable","unreliable","unrein","uns",
        "unsin","unslain","unshale","unshale","uni","unie","unhale","unhair","unhale",
        "uni","unie","un","unn","uni","unie","unrelishable","unreliable",
        "unrelinquishable","unrein","n","ni","nihal","nihal","nis","nisei","niseis",
        "nisse","nisi","nil","nile","nu","nun","nuns","nr","r","rin","rie",
        "riel","risqu","rise","rises","riss","rissel","ria","rial","rial",
        "rials","rin","rins","rinse","rinses","rile","rn","rle","rn",
        "re","rel","relais","relinquish","relinquishes","relish","relishes",
        "relishable","reliable","relinquish","relinquishes","rei","rein","reis",
        "rein","reins","e","el","ela","elain","elain","elains","elhi","eli","elisha",
        "elia","eir","eila","er","erin","eris","eria","erin","ern","erns","ernie",
        "ern","qu","qui","quin","quins","quinse","quinin","quiniela","quinia",
        "quis","quis","quisle","n","nu","nun","nr","ns","ni",
        "nis","nisse","nies","nies","niels","nis","nisi","nisse","ni",
        "nihal","nihal","nis","nisei","niseis","nisse","nisi","nil","nile",
        "i","ir","ire","in","inn","inns","ie","ihs","is",
        "isn","ise","issei","isl","isle","isles","isis","ish","ia",
        "in","inn","ins","inisle","inhale","inhaler","inhale","inhales","inhales",
        "il","ile","ila","l","le","lei","leis","leiss","ler",
        "lr","la","lai","lair","lain","laisse","lain","lab","lah",
        "lh","lhb","li","lir","lire","lin","linn","linns","linquish",
        "lie","lier","lis","lise","liss","lisle","lisles","lish","liable",
        "lin","linn","lins","linie","linha","linquish","i","in","inn",
        "ins","inhale","inhaler","inhale","inhales","inhales","inisle","inia","inial",
        "inial","is","ise","ie","is","isn","ise","isl","isle",
        "isles","ish","s","sn","snies","snirl","squin","squinnier","si",
        "sir","sire","sin","sie","sier","sia","sial","sial","sin",
        "sinh","sil","sile","se","sei","seis","sel","selah","ss",
        "ssi","sl","sla","slain","slain","slab","si","sin","sinh",
        "sis","sise","sisel","sie","sh","shi","shirl","shire","shin",
        "shinnies","shiel","shier","shia","shin","she","shes","shel","shela",
        "sha","shale","shalier","shai","shairn","shairn","shab","shale","shales",
        "h","hi","hir","hire","hin","hinnies","hinnies","hie","his",
        "hisn","hiss","hissel","hisis","hia","hin","hins","hile","hila",
        "hl","hler","hl","he","hes","hei","hein","heinie","hes",
        "hel","hb","hs","hsi","hsi","ha","hal","hale","haler",
        "hair","haire","hain","hain","hail","hailer","hab","hable","hal",
        "hals","halse","hale","hales","hales","a","al","ale","alin",
        "alish","alin","ai","air","airn","airns","airn","aire","ain",
        "ainu","aiel","ais","aisle","aisles","ain","ainu","ains","ail",
        "aile","ab","abl","able","ables","ables","al","als","ale",
        "ales","ales","alb","ah","ahi","ahir","ahs","s","si",
        "sin","sins","sinh","sinhs","sie","sis","sisi","sise","sisel",
        "sish","ss","ssi","ssi","se","sesqui","sesia","sei","seis",
        "seisin","seisin","sel","sels","selah","selahs","e","es","ess",
        "eshin","eshin","eh","es","ess","essie","el","elhi","els",
        "elsin","elsin","elsin","elshin","elshin","ela","elain","elain","elains",
        "elb","l","lh","lhb","ls","la","lai","lair","lain",
        "laisse","lain","lab","lah","le","les","less","lei","leis",
        "leiss","leis","leiss","lehi","les","less","lessn","lb","b",
        "ba","bal","bale","balei","baleise","baler","balr","bali","bai",
        "bairn","bairns","bairnie","bairnish","bairn","bain","bais","bain","bainie",
        "bail","baile","bailer","bal","bals","bale","bales","balei","bales",
        "bah","bhil","bl","bls","blair","blain","blain","blains","blah",
        "blahs","bless","bless"
    ]

# -----------------------------------------------------
# Solved board max 4-letter words
# -----------------------------------------------------

# Init for word tree (4 board_4x4 or less) and fixtures
@pytest.fixture
def board_4(board_4x4):
    return BoggleBoard(board_4x4, 4)

@pytest.fixture
def tree_4(board_4):
    return build_full_boggle_tree(board_4, Path(WORDLISTS_DIR))

@pytest.fixture
def found_words_4(tree_4):
    return list(chain.from_iterable([x.word_paths for x in tree_4.values()]))

# Tests for solved board with max of 4-letter words
def test_word_count_4_board_4x4_max(expected_words_max_4, tree_4):
    assert len(expected_words_max_4) == sum(map(lambda x: len(x.word_paths), tree_4.values()))

def test_words_full_4_board_4x4_max(expected_words_max_4, found_words_4, tree_4):
    found_words = [x.word_paths for x in tree_4.values()]
    for letter, subtree in tree_4.items():
        for i in range(0, min(len(expected_words_max_4), len(found_words_4))):
            assert expected_words_max_4[i] == found_words_4[i][0]

def test_format_words_4_to_csv():
    pass

def test_format_words_4_to_json():
    pass


# -----------------------------------------------------
# Solved board max 20-letter words
# -----------------------------------------------------

# Init for word tree (20 board_4x4 or less) and fixtures
@pytest.fixture
def board_20(board_4x4):
    return BoggleBoard(board_4x4, 20)

@pytest.fixture
def tree_20(board_20):
    return build_full_boggle_tree(board_20, WORDLISTS_DIR)

@pytest.fixture
def found_words_20(tree_20):
    return list(chain.from_iterable([x.word_paths for x in tree_20.values()]))

# Tests for solved board with max of 20-letter words
def test_word_count_20_board_4x4_max(expected_words_max_20, tree_20):
    assert len(expected_words_max_20) == sum(map(lambda x: len(x.word_paths), tree_20.values()))

def test_words_full_20_board_4x4_max(expected_words_max_20, found_words_20, tree_20):
    found_words = [x.word_paths for x in tree_20.values()]
    for letter, subtree in tree_20.items():
        for i in range(0, min(len(expected_words_max_20), len(found_words_20))):
            assert expected_words_max_20[i] == found_words_20[i][0]

def test_format_words_20_to_csv():
    pass

def test_format_words_20_to_json():
    pass
