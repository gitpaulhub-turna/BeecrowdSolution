a=input()
b=input()
c=input()

d={
    'vertebrado':
        {'ave':
         {
            'carnivoro':'aguia',
            'onivoro':'pomba'
            },

        'mamifero':
            {'onivoro':'homem',
             'herbivoro':'vaca'
         }},
        
    'invertebrado':
        {'inseto':
         {'hematofago':'pulga',
          'herbivoro':'lagarta'},
          'anelideo':
          {'hematofago':'sanguessuga',
           'onivoro':'minhoca'}
           }

}
print(d[a][b][c])
