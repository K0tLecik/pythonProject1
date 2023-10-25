from polls.models import Person        
>>> Person.objects.all()
<QuerySet [<Person: Maciej Tatkowski>, <Person: Julia Żugaj>, <Person: Stanisław Wiercipięta>]>
>>> Person.objects.get(id=3) 
<Person: Maciej Tatkowski>
>>> Person.objects.filter(first_name__startswith='M')
<QuerySet [<Person: Maciej Tatkowski>]>           
>>> Person.objects.values_list('position__name', flat=True).distinct()        
<QuerySet ['Nauczyciel', 'Mechanik', 'IT']>
>>> Person.objects.values_list('position__name', flat=True).order_by('-position') 
<QuerySet ['IT', 'Mechanik', 'Nauczyciel']>
>>> Person.objects.values_list('position__name', flat=True).order_by('-position__name') 
<QuerySet ['Nauczyciel', 'Mechanik', 'IT']>
>>> new_person = Person(first_name='Jan', second_name='Matejko', gender='M')
>>> new_person.save()
>>> exit()

*Wywaliło błąd przez to, że moja nowa osoba nie miała pozycji, a dalej w kodzie jest linijka, która pobiera id pozycji danej osoby, przez co wszystko się wykrzaczyło. Część dalsza, naprawiająca błąd:*

from polls.models import Person, Position
>>> position_it = Position.objects.get(name='IT')
>>> person = Person.objects.get(first_name='Jan')
>>> person.position = position_it
>>> person.save()
>>> exit()

