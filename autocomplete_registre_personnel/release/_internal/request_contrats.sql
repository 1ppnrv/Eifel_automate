SELECT code_type_cont, matr_pers, code_soci
FROM BaseHeracles.contrat 
WHERE date_arri > 'datenow' AND indi_cont<>'A';