import re

# Patterns for detecting full words
word_pattern1 = r"(?<=\b|^)"  # Before the word
word_pattern2 = r"(?=\b|[,\.!?;:\s]|$)"  # After the word

# Patterns for detecting suffixes (identical to words, but applied to word endings)
suffix_pattern1 = r""  # Before the suffixe no constrainct
suffix_pattern2 = r"(?=\b|[,\.!?;:\s]|$)"  # After the suffixe

# Dictionary to standardize non-binary notations in translation evaluation and thus enable greater language flexibility.
normalization_rules = {
    # Full words
    "Un.e": [
        rf"{word_pattern1}(Un/Une|Un/une|Une/Un|Une/un|Un\.Une|Un\.une|Une\.Un|Une\.un|UnE|Un-e|Un ou une|Une ou un){word_pattern2}"
    ],
    "un.e": [
        rf"{word_pattern1}(un/une|une/un|un\.une|une\.un|unE|un-e|un ou une|une ou un){word_pattern2}"
    ],
    "Le.a": [
        rf"{word_pattern1}(Lea|Lia|Li|Lae|Le\.la|Le/La|Le/la|La\.le|La/le|La\.Le|La/Le|Le-a|Le ou la|La ou le){word_pattern2}"
    ],
    "le.a": [
        rf"{word_pattern1}(lea|lia|li|lae|le\.la|le/la|la\.le|la/le|le-a|le ou la|la ou le){word_pattern2}"
    ],
    "Iel": [
        rf"{word_pattern1}(Ille|Yel|Ielle|Ellui|Il/Elle|Il/elle|Il\.Elle|Il\.elle|Elle/Il|Elle/il|Elle\.Il|Elle\.il|Il ou elle|Elle ou il){word_pattern2}"
    ],
    "iel": [
        rf"{word_pattern1}(ille|yel|ielle|ellui|il/elle|il\.elle|elle/il|elle\.il|il ou elle|elle ou il){word_pattern2}"
    ],
    "Ce.tte": [
        rf"{word_pattern1}(Ce\.te|Cès|Cèx|Ce ou cette|Cette ou ce|Cette ou cet){word_pattern2}"
    ],
    "ce.tte": [
        rf"{word_pattern1}(ce\.te|cès|cèx|ce ou cette|cette ou ce|cette ou cet){word_pattern2}"
    ],

    # Suffixes
    "ien.ne": [
        rf"{suffix_pattern1}(ien\.ienne|ienE){suffix_pattern2}"
    ],
    "ier.ère": [
        rf"{suffix_pattern1}(ier\.ière|ierE){suffix_pattern2}"
    ],
    "eur.euse": [
        rf"{suffix_pattern1}(eur\.se){suffix_pattern2}"
    ],
    "eur.e": [
        rf"{suffix_pattern1}(eurE){suffix_pattern2}"
    ],
    "eux.euse": [
        rf"{suffix_pattern1}(eux\.se){suffix_pattern2}" 
    ],
    "tre.esse": [
        rf"{suffix_pattern1}(tre\.tresse|tre\.sse){suffix_pattern2}"
    ],
    "te.esse": [
        rf"{suffix_pattern1}(te\.sse){suffix_pattern2}"
    ]
}

# Function to apply non-binarity standardization rules
def non_binary_standardization(text):
    text = text.replace('·', '.').replace('•', '.') # interpuncts standardization
    for target, regex_list in normalization_rules.items():
        for regex in regex_list:
            text = re.sub(regex, target, text)
    return text


  