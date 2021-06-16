"""
Unique Email Addresses
"""


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            plus_sign = email.find("+")
            dot = email.find(".")
            at = email.find("@")
            clean_email_address = ""
            if dot < at or dot < plus_sign:
                if plus_sign != -1:
                    clean_email_address += email[:plus_sign].replace(".", "") + email[at:]
                else:
                    clean_email_address += email[:at].replace(".", "") + email[at:]
            elif plus_sign != -1:
                clean_email_address = email[:plus_sign].replace(".", "") + email[at:]

            if clean_email_address:
                unique_emails.add(clean_email_address)
            else:
                unique_emails.add(email)

        return len(unique_emails)
