class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()  
        # Create an empty set to store unique (processed) email addresses

        for email in emails:  
            # Loop through each email in the input list
            
            local, domain = email.split('@')  
            # Split the email into local part and domain part at '@'
            # Example: "test.email+alex@gmail.com"
            # local = "test.email+alex", domain = "gmail.com"
            
            local = local.split("+")[0]  
            # Ignore everything after '+' in the local part
            # "test.email+alex" → "test.email"
            
            local = local.replace(".", "")  
            # Remove all '.' from the local part
            # "test.email" → "testemail"
            
            unique.add((local, domain))  
            # Add the processed email as a tuple to the set
            # Using a set ensures only unique emails are stored
        
        return len(unique)  
        # Return the number of unique processed email addresses