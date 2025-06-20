from replacer import Replacer
from command import LeafCommander, StemCommander
from jayson import Jayson
from message_builder import MessageForm
from sugar import str_none, none
from splash import Splash
import random
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

def channel_extractor(command : str):
    return int(command.removeprefix(" ").removeprefix("<#").removesuffix(" ").removesuffix(">"))

def set_jay(jayson : Jayson, prompt : str, suf : str, key, val):
    jayson({key: val})
    return prompt + str(val) + suf

channel_editor = StemCommander(
    {
        "set ": LeafCommander(lambda edit, msg: set_jay(jay, "set channel to: <#", ">", "channel", channel_extractor(msg))),
        "get ": LeafCommander(lambda edit, msg: jay["channel"])
    }
)

meta = StemCommander(
    {
        "channel ": channel_editor
    }
)

interaction = StemCommander(
    {
        "meta ": meta,
        "!errorTest":
            LeafCommander(lambda x, word: 0/0),
        "save ": LeafCommander(lambda x, y: saver(y)),
        "read ": LeafCommander(lambda x, word: typifier(uwuifier(str_none(jay[word], "", "wat " + word)))),
        "greet": 
        LeafCommander(((lambda x,y: "Hewwo!"), lambda x,y: channel_extractor(y))),
        "roll ": LeafCommander(lambda x, number: str(random.randint(1, int(number))))
    },
    default=
        LeafCommander(lambda x, word: typifier(uwuifier(word.lower()) or ""))
)

call = StemCommander({"$": interaction})

prolly_uwu = (lambda x : (uwuifier(x) if random.randint(0,1) == 1 else x))

greeter = Splash(
    [
        "a wild %s appeared",
        "hello %s",
        "ayooooo %s",
        "%s come here, imma squeesh u",
        "%s now exists",
        "finally, some %s"
    ]
)

squeesher = Splash(["%s","%s the squeesh","%s UwU"])