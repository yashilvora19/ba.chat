# BA.Chat

**Basically Affordable:** Making insurance and healthcare simpler, one chat at a time!

Time is money. We save both. Come try out ba.chat and save on time and money. Insurance stress? Chat with our personalized assistant and find the best path to maximize your insurance benefits and get better!

1. Upload your diagnosis into the system
2. Insurance policy should be in the database
3. Based on this, we reccommend hospitals- present costs as well- AGENT 1
4. Hospital bills are inaccurate- have the model compare hospital bills and how we can cut down on costs- also draft a mail and send it to negatiate costs- AGENT 2
5. Designs the email- doesn't send it- we want to actually send it

- Input: Written diagnosis of the doctor + insurance company and plan
- 2-3 insurance companies for now- UC SHIP, Kaiser Permanente, etc- we'll have the database for these companies
- Pull the relevant data from plan- estimating costs- suggest how to maximize the insurance benefit (LLM agents)
-  Suggest appointment times based on location and calender- present phone numbers for this (Maps + calendar API)
-  Write an email to insurance company to lower costs- negotiating (Gemini API)
