SELECT 
    0,
    concat(year(ea.date_heur_debu),lpad(month(ea.date_heur_debu),2,'0')),
    '' as nr,
    sum(dure/coef)/3600
    
FROM BaseSolane.elem_activite ea, BaseHeracles.personne p
WHERE  
    ea.date_heur_debu 
    between 'date1 00:00:00' and 'date2 23:59:59' 
    and ea.nume_serr=0 
    and ea.matr_pers=p.matr_pers 
    and ea.code_acti='act1'
group by 1  
order by 1