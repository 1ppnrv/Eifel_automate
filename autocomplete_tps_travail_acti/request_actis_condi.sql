SELECT 
    distinct '' ,
    ea.code_acti,
    ta.flag_paye,
    a.libe_acti  
FROM 
    elem_activite ea  
    left outer join 
    activite a 
    on 
    a.code_acti=ea.code_acti  
    left outer join 
    type_activite ta 
    on 
    ta.code_type_acti=a.code_type_acti  
    left outer join 
    elem_production ep 
    on 
    (ep.code_lign_cond=ea.code_lign_cond and ep.date_heur_debu=ea.debu_elem_prod) 
WHERE 
    a.lieu_acti='C' 
    and 
    ea.date_heur_debu>='date1 00:00:00' 
    and 
    ea.date_heur_fin<='date2 23:59:59'
order by 1,2