chipta={
    "id":              "",
    "ism":              "",
    "sharifi":          "",
    "yonalish":         "",
    "reys_raqami":      "",
    "orni":             "",
    "vagon":            "",
    "klass":            "",
}

# chipta2=chipta.copy()
vagon1={
    "tur":          "",
    "orinlar_soni":     "",
    "vagon_raqami":     "",
    "yo'lovchilar":     [],
}
poyezd={
    "poyezd_id":        "",
    "poyezd_mashinist": "",
    "vagonlar":         [],
}
rels={
    "yo'nalish":        [[],[]],
    "vaqti":            [],
    "poyezd":           []
}
def chipta_sotish():
    ism=input("ismni kiriting: ")
    sharif=input("Familiya: ")
    yonalish=input("yonalish: ")
    yangi_chipta=chipta.copy()
    yangi_chipta.update({"ism": ism})
    yangi_chipta.update({"sharif": ism})
    yangi_chipta.update({"yonalish": yonalish})
    return yangi_chipta
def vagonlar():
    turi=input("turi: ")