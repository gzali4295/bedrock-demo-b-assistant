#a set of predefined prompts

def get_base_prompt(transcript):
    base_prompt = f"""
    Between the <transcript> and </transcript> tags is a transcript from a recorded memo by a Financial Services Advisor (also known as a Banker) regarding a recent visit to a client.
    
    <transcript>{transcript}</transcript>
    """
    return base_prompt

base_prompt_minimal = f"""
Between the <transcript> and </transcript> tags is a transcript from a phone call between a Claims Advisor (also known as a Banker) and a Customer (also know as a Worker) regarding a personal injury insurance claim.

<transcript></transcript>

"""

summary = """\nYour task is to write a brief summary of a recording in dot point form, from the perspective of the Banker. Include a line break between each dot point.

Do not include preamble in your response. Output the summary in the following format:

Transcript Summary:
- (summary dot points)

content of the recording is below:\n
"""

summary_prompt = f"""
\nYour task is to write a detailed summary of the call in dot point form, from the perspective of the Banker. Include a line break between each dot point.

Do not include preamble in your response. Output the summary in the following format:

Transcript Summary:
- (summary dot points)
"""


qa_prompt = f"""
\nYour task is to analyse the transcript and answer each of the questions between the <question_start> and <question_end> tags. Respond with :white_check_mark: if the question can be answered, or :x: if it cannot. 

<question_start>
- Is the date included in the voice note?
- Is there any non-redacted Personal Identifiable Information [PII]? Example credit card numbers, drives license number or date of brith?
- Does the banker have latest financials on file?
- Has the banker scheduled next meeting?
<question_end>

Please put your response in the format of the question then your response and include a line break after each question and response. 
First section is Non Compliant followed by a second section called Compliant. 
List only the questions that have response :x: in the "Non Compliant" section. List only the questions that have response :white_check_mark: in the "Compliant" section

Do not include preamble in your response. 

Use the following as an example:

Non Compliant:
- Has the banker scheduled the next meeting? :x: 

Compliant
- Is there any non-redacted Personal Identifiable Information [PII]? :white_check_mark: 
"""

file_note_prompt=f"""
Write a concise summary of the call in dot point form. Be sure to:
1. Summarise the key points of the visit.
2. Any administrative steps being undertaken by the banker.
3. Any follow up actions or next steps that were mentioned.
4. Write in 1st person from the perspective of the banker.
5. Include a line break between each dot point.

Do not include preamble in your response. Output the summary in the following format

Subject: (one sentence summary of the purpose of the conversation)

Case Details:
- (include summary dot points)

Actions:
- (include administrative steps and follow up actions)
"""

actions_prompt=f"""
Write a concise list of actions that need to be taken by the banker and the client.
Actions should be listed in dot point form.Include a line break between each dot point with a seperate section for customer actions, bank actions and 3rd party actions
Do not include preamble in your response.
Output the list of actions in the following format:

Client actions:
- list the actions that the client needs to take

Banker actions:
- list the actions the banker needs to take

3rd party actions
list of actions actions by others other than the bank or customer
"""


correspondence_prompt=f"""
\nPlease write a letter to the client using the format below. Replace [Next Steps] with a concise list of actions that need to be taken by the banker and the client.
Actions should be listed in dot point form.Include a line break between each dot point with a seperate section for customer actions, bank actions and 3rd party actions
Do not include preamble in your response.
Output the list of actions in the following format:

Dear John and Karen

Thank you for your time today. 

Further to our discussion these are the agreed next steps and actions. 

[Next Steps]
Client actions:
- list the actions that the client needs to take

Banker actions:
- list the actions the banker needs to take

3rd party actions
list of actions actions by others other than the bank or customer







I will contact you early next week to arrange our next meeting. 


Regards



Joseph Banker
jbank@bestbank.com
0431 222 998

"""