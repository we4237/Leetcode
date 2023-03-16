from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for email in emails:
            i = email.index('@')
            local = email[:i].split('+',1)[0] #保留第一个+号以前的内容
            local = local.replace('.','')
            emailSet.add(local+email[i:])
        return len(emailSet)