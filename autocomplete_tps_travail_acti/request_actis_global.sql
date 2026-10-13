SELECT 
    ea.code_acti, 
    ea.code_acti, 
    a.libe_acti,
    ta.flag_paye,
    count(distinct eap.code_acti),
    a.rend_stan   
FROM 
    elem_activite ea ,
    activite a,
    type_activite ta  
    left outer join 
        elem_acti_produit eap 
        on 
        ea.matr_pers=eap.matr_pers 
        and 
        ea.code_acti=ea.code_acti 
        and 
        ea.date_heur_debu=eap.date_heur_debu 
WHERE 
    ea.code_acti=a.code_acti 
    and 
    ta.code_type_acti=a.code_type_acti 
    and  
    ea.date_heur_debu between '20260701 00:00:00' and '20260731 23:59:59' 
    and ea.nume_serr=0 
    and ea.code_acti NOT IN ('0099', 'PRES', '10001', '10000', '10002', '10003', '1120') 
group by 1 
order by 1