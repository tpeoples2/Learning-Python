# Level 1

import string

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

ALPHABET = [letter for letter in string.lowercase]
NEW_ALPHABET = ALPHABET[2:]
NEW_ALPHABET.append("a")
NEW_ALPHABET.append("b")

ALPHABET = "".join(ALPHABET)
NEW_ALPHABET = "".join(NEW_ALPHABET)

TABLE = string.maketrans(ALPHABET, NEW_ALPHABET)

print string.translate(text, TABLE)

print string.translate("map", TABLE)
