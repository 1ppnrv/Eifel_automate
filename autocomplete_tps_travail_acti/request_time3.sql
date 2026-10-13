SELECT 
    date_format(min(ea.date_heur_debu),'%Y%m%d'), 
    date_format(max(ea.date_heur_debu),'%Y%m%d%H%i%s'),
    concat(year(ea.date_heur_debu),lpad(month(ea.date_heur_debu),2,'0'),'01'), 
    sum(dure/coef)/3600 
FROM  
    elem_activite ea , 
    BaseHeracles.personne p  
WHERE 
    ea.date_heur_debu>='date1 00:00:00' 
    and 
    ea.date_heur_debu<='date2 23:59:59' 
    and 
    ea.code_acti='act1' 
    and 
    p.matr_pers = ea.matr_pers 
GROUP BY ea.code_acti,3 
order by 3