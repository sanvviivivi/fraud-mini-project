# Fraud Detection App
A simple web app built with Flask that detects fraudulent transactions based on amount.  
Anything above 1,000,000 is marked as Fraud.

# Full Flow
User opens website  
        ↓  
HTML form shows  
        ↓
User enters data  
        ↓  
Clicks button  
        ↓  
HTML sends data → Flask (/check)  
        ↓  
Flask checks fraud rule  
        ↓  
Flask sends result back  
        ↓  
HTML displays result  
