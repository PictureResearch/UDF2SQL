
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../')

import synth

synth.synth({
   'body': """AString t1 = AString2(constString("name"), constString("age"));
AAny t4 = AAny2(t2, t3);
AStringAny t5 = AStringAny_zip(t1, t4);
MStringAny t6 = AStringAny_toMap(t5);""",
   'args': [("t2", "Any"), ("t3", "Any")],
   'ret': ("t6", "MStringAny"),
   'strings': ['"name"', '"age"'],
   'arg_map': ["$name", "$age"]
})
    