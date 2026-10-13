SELECT     
    p.pren,
    p.nom,
    p.adre_1, 
    p.adre_2,
    p.vill ,
    p.code_post ,
    p.date_nais ,
    p.nume_ss ,
    p.flag_sexe ,
    n.libe_nati 
FROM BaseHeracles.personne p left outer join BaseHeracles.nationalite n on p.code_nati=n.code_nati
WHERE matr_pers='matr1'