# Argument Handling
MATCH_MODE = "MATCH_MODE"
MERGE_MODE = "MERGE_MODE"

ENG_SCHEME = "eng"
ORTH_SCHEME = "orth"
IPA_SCHEME = "ipa"
JAP_SCHEME = "jap"
SCHEMES = {ENG_SCHEME, ORTH_SCHEME, IPA_SCHEME, JAP_SCHEME}

# Scheme Handling
VOWEL = "VOWEL"
CONSONANT = "CONSONANT"
EMPTY = "EMPTY"
CHAR_TYPES = [VOWEL, CONSONANT, EMPTY]
VOWEL_PATTERN = r"[aeiou]"
CONSONANT_PATTERN = r"[bcdfghjklmnpqrstvwxyzCS]"
ENG_CHUNKS = {"ch": "C", "sh": "S", "ph": "f",
              "ck": "k", "q": "k"}
