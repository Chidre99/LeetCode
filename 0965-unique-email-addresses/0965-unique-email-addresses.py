class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        processed  = set()
        for email in emails:
            local,domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            corrected_email = local + '@' + domain
            processed .add(corrected_email)
        return len(processed)