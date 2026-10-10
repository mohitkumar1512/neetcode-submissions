class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            temp = email.split('@')
            # res = ''
            # for char in temp[0]:
            #     if char == '+': break
            #     if char != '.': res += char
            # seen.add(res + '@' + temp[1])
            local = temp[0].split('+')[0].replace('.', '')
            seen.add(local + '@' + temp[1])            
        
        return len(seen)