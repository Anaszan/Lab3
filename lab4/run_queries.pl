% Runner to execute example queries for Lab 4
:- initialization(main).

main :-
    consult('family.pl'),
    nl, write('--- Query: mother(X, manee) ---'), nl,
    (   mother(X, manee)
    ->  write('X = '), write(X), nl
    ;   write('No result'), nl
    ),

    nl, write('--- Query: descendant(X, somchai) ---'), nl,
    (   setof(D, descendant(D, somchai), Ds)
    ->  write(Ds), nl
    ;   write([]), nl
    ),

    nl, write('--- Query: cousin(prayut, somyot) ---'), nl,
    (   cousin(prayut, somyot)
    ->  write('true'), nl
    ;   write('false'), nl
    ),

    nl, write('--- Query: aunt(X, manee) ---'), nl,
    findall(A, aunt(A, manee), As), write(As), nl,

    nl, write('--- Query: related(X, somyot) ---'), nl,
    findall(R, related(R, somyot), Rs), sort(Rs, RsSorted), write(RsSorted), nl,

    halt.
