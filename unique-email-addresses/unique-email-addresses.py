class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashset=set()
        for i in emails:
            split_domain_local=i.split('@')
            domain=split_domain_local[1]
            local=split_domain_local[0]
            local=local.replace('.','')
            plus_lst=local.find('+')
            if plus_lst!=-1:   
                #tmp=local
                local=local[:plus_lst]
                print(split_domain_local[0]+"--->"+local)
            final=local+'@'+domain
            print(final)
            hashset.add(final)
        
        return len(hashset)