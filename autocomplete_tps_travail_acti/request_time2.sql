SELECT 
    0,
    0,
    concat(year(ea.date_heur_debu),lpad(month(ea.date_heur_debu),2,'0'),'01'), 
    sum(ea.dure/ea.coef)/3600, 
    (sum(ea.dure/ea.coef)/count(distinct if(ea.nume_rang=0,null,concat(ea.nume_rang,ea.date_heur_acti))))/3600, 
    sum(ea.surf_rang*ea.comp_elem_acti), 
    sum(ea.dure_stan_poid_reco)/3600 , 
    sum(ea.dure*(ifnull(ea.cout_hora_pers,0)+ifnull(ea.cout_hora_acti,0))/ea.coef)/3600
FROM 
    elem_activite ea,
    activite a,  
    BaseHeracles.personne p  
WHERE  
    ea.date_heur_debu>='date1 00:00:00' 
    and 
    ea.date_heur_debu<='date2 23:59:59' 
    and 
    ifnull(ea.date_heur_fin,'')<>''  
    and 
    ea.matr_pers=p.matr_pers 
    and 
    ea.code_acti=a.code_acti 
    and 
    ea.code_acti='act1' 
group by 1,2
order by 2 desc