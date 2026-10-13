SELECT 
    concat(
        P.matr_pers,
        ' - ',
        ifnull(P.nom,''),
        ' ',
        ifnull(P.pren,'')
        ),
    S.nom_soci, 
    date_format(C.date_arri, '%Y%m%d'), 
    date_format(C.date_sort, '%Y%m%d'),
    C.code_type_cont
FROM BaseHeracles.PERSONNE P, BaseHeracles.SOCIETE S, BaseHeracles.CONTRAT C 
WHERE P.matr_pers=C.matr_pers AND S.code_soci=C.code_soci AND C.matr_pers='matr1' AND C.indi_cont='A' AND C.date_arri='date1'
ORDER BY P.nom ASC, C.date_arri DESC