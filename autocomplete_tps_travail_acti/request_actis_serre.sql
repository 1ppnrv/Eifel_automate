SELECT DISTINCT 
    ea.code_acti, 
    ea.code_acti, 
    a.libe_acti, 
    round(avg(sac.temp_stan),1), 
    a.code_type_acti,
    a.code_loca,
    round(avg(sac.nomb_tete_heur_stan),0),
    ta.flag_paye  
FROM 
    BaseSolane.elem_activite ea, 
    BaseSolane.activite a,
    BaseSolane.type_activite ta  
    left outer join 
        standard_activite_culture sac 
        on 
        sac.code_acti=ea.code_acti 
        and (sac.code_cult=ea.code_cult 
            or 
            sac.code_cult='0' 
            or 
            sac.code_cult is null 
            )  
WHERE 
    ea.date_heur_debu>='date1 00:00:00'
    and 
    ea.date_heur_debu<='date2 23:59:59' 
    and 
    ifnull(ea.date_heur_fin,'')<>'' 
    and 
    ea.nume_serr<>0 
    and 
    a.lieu_acti 
    in('S','P') 
    and 
    ea.code_acti=a.code_acti 
    and 
    ta.code_type_acti=a.code_type_acti  
    and 
    ifnull(a.flag_reco,'N')<>'O'  
group by 1,2  
ORDER BY 4,1