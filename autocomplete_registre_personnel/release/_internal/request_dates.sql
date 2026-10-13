select 
    max(
        if(
            date_arri<=curdate() 
            and (
                date_sort>curdate()
                or ifnull(date_sort,0)*1=0 
                ),
            concat( 
                date_format(date_arri,'%Y%m%d'),
                '&',
                date_format(ifnull(date_sort,''),'%Y%m%d')
                ),
            ''
        )
    ),
    min(
        if(
            date_arri>curdate(),
            concat(
                date_format(date_arri,'%Y%m%d'),
                '&',
                date_format(ifnull(date_sort,''),'%Y%m%d')
                ),
            '22220101'
            )
        ) ,
    max(
        if(
            date_arri<curdate()
            and ifnull(date_sort,0)*1 between 1 and curdate(),
            concat( 
                date_format(date_arri,'%Y%m%d'),
                '&',
                date_format(ifnull(date_sort,''),'%Y%m%d')
                ),
            ''
            )
        )  
from BaseHeracles.contrat 
where matr_pers = 'matr1'