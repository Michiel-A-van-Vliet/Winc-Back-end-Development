Uitleg over de technische keuzes in opdracht SuperPy.

Eigenlijk is de enige keuze die ik heb gemaakt, om binnen mijn code de gegevens op te slaan in een lijst van woordenboeken. Ik had ook kunnen kiezen voor tupels of het in objecten kunnen stoppen. Deze keuze maakt de code leesbaar, zonder het onnodig ingewikkeld te maken.

Als extra's heb ik gedaan:
- tabelletjes met de 'Rich' module
- een rapport voor onverkochte producten die over de datum zijn
- afkortingen in de command line interface (bij onder andere 'buy' en 'sell')
- een custom check of ingevoerde datum aan ISO-norm voldoet
- een rapport voor uitgaven

Aangezien het me verstandig leek om bij het opslaan van rapporten unieke bestandsnamen te gebruiken, heb ik daarvoor "strftime" gebruikt. Ik kon geen zinvolle toepassing verzinnen voor "strptime". Het is logischer om "isoformat" en "fromisofrmat" te gebruiken bij "datetime.date" objecten.

Verder heb ik me zo veel mogelijk aan de opdracht gehouden en waar mogelijk de gegeven voorbeelden gebruikt.

Zie 'read_me.txt' voor uitleg over de werking van het programma. 
