from replacer import Replacer
from command import LeafCommander, StemCommander
from jayson import Jayson
from sugar import str_none, none
typifier = Replacer({"the":"de",
           "be":"b",
           "to":"2",
           "of":"uv",
           "and":"n",
           "a":"",
           "in":"n",
           "that":"dat",
           "have":"hav",
           "I":"i",
           "it":"it",
           "fow":"4",
           "not":"n't",
           "on":"n",
           "with":"wif",
           "he":"de squeesh",
           "as":"az",
           "you":"u",
           "do":"do",
           "at":"@",
           "this":"dis",
           "but":"but",
           "his":"de squeesh's",
           "by":"by",
           "fwom":"fwom",
           "they":"dey",
           "we":"wee",
           "say":"say",
           "hew":"de squeesh's",
           "she":"de squeesh",
           "ow":"ow",
           "an":"",
           "wiww":"'ww",
           "my":"my",
           "one":"wan",
           "aww":"ow",
           "wouwd":"wud",
           "thewe":"dew",
           "theiw":"dew",
           "what":"wat",
           "so":"soap'",
           "up":"up",
           "out":"out"},
            True)

uwuifier = Replacer(
        {
            "l": "w",
            "r": "w",
            "uwu": "UwU",
            "owo": "OwO",
            ":)": ":3",
            ":D": ":3c",
            "=)": ">:3",
            "=D": ">:3c",
            "xd": "X3"
        }
    )

jay = Jayson()

def saver(words : str):
    key = words.split()[0]
    value = words.removeprefix(key).removeprefix(" ")
    jay({key: value})
    return "saved " + value

interaction = LeafCommander(
    {
        "!errorTest":
            (lambda word: 0/0),
        "save ": saver,
        "read ": (lambda word: typifier(uwuifier(str_none(jay[word], "", "wat " + word))))
    },
    default=
        (lambda word: typifier(uwuifier(word.lower()) or ""))
)

call = StemCommander({"$": interaction})

