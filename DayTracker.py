class DayTracker:       
    #{Segunda, terça, quarta, quinta, sexta}    
    day = Segunda
    #{work, holiday, vacation, compensated}
    dayType = work
    
    #from csv
    workTimeDuration
    ''ht = hours tracker
    def __init__(self):
        dayType = 'work'
        
    def addRow(self, htRow):
        '''
            "Job","Clocked In","Clocked Out","Duration","Comment","Tags","Breaks","Adjustments","TotalTimeAdjustment","TotalEarningsAdjustment"
            "SIBS","21/02/17 12:51","21/02/17 17:12","4,35","Mastercard pin offline autorizações  Recibo Bits","ARCTIC - Construction - Suporte interno/externo sem SW","","","",""
        '''
        
   #