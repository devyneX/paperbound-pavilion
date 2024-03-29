from django.db import models


class GenreChoices(models.TextChoices):
    ACTION = 'action', 'Action'
    ADVENTURE = 'adventure', 'Adventure'
    FANTASY = 'fantasy', 'Fantasy'
    HORROR = 'horror', 'Horror'
    FICTION = 'fiction', 'Fiction'
    SPIRITUAL = 'spiritual', 'Spiritual'
    PHILOSOPHY = 'philosophy', 'Philosophy'
    MYSTERY = 'mystery', 'Mystery'
    ROMANCE = 'romance', 'Romance'
    SCIENCE_FICTION = 'science_fiction', 'Science Fiction'
    THRILLER = 'thriller', 'Thriller'
    WESTERN = 'western', 'Western'
    BIOGRAPHY = 'biography', 'Biography'
    AUTOBIOGRAPHY = 'autobiography', 'Autobiography'
    COMICS = 'comics', 'Comics'
    COOKBOOK = 'cookbook', 'Cookbook'
    DIARY = 'diary', 'Diary'
    DICTIONARY = 'dictionary', 'Dictionary'
    ENCYCLOPEDIA = 'encyclopedia', 'Encyclopedia'
    GUIDE = 'guide', 'Guide'
    HEALTH = 'health', 'Health'
    HISTORY = 'history', 'History'
    JOURNAL = 'journal', 'Journal'
    MATH = 'math', 'Math'
    MEMOIR = 'memoir', 'Memoir'
    PRAYER = 'prayer', 'Prayer'
    RELIGION = 'religion', 'Religion'
    TEXTBOOK = 'textbook', 'Textbook'
    POETRY = 'poetry', 'Poetry'
    PLAY = 'play', 'Play'
    SATIRE = 'satire', 'Satire'
    SCIENCE = 'science', 'Science'
    TRAVEL = 'travel', 'Travel'
    TRUE_CRIME = 'true_crime', 'True Crime'


class LanguageChoices(models.TextChoices):
    AA = 'aa', 'Afar'
    AB = 'ab', 'Abkhazian'
    AF = 'af', 'Afrikaans'
    AK = 'ak', 'Akan'
    SQ = 'sq', 'Albanian'
    AM = 'am', 'Amharic'
    AR = 'ar', 'Arabic'
    AN = 'an', 'Aragonese'
    HY = 'hy', 'Armenian'
    AS = 'as', 'Assamese'
    AV = 'av', 'Avaric'
    AE = 'ae', 'Avestan'
    AY = 'ay', 'Aymara'
    AZ = 'az', 'Azerbaijani'
    BA = 'ba', 'Bashkir'
    BM = 'bm', 'Bambara'
    EU = 'eu', 'Basque'
    BE = 'be', 'Belarusian'
    BN = 'bn', 'Bengali'
    BH = 'bh', 'Bihari languages'
    BI = 'bi', 'Bislama'
    BO = 'bo', 'Tibetan'
    BS = 'bs', 'Bosnian'
    BR = 'br', 'Breton'
    BG = 'bg', 'Bulgarian'
    MY = 'my', 'Burmese'
    CA = 'ca', 'Catalan; Valencian'
    CS = 'cs', 'Czech'
    CH = 'ch', 'Chamorro'
    CE = 'ce', 'Chechen'
    ZH = 'zh', 'Chinese'
    CU = 'cu', 'Church Slavic; Old Slavonic; Church Slavonic; \
        Old Bulgarian; Old Church Slavonic'

    CV = 'cv', 'Chuvash'
    KW = 'kw', 'Cornish'
    CO = 'co', 'Corsican'
    CR = 'cr', 'Cree'
    CY = 'cy', 'Welsh'
    DA = 'da', 'Danish'
    DE = 'de', 'German'
    DV = 'dv', 'Divehi; Dhivehi; Maldivian'
    NL = 'nl', 'Dutch; Flemish'
    DZ = 'dz', 'Dzongkha'
    EL = 'el', 'Greek, Modern (1453-)'
    EN = 'en', 'English'
    EO = 'eo', 'Esperanto'
    ET = 'et', 'Estonian'
    EE = 'ee', 'Ewe'
    FO = 'fo', 'Faroese'
    FA = 'fa', 'Persian'
    FJ = 'fj', 'Fijian'
    FI = 'fi', 'Finnish'
    FR = 'fr', 'French'
    FY = 'fy', 'Western Frisian'
    FF = 'ff', 'Fulah'
    GD = 'gd', 'Gaelic; Scottish Gaelic'
    GA = 'ga', 'Irish'
    GL = 'gl', 'Galician'
    GV = 'gv', 'Manx'
    GN = 'gn', 'Guarani'
    GU = 'gu', 'Gujarati'
    HT = 'ht', 'Haitian; Haitian Creole'
    HA = 'ha', 'Hausa'
    HE = 'he', 'Hebrew'
    HZ = 'hz', 'Herero'
    HI = 'hi', 'Hindi'
    HO = 'ho', 'Hiri Motu'
    HR = 'hr', 'Croatian'
    HU = 'hu', 'Hungarian'
    IG = 'ig', 'Igbo'
    IS = 'is', 'Icelandic'
    IO = 'io', 'Ido'
    II = 'ii', 'Sichuan Yi; Nuosu'
    IU = 'iu', 'Inuktitut'
    IE = 'ie', 'Interlingue; Occidental'
    IA = 'ia', 'Interlingua (International Auxiliary Language Association)'
    ID = 'id', 'Indonesian'
    IK = 'ik', 'Inupiaq'
    IT = 'it', 'Italian'
    JV = 'jv', 'Javanese'
    JA = 'ja', 'Japanese'
    KL = 'kl', 'Kalaallisut; Greenlandic'
    KN = 'kn', 'Kannada'
    KS = 'ks', 'Kashmiri'
    KA = 'ka', 'Georgian'
    KK = 'kk', 'Kazakh'
    KM = 'km', 'Central Khmer'
    KI = 'ki', 'Kikuyu; Gikuyu'
    RW = 'rw', 'Kinyarwanda'
    KY = 'ky', 'Kirghiz; Kyrgyz'
    KV = 'kv', 'Komi'
    KG = 'kg', 'Kongo'
    KO = 'ko', 'Korean'
    KJ = 'kj', 'Kuanyama; Kwanyama'
    KU = 'ku', 'Kurdish'
    LO = 'lo', 'Lao'
    LA = 'la', 'Latin'
    LV = 'lv', 'Latvian'
    LI = 'li', 'Limburgan; Limburger; Limburgish'
    LN = 'ln', 'Lingala'
    LT = 'lt', 'Lithuanian'
    LB = 'lb', 'Luxembourgish; Letzeburgesch'
    LU = 'lu', 'Luba-Katanga'
    LG = 'lg', 'Ganda'
    MK = 'mk', 'Macedonian'
    MH = 'mh', 'Marshallese'
    ML = 'ml', 'Malayalam'
    MI = 'mi', 'Maori'
    MR = 'mr', 'Marathi'
    MS = 'ms', 'Malay'
    MT = 'mt', 'Maltese'
    MN = 'mn', 'Mongolian'
    NA = 'na', 'Nauru'
    NV = 'nv', 'Navajo; Navaho'
    NR = 'nr', 'Ndebele, South; South Ndebele'
    ND = 'nd', 'Ndebele, North; North Ndebele'
    NE = 'ne', 'Nepali'
    NN = 'nn', 'Norwegian Nynorsk; Nynorsk, Norwegian'
    NB = 'nb', 'Bokmål, Norwegian; Norwegian Bokmål'
    NO = 'no', 'Norwegian'
    OC = 'oc', 'Occitan (post 1500)'
    OJ = 'oj', 'Ojibwa'
    OR = 'or', 'Oriya'
    OM = 'om', 'Oromo'
    OS = 'os', 'Ossetian'
