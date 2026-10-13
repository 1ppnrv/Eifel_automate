SELECT 
       date_format(ea.date_heur_debu,'%Y%m'),
       date_format(ea.date_heur_debu,'%Y%m01'),
       sum(ea.comp_elem_acti), 
       sum(ea.dure/ea.coef)/3600
FROM 
     BaseSolane.elem_activite ea, 
     BaseSolane.activite a, 
     BaseHeracles.personne p  
WHERE  
       ea.date_heur_debu between 'date1 00:00:00' and 'date2 23:59:59' 
       and 
       ifnull(ea.date_heur_fin,'')<>'' 
       and 
       ea.nume_serr<>0  
       and 
       ea.matr_pers=p.matr_pers 
       and 
       ea.code_acti=a.code_acti 
       and 
       ea.code_acti='act1' 
group by 1,2 
order by 2