hallgatok = [
    {
        'id': 0,
        'name': 'test_name_1',
        'kepzes': 'bsc',
        'spec': 'aut',
        'NEPTUN': 'AAAAAA',
        'TODO': [],
        'Active': False,
        'Subject': ''
    },
    {
        'id': 1,
        'name': 'test_name_2',
        'NEPTUN': 'BBBBBB',
        'kepzes': 'bsc',
        'spec': 'aut',
        'TODO': [0, 1, 2, 3],
        'Active': False,
        'Subject':''
    }
]
TodoList = [
    {'deadline': '2018.09.02.', 'text': 'Neptun tárgyfelvétel	',
        'responsible': 'Hallgató'	},
    {'deadline': '2018.09.23.', 'text': 'AUT portál: Témajelentkezés	',
        'responsible': 'Hallgató'	},
    {'deadline': '2018.09.23.', 'text': 'Diplomaterv portál: Téma megnyitása	',
        'responsible': 'Konzulens'	},
    {'deadline': '2018.09.30.', 'text': 'Diplomaterv portál: Elbocsájtó-befogadó nyilatkozat vagy dékánhelyettesi engedély feltöltése	', 'responsible': 'Hallgató'	},
    {'deadline': '2018.10.07.', 'text': 'Diplomaterv portál: Feladatkiírás feltöltése	',
        'responsible': 'Konzulens'	},
    {'deadline': '2018.10.14.', 'text': 'Diplomaterv portál: Adatlap kitöltése	',
        'responsible': 'Hallgató'	},
    {'deadline': '2018.10.15.', 'text': 'Diplomaterv portál: Feladatkiírás jóváhagyása	',
        'responsible': 'Tanszékvezető'	},
    {'deadline': '2018.10.15.', 'text': 'Diplomaterv portál: Adatlap jóváhagyása	',
        'responsible': 'Konzulens'	},
    {'deadline': '2018.12.07.', 'text': 'Diplomaterv portál: Dolgozat beadása	',
        'responsible': 'Hallgató'	},
    {'deadline': '2018.12.17.', 'text': 'Diplomaterv portál: Dolgozat beadás jóváhagyása	',
        'responsible': 'Konzulens'	},
    {'deadline': '2019.01.27.', 'text': 'Diplomaterv portál: Bírálat feltöltés	',
        'responsible': 'Konzulens'}
]

tantargyak = [
    {'kepzes': 'bsc', 'spec': 'aut', 'targyak': [{'nev': 'Beágyazott operációs rendszerek és kliens alkalmazások', 'targykod': 'VIAUAC07'}, {
        'nev': 'Mikrokontroller alapú rendszerek', 'targykod': 'VIAUAC06'}]},
]
beosztas = {
    'test_name_1': '2019.jan.05 12:00',
    'test_name_2': '2019.jan.05 12:10'
}

if __name__ == "__main__":
    import json

    hallg = open('hallgatok.json', 'w')
    json.dump(hallgatok, hallg, ensure_ascii=False)

    tdlist = open('todolist.json', 'w')
    json.dump(TodoList, tdlist, ensure_ascii=False)

    subjects = open('tantargyak.json', 'w')
    json.dump(tantargyak, subjects, ensure_ascii=False)

    sched = open('beosztas.json', 'w')
    json.dump(beosztas, sched, ensure_ascii=False)
